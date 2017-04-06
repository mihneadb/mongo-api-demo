# Mongo API demo

Simple project showing off how to integrate an external API and store data
into Mongo.

Demo for http://cdl.rosedu.org/.


## How to run

```bash
docker-compose up
```

This will start a Mongo container and a fetcher container. The fetcher will
get the comments of a given product (see `main.py`) from a shopping website,
annotate them with sentiment and store them in Mongo.

One can then use the Mongo shell to explore the stored data.

