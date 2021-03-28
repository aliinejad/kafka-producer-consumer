from kafka import KafkaConsumer
from kafka import KafkaProducer
import time 
import os

key = "KAFKA_SERVICE_NAME"
kafka = os.getenv(key)

consumer = KafkaConsumer (bootstrap_servers = f'{kafka}:9092'))
consumer.subscribe(['input'])
producer = KafkaProducer(bootstrap_servers = f'{kafka}:9092') )

for msg in consumer:
     epoch_time = msg.value
     standard_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(epoch_time)))
     producer.send('output', bytes(standard_time , 'utf-8') )
