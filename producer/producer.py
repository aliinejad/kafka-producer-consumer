from kafka import KafkaProducer
import time
import os
key = "KAFKA_SERVICE_NAME"
kafka = os.getenv(key)
producer = KafkaProducer(bootstrap_servers = f'{kafka}:9092')
while True :
    producer.send('input', bytes(str(time.time()) , 'utf-8'))
    time.sleep(1)

