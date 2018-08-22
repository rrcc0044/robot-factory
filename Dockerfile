FROM python:3.6
ENV PYTHONUNBUFFERED 1

# -- Install Pipenv:
RUN pip3 install pipenv

# -- Adds our application code to the image
COPY . code
WORKDIR code

# -- Install dependencies:
RUN pipenv install --deploy --system

EXPOSE 8000

# -- Migrates the database, uploads staticfiles, and runs the production server
CMD ./manage.py migrate && \
    ./manage.py collectstatic --noinput && \
    newrelic-admin run-program gunicorn --bind 0.0.0.0:$PORT --access-logfile - robot_factory.wsgi:application
