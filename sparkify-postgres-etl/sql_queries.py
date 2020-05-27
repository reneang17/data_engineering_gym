# DROP TABLES

drop_prefix= "DROP TABLE IF EXISTS "

songplay_table_drop = drop_prefix + "songplays;"
user_table_drop = drop_prefix + "users;"
song_table_drop = drop_prefix + "songs;"
artist_table_drop = drop_prefix + "artists;"
time_table_drop = drop_prefix + "time;"

# CREATE TABLES

create_prefix =  "CREATE TABLE IF NOT EXISTS "

songplay_table_create = create_prefix + """songplays (
        songplay_id SERIAL PRIMARY KEY,
        start_time BIGINT NOT NULL,
        user_id INT NOT NULL,
        level VARCHAR,
        song_id VARCHAR,
        artist_id VARCHAR(255),
        session_id INT,
        location VARCHAR,
        user_agent VARCHAR(255)
        );"""

user_table_create = create_prefix + """users (
        user_id INT PRIMARY KEY,
        first_name VARCHAR,
        last_name VARCHAR,
        gender VARCHAR,
        level VARCHAR
        );"""

song_table_create = create_prefix +  """songs (
        song_id VARCHAR PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        artist_id VARCHAR(255) NOT NULL,
        year INT,
        duration FLOAT
        );"""

artist_table_create = create_prefix +  """artists (
        artist_id VARCHAR(255) PRIMARY KEY, 
        name VARCHAR, 
        location VARCHAR, 
        lattitude VARCHAR, 
        longitude VARCHAR
        );"""

time_table_create = create_prefix + """time (
        start_time BIGINT PRIMARY KEY,
        hour INT,
        day INT,
        week INT,
        month INT,
        year INT,
        weekday INT
        );"""

# INSERT RECORDS

insert_prefix = "INSERT INTO "
insert_sufix = "ON CONFLICT DO NOTHING;" #How to manage conflics on primary keys

songplay_table_insert = insert_prefix + """songplays (
        songplay_id, 
        start_time, 
        user_id, 
        level, 
        song_id, 
        artist_id, 
        session_id, 
        location, 
        user_agent) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """ + insert_sufix

user_table_insert = insert_prefix + """users (
        user_id, 
        first_name, 
        last_name, 
        gender, 
        level) 
        VALUES (%s, %s, %s, %s, %s) """ + insert_sufix

song_table_insert = insert_prefix + """songs (
        song_id, 
        title, 
        artist_id, 
        year, 
        duration) 
        VALUES (%s, %s, %s, %s, %s) """ + insert_sufix

artist_table_insert = insert_prefix + """artists (
        artist_id, 
        name, 
        location, 
        lattitude, 
        longitude) 
        VALUES (%s, %s, %s, %s, %s) """ + insert_sufix

time_table_insert = insert_prefix + """time (
        start_time, 
        hour, 
        day, 
        week, 
        month, 
        year, 
        weekday) 
        VALUES (%s, %s, %s, %s, %s, %s, %s) """ + insert_sufix



# FIND SONGS

song_select = ("""SELECT songs.song_id, artists.artist_id
        FROM songs
        JOIN artists
        ON songs.artist_id = artists.artist_id
        WHERE songs.title = %s AND artists.name=%s AND songs.duration=%s;""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]

drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]


