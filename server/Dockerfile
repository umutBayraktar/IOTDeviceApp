# syntax=docker/dockerfile:1
FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
# COPY ./server/requirements.txt /code/requirements.txt
COPY . /code/
RUN pip install -r requirements.txt
# COPY . /code/
EXPOSE 65432

CMD ["python", "server.py"]