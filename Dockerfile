FROM python:3.12

WORKDIR /receipt-processor

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python", "./app/main.py"] 