#!/bin/sh

crontab -l > workercron

echo "0 * * * * /usr/local/bin/python /app/worker.py >> /var/log/cron.log 2>&1" >> workercron

crontab workercron
rm workercron

cron -f
