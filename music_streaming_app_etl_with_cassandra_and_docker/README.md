
# Music-streaming-app, analytics with Apache Cassandra


In this project, from my Data Enginerring Udacity degree, I create a NoSQL using Apache Cassandra database `sparkifyks` for a music streming app, *Sparkify*. The purpose of this database is creating tables to answer the following queries:

1. song title and song's length in the music app history heard for given sessionId and  itemInSession.

2. name of artist, song (sorted by itemInSession) and user first and last name given userid  and sessionid.
    
3. user first and last  of who listent to given song title.

<br>

## ETL pipeline

Historical data of the music app is stored into csv files split by date, inside the data folder.
This data is ETL pipelined by **sparkify.ipynb**. Firstly into a master file **event_datafile_new.csv**, and subsequently used to load data into 3 tables (session_item, user_session, songs_userId). 

<br>

## Example queries

```{sql}
SELECT artist, song, length FROM session_item 
WHERE sessionId = '338' and itemInSession = '4';
```

```{sql}
SELECT artist, song, itemInSession, song, firstName, lastName
FROM user_session 
WHERE userId = '10' and sessionId = '182';
```

```{sql}
SELECT song, firstName, lastName 
FROM songs_userId 
WHERE song='All Hands Against His Own';
```

<br>

## Start node with Docker
To start the running enviroment build and run the container using

```{bash}
docker-compose up
```

This command authomatically run the yaml configuration file I took from [awesome post](https://medium.com/swlh/building-a-python-data-pipeline-to-apache-cassandra-on-a-docker-container-fc757fbfafdd).

Run the following to clean up:

```{bash}
docker stop cassandra
docker rm cassandra
docker rmi cassandra
```

