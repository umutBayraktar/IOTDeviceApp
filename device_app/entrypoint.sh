#!/bin/bash


# Stop execution if we have an error
set -e

# Get host:port from parameters list
host="$1"

# Remove first argument from list of parameters (host)
# shift

# Try to connect to PostgreSQL
until PGPASSWORD=$DB_PASSWORD psql -h "$DB_HOST" -U "$DB_USER" -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  echo "DB_PASSWORD: $DB_PASSWORD"
  echo "DB_USER: $DB_USER"
  echo "db: $db"
  echo "1: $1"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

#python manage.py test
# python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
exec "$@"
