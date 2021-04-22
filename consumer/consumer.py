from prometheus_client import start_http_server,Counter
from kafka import KafkaConsumer
from kafka import KafkaProducer
import time 
import os

key = "KAFKA_SERVICE_NAME"
kafka = os.getenv(key)

consumer = KafkaConsumer (bootstrap_servers = f'{kafka}:9092')
consumer.subscribe(['input'])
producer = KafkaProducer(bootstrap_servers = f'{kafka}:9092')
start_http_server(8000)
p = Counter('produce_massage', 'Description of counter')

for msg in consumer:
     epoch_time = msg.value
     standard_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(epoch_time)))
     producer.send('output', standard_time.encode("utf-8") )
     p.inc()
