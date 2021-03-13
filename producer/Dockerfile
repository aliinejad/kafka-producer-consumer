FROM python:3.7-alpine
WORKDIR /code
RUN pip install pip install kafka-python
COPY . .
CMD ["python", "producer.py"]
