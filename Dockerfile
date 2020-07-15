FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
	wget \
	xvfb \
	unzip \
	python3-pip \
	python3-dev \
	python3-setuptools

ENV CHROME_VERSION "google-chrome-stable"
RUN sed -i -- 's&deb http://deb.debian.org/debian jessie-updates main&#deb http://deb.debian.org/debian jessie-updates main&g' /etc/apt/sources.list \
  && apt-get update && apt-get install wget -y
ENV CHROME_VERSION "google-chrome-stable"
RUN wget --no-check-certificate -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list \
  && apt-get update && apt-get -qqy install ${CHROME_VERSION:-google-chrome-stable}

RUN google-chrome --version

RUN mkdir -p /app

WORKDIR /app

COPY . /app

RUN pip3 install selenium
RUN pip3 install bs4
RUN pip3 install configparser

ENV LC_ALL=C.UTF-8
ENV PYTHONUNBUFFERED 0

EXPOSE 4000

ENTRYPOINT ["python3", "/app/crawler.py"]