FROM python:3.8-slim-buster

ENV DEBIAN_FRONTEND=noninteractive

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN echo deb http://deb.debian.org/debian/ unstable main contrib non-free >> /etc/apt/sources.list && \
	apt-get update && export DEBIAN_FRONTEND=noninteractive \
	&& apt-get install -y --fix-missing \
		#git \
		#make \
		#curl \
		#unzip \
		#wget \
		#gnupg \
		#gnupg2 \
		#gnupg1 \
	&& apt-get autoremove -y \
	&& apt-get clean \
	&& apt-get autoclean

CMD [ "python", "./newsbotApi/run.py" ]