# kafka-produser-consumer

this is consumer and producer program in python programming language
  - producer continuously write messages to 'input' topic with epoch timestamp in ms
  - consumer reads from 'input' topic, transforms input message to date string (must be in RFC 3339) and sends to topic 'output'


## install charts 
 for installing charts with helm in kubernetese cluster :
  - install producer helm chart 
    - this chart automatically install kafka and zookeeper for dependency
  - then install consumer helm chart with kafkahost flag 


```console
helm install producer ./producer/producer-chart

helm install consumer ./consumer/consumer-chart --set kafkahost=producer-kafka
```
