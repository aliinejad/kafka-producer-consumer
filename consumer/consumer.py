from kafka import KafkaConsumer
from kafka import KafkaProducer
import time 


consumer = KafkaConsumer (bootstrap_servers = 'localhost:9092')
consumer.subscribe(['input'])
producer = KafkaProducer(bootstrap_servers='localhost:9092')

for msg in consumer:
     epoch_time = msg.value
     standard_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(float(epoch_time)))
     producer.send('output', standard_time )