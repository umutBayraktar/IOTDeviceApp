FROM python:3.10

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y
RUN apt-get -y install binutils libproj-dev gdal-bin postgresql-client python3-lxml
RUN apt-get -y install libmemcached-dev

RUN mkdir /code
WORKDIR /code
COPY ./device_app /code/
RUN pip install -r requirements.txt
COPY ./device_app/scripts/entrypoint.sh /code/scripts/entrypoint.sh
RUN chmod +x /code/scripts/entrypoint.sh
CMD ["/code/repo/IOTDeviceApp/device_app/scripts/entrypoint.sh"]