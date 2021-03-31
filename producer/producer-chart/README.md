## producer 
this chart run producer app that continuously write messages to 'input' topic in kafka with epoch timestamp in ms

this chart automatically install kafka and zookeeper chart for dependency and connect to them automatically


## TL;DR

```console
helm install < chart name > < chart path > 

## example

helm install producer ./producer/producer-chart 
```


