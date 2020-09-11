# syntax=docker/dockerfile:experimental
FROM python:3.6

EXPOSE 80
RUN apt-get update -y && apt-get install -y \
    nginx \
    supervisor \
    curl
RUN mkdir ~/.ssh && echo "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config

RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY etc/nginx.conf /etc/nginx/sites-available/default
COPY etc/supervisor.conf /etc/supervisor/conf.d/app.conf

RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && apt-get install -y nodejs
RUN apt-get install npm -y
RUN npm install npm@latest -g

WORKDIR /app

ARG DJVOCAB_COMMIT=a0cfeba93ea805d3861e97e9c38fd27447e5b58a
ARG IFXURLS_COMMIT=72f75b3fcc9446fc5095ad747b3ed53d05bc4799
ARG IFXUSER_COMMIT=701eec94d06e83fcb42416b9fb07255569c4c2c4
ARG IFXAUTH_COMMIT=d184b09de3159c1d437171262f30d7f20c9b174c
ARG IFXMAIL_CLIENT_COMMIT=b649c6ed9edfa7cae5a402485e689fcaf1e3dc86

COPY requirements.txt /app

RUN --mount=type=ssh pip install --upgrade pip && \
    pip install 'Django>2.1,<3' && \
    pip install gunicorn && \
    pip install git+ssh://git@github.com/harvardinformatics/djvocab.git@${DJVOCAB_COMMIT} && \
    pip install git+ssh://git@github.com/harvardinformatics/ifxurls.git${IFXURLS_COMMIT} && \
    pip install git+ssh://git@github.com/harvardinformatics/ifxuser.git@${IFXUSER_COMMIT} && \
    pip install git+ssh://git@github.com/harvardinformatics/ifxauth.git@${IFXAUTH_COMMIT} && \
    pip install git+ssh://git@github.com/harvardinformatics/ifxmail.client.git@${IFXMAIL_CLIENT_COMMIT} && \
    pip install -r requirements.txt

ADD . /app

ENV PYTHONPATH /app

RUN rm -rf /app/frontend/dist/* && rm -rf /app/static/* && rm -rf /app/frontend/node_modules/* && (cd frontend && npm install . && npm run-script build)
RUN mkdir -p /app/frontend/dist/static && ./manage.py collectstatic --noinput
RUN cp -r /app/frontend/dist/* /app/static

CMD ./manage.py makemigrations && ./manage.py migrate && /usr/bin/supervisord -n

