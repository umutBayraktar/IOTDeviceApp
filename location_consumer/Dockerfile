# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update -y
RUN apt-get -y install binutils libproj-dev gdal-bin postgresql-client python3-lxml
RUN apt-get -y install libmemcached-dev

WORKDIR /code
COPY ./location_consumer/requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8000
CMD ["python", "location_consumer/main.py"]