FROM python:3.9-slim-bullseye
ENV DEBIAN_FRONTEND=noninteractive
RUN echo deb http://deb.debian.org/debian/ unstable main contrib non-free >> /etc/apt/sources.list && \
	apt-get update \
	&& export DEBIAN_FRONTEND=noninteractive \
	&& apt-get install -y \
		git \
		make \
	&& apt-get autoremove -y \
	&& apt-get clean \
	&& apt-get autoclean

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
