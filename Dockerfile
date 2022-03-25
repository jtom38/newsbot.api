FROM python:3.10.4-slim-bullseye

ENV DEBIAN_FRONTEND=noninteractive

#RUN echo deb http://deb.debian.org/debian/ unstable main contrib non-free >> /etc/apt/sources.list && \
#	apt-get update \
#	&& apt-get install -y --fix-missing \
#	&& apt-get autoremove -y \
#	&& apt-get clean \
#	&& apt-get autoclean

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt

CMD ["uvicorn", "newsbotApi.run:app", "--host", "0.0.0.0", "--port", "8000"]