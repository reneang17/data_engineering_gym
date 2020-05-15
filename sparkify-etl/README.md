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


<p align="center">
  <img  src="./media/ERD_sparkigy.png">
</p>


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

## Run this project with docker

Build container and image as a local server running on port 5555

`docker build -t postgres-student-image .`

`docker run -d --name sparkigy-container -p 5555:5432 postgres-student-image`

then install requirement and run the scripts create_tables.py, then etl.py and check the jupyter nb test.ipynb.
Clean the server/databse running.

docker stop sparkigy—student-container
docker rm sparkigy—student-container
docker rmi sparkigy—student-image

Have a look at ![tutorial](https://medium.com/@wkrzywiec/database-in-a-docker-container-how-to-start-and-whats-it-about-5e3ceea77e50), 
![reference](https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/) and 
![reference](https://stackoverflow.com/questions/53610266/cannot-connect-to-postgres-container-using-psycopg2) expand 
on how to deal with connecting multiple containers.

