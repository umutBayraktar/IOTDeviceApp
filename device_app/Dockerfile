FROM python:3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get -y install binutils libproj-dev gdal-bin postgresql-client python3-lxml
RUN apt-get -y install libmemcached-dev

RUN mkdir /code
COPY ./device_app /code/
WORKDIR /code
RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh
CMD ["sh", "entrypoint.sh"]