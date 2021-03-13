 
from kafka import KafkaProducer
import time
producer = KafkaProducer(bootstrap_servers='localhost:9092')
while True :
    t = str(time.time())
    producer.send('input', t )
    time.sleep(1)

