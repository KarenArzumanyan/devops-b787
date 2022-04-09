FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN pip install requests

ENV SITEURL=novalue

CMD ["python3", "loadicon.py"]