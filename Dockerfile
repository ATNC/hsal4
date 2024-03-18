FROM python:3.12.1-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get -y install cron nano

COPY worker.py /app/worker.py
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
RUN touch /var/log/cron.log

ENTRYPOINT ["/bin/sh", "/app/entrypoint.sh"]