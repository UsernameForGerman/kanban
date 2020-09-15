FROM python:3.6.11-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y \
  # psycopg2 dependencies
  && apt-get install gcc -y \
  && apt-get install libpq-dev -y

RUN addgroup --system kanban \
    && adduser --system --group kanban --shell /bin/sh

WORKDIR /home/kanban/

RUN mkdir -p /var/kanban/static/
RUN mkdir -p /var/kanban/media/

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/requirements.txt \
    && rm -rf /requirements

COPY ./compose/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint
RUN chown kanban /entrypoint

COPY ./compose/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start
RUN chown kanban /start

COPY ./config /kanban/config
COPY ./kanban /kanban/kanban
COPY ./tasks /kanban/tasks
COPY ./manage.py /kanban

RUN chown -R kanban /kanban
RUN chown -R kanban /var/kanban/static
RUN chown -R kanban /var/kanban/media

USER kanban

WORKDIR /kanban

ENTRYPOINT ["/entrypoint"]