FROM python:3.8.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/mus_cloud

COPY mus_cloud/requirements.txt ./

RUN pip3 install -r requirements.txt
