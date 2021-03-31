

| Parameter                 | Description                                     | Default                                                 |
|---------------------------|--------------------------------------------------------|--------------------------------------------------|
| `      kafkahost     `    | kafkahost name for connect consumer                    | `producer-kafka`                                 |



```console
helm install consumer ./consumer/consumer-chart --set kafkahost=<producer-cahrt name>-kafka
```
