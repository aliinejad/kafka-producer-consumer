from kafka import KafkaProducer
import time
producer = KafkaProducer(bootstrap_servers='localhost:9092')
while True :
    producer.send('input', bytes(str(time.time()) , 'utf-8'))
    time.sleep(1)

