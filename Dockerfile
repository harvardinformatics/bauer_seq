FROM python:3.6
RUN mkdir /code
WORKDIR /code
RUN pip install django
RUN pip install mysqlclient
ADD . /code/
ENV PYTHONPATH /code
