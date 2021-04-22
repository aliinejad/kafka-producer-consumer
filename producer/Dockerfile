FROM python:3.7-alpine
WORKDIR /code
RUN pip install kafka-python
RUN pip install prometheus_client
COPY . .
EXPOSE 8000
CMD ["python", "producer.py"]
