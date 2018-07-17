from django.http import JsonResponse
from rest_framework.authtoken.models import Token
import logging

def get_remote_user_auth_token(request):
    #header = "HTTP_REMOTE_USER"
    #username = request.META[header]
    token = Token.objects.get(user=request.user)
    return JsonResponse({'token': str(token)})
