from django.contrib import auth
from django.contrib.auth.middleware import RemoteUserMiddleware
from django.core.exceptions import ImproperlyConfigured
from rest_framework.authtoken.models import Token
import logging, os
from bauer.settings import DEBUG


logger = logging.getLogger(__name__)


class RemoteUserPlusMiddleware(RemoteUserMiddleware):
    """
    If request.user is not authenticated, then this middleware attempts to
    authenticate the username passed in the ``REMOTE_USER`` request header.
    If authentication is successful, the user is automatically logged in to
    persist the user in the session.

    If it is the first time the user has been seen in the session, an attempt
    is made to fetch name, email, etc. from RC AD.

    If this works and information is different than what was previously there,
    the information will be stored and a "please review" flag
    will be added to the user table.
    """

    # Name of request header to grab username from.  This will be the key as
    # used in the request.META dictionary, i.e. the normalization of headers to
    # all uppercase and the addition of "HTTP_" prefix apply.
    header = "HTTP_HKEYMAIL"
    huid_header = "HTTP_X_REMOTE_USER"
    header_dev = "HTTP_REMOTE_USER"
    force_logout_if_no_header = True

    def process_request(self, request):
        # AuthenticationMiddleware is required so that request.user exists.
        if not hasattr(request, 'user'):
            raise ImproperlyConfigured(
                "The Django remote user auth middleware requires the"
                " authentication middleware to be installed.  Edit your"
                " MIDDLEWARE setting to insert"
                " 'django.contrib.auth.middleware.AuthenticationMiddleware'"
                " before the RemoteUserMiddleware class.")
        try:
            logger.debug("Checking header for REMOTE_USER")
            if DEBUG and os.environ.get("IFX_REMOTE_USER"):
                logger.debug('ifx remote user')
                username    = os.environ.get("IFX_REMOTE_USER").strip()
                huid        = os.environ.get("IFX_HUID").strip()
            elif DEBUG and self.header_dev in request.META:
                logger.debug('dev header found')
                username    = request.META[self.header_dev]
            else:
                logger.debug('looking for prod header')
                username    = request.META[self.header]
                huid    = request.META[self.huid_header]
            logger.debug("User %s logged in" % username)
            #for k, v in request.META.items():
            #    logger.debug("%s = %s" % (k, v))
        except KeyError:
            # If specified header doesn't exist then remove any existing
            # authenticated remote-user, or return (leaving request.user set to
            # AnonymousUser by the AuthenticationMiddleware).
            logger.debug("Key error in check for header.  META headers are %s" % "\n".join(request.META.keys()))
            if self.force_logout_if_no_header and request.user.is_authenticated:
                self._remove_invalid_user(request)
            return
        # If the user is already authenticated and that user is the user we are
        # getting passed in the headers, then the correct user is already
        # persisted in the session and we don't need to continue.
        logger.debug("Checking for authenticated user")
        if request.user.is_authenticated:
            if request.user.get_username() == self.clean_username(username, request):
                return
            else:
                # An authenticated user is associated with the request, but
                # it does not match the authorized user in the header.
                self._remove_invalid_user(request)

        # We are seeing this user for the first time in this session, attempt
        # to authenticate the user.
        logger.debug("User not authenticated.  Trying...")
        user = auth.authenticate(remote_user=username)
        if user:
            logger.debug("User is valid")
            # User is valid.  Set request.user and persist user in the session
            # by logging the user in.
            request.user = user
            auth.login(request, user)
            Token.objects.get_or_create(user=user)

