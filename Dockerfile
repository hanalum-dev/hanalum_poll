FROM python:3
ENV PYTHONUNBU  FFERED 1
WORKDIR /hanalum_poll
COPY . .
RUN apt-get update -y
RUN apt-get upgrade -y
RUN pip install -r requirements.txt