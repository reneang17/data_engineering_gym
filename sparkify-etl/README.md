# Data modeling with Postgres

This project creates relation database in postgres `sparkifydb` for a music app, **Sparkify**. 
This allows to perform queries on data extracted by song and log json
from the ![Million Song Dataset](http://millionsongdataset.com/).

We use the star **schema**, as we mean to optimize for queries for data analysis.


## Schema and ETL pipeline

The json files corresponding to song info and log user history, 
was extracted via a ETL pipeline whose final results is a 
fact table (songplays) that contains 

- *Name:* `songplays`,  Fact table

| Column | Type | Description 
| ------ | ---- | ----------------------- |
| `songplay_id` | `SERIAL PRIMARY KEY` | 
| `start_time` | `BIGINT NOT NULL` | 
| `user_id` | `INT NOT NULL` | 
| `level` | `VARCHAR` | 
| `song_id` | `VARCHAR` | 
| `artist_id` | `VARCHAR(255)` | 
| `session_id` | `INT` | 
| `location` | `VARCHAR` | 
| `user_agent` | `VARCHAR(255)` | 

and 4 *dimension* tables users, songs, artists and  time, see below. 


The **create_tables.py** script contains the `CREATE` and  `DROP`  use to create the database and empty tables tables. 
Finally, the etl.py script extracts the information of song and logs files and use  `INSERT`and `SELECT` queries in **create_tables.py** to fill the tables. Assuming, there are not collision of the enties in such files 
use `ON CONFLICT DO NOTHING`.  Below find the  final ERD diagram (produced via www.lucidchart.com).


![](ERD_sparkigy.png?raw=true)


## Song play example queries

Day of the week music with more song reproductions:

`SELECT COUNT(weekday) FROM time
ORDER BY weekday;`

The average duration of the song each gender listens to (why not?! XD):

`SELECT u.gender, AVG(s.duration)
FROM songplays AS sp
JOIN songs AS s 
ON s.song_id = sp.song_id
JOIN users AS u
ON u.user_id = sp.user_id
GROUP BY 
u.gender
`