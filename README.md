# Mongo API demo

Simple project showing off how to integrate an external API and store data
into Mongo.

Demo for http://cdl.rosedu.org/.


## How to run

```bash
docker-compose build
docker-compose up
```

This will start a Mongo container and a fetcher container. The fetcher will
get the comments of a given product (see `main.py`) from a shopping website,
annotate them with sentiment and store them in Mongo.

You can then use the Mongo shell to explore the stored data.

## Accessing the database

```bash
docker exec -it mongoapidemo_db_1 mongo
```

This will connect to the Mongo container and start a shell. From here, you can
take a look at the data:

```javascript
> use test
switched to db test
> db.getCollectionNames()
[ "comment" ]
> db.comment.findOne()
{
	"_id" : ObjectId("58e6a88de03e3f000144eaef"),
	"text" : "Il folsesc de un an aproximativ,pot spune ca nu am avut nici cea mai mica problema cu el, reda toate pozele/filmele. L-am folosit si pe un ps3, merge excelent. Foarte multumit",
	"type" : "pro",
	"sentiment" : "positive"
}
```

## Example queries

How many cons were fetched?

```javascript
> db.comment.find({"type": "con"}).count()
16
```

How many positive comments were misannotated?

```javascript
> db.comment.find({"type": "pro", "sentiment": "negative"}).count()
6
```

