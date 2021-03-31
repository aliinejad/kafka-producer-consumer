# kafka-produser-consumer

this is consumer and producer program in python programming language
  - producer continuously write messages to 'input' topic with epoch timestamp in ms
  - consumer reads from 'input' topic, transforms input message to date string (must be in RFC 3339) and sends to topic 'output'
