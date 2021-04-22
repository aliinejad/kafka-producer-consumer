from prometheus_client import start_http_server,Counter
from kafka import KafkaProducer
import time
import os


key = "KAFKA_SERVICE_NAME"
kafka = os.getenv(key)
producer = KafkaProducer(bootstrap_servers = f'{kafka}:9092')
start_http_server(8000)
c = Counter('produce_massage', 'Description of counter')
while True :
    t = str(time.time())
    producer.send('input', t.encode("utf-8") )
    time.sleep(1)

