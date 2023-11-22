FROM python:3.11-alpine

WORKDIR /testnet-backup-bot

COPY . .

RUN chmod +x create_backup.py

RUN pip install pipenv

RUN pipenv install --system --deploy

CMD ["python", "create_backup.py"]