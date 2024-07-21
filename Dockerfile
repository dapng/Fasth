FROM python:3.9-slim

WORKDIR /test

COPY . .

WORKDIR .

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0"]