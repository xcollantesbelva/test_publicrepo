FROM python:3.9-slim

WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir fastapi uvicorn

EXPOSE 5000

CMD ["uvicorn", "app:cat", "--host", "0.0.0.0", "--port", "5005"]
