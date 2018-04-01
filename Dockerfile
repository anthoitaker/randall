FROM python:3.6
LABEL maintainer="Toni Robles <r21robles@gmail.com>"

WORKDIR /code

COPY requirements.txt /code

RUN pip3 install --upgrade pip \
 && pip3 install -r requirements.txt

ADD . /code

VOLUME /data/randall

EXPOSE 80

CMD ["gunicorn", "config.wsgi", "-b", "0.0.0.0:80"]
