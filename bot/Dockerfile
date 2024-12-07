FROM python:3.11.9-alpine


COPY ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .

CMD ["/bin/sh", "-c", "python app.py"]