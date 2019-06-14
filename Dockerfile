FROM python:3.6.5-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]