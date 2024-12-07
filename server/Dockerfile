FROM python:3.11.9-alpine

COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .

COPY ./wait-for-it.sh /usr/local/bin/wait-for-it
RUN apk add --no-cache bash

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info"]