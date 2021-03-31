## consumer
this chart run consumer app that reads from 'input' topic in kafka and transforms input message to date string (must be in RFC 3339) and sends to topic 'output'





| Parameter                 | Description                                     | Default                                                 |
|---------------------------|--------------------------------------------------------|--------------------------------------------------|
| `      kafkahost     `    | kafkahost name for connect consumer                    | `producer-kafka`                                 |


## TL;DR

```console
helm install < chart name > < chart path > --set kafkahost=<producer-cahrt name>-kafka

## example

helm install consumer ./consumer/consumer-chart --set kafkahost=producer-kafka
```
