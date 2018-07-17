FROM python:3.6

EXPOSE 80
RUN apt-get update -y && apt-get install -y \
    nginx \
    sendmail \
    supervisor

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY etc/nginx.conf /etc/nginx/sites-available/default
COPY etc/supervisor.conf /etc/supervisor/conf.d/app.conf
COPY etc/.htpasswd /etc/nginx/.htpasswd

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt && \
    pip install gunicorn

ADD . /app/
ENV PYTHONPATH /app

CMD ["/usr/bin/supervisord","-n"]
