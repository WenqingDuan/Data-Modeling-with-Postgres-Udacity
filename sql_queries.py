# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS  artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays (
songplay_id INT PRIMARY KEY,
start_time TIMESTAMP NOT NULL,
user_id VARCHAR NOT NULL,
level VARCHAR,
song_id VARCHAR,
artist_id VARCHAR,
session_id INT,
location VARCHAR,
user_agent VARCHAR
)""")

user_table_create = ("""
CREATE TABLE users (
user_id INT NOT NULL PRIMARY KEY,
first_name VARCHAR NOT NULL,
last_name VARCHAR NOT NULL,
gender VARCHAR,
level VARCHAR NOT NULL
)""")

song_table_create = ("""
CREATE TABLE songs (
song_id VARCHAR PRIMARY KEY,
title VARCHAR NOT NULL,
artist_id VARCHAR NOT NULL,
year INT NOT NULL,
duration INT NOT NULL
)""")

artist_table_create = ("""
CREATE TABLE artists (
    artist_id VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    location VARCHAR,
    latitude FLOAT,
    longitude FLOAT
)""")

time_table_create = ("""
CREATE TABLE time (
    start_time TIMESTAMP NOT NULL PRIMARY KEY,
    hour INT NOT NULL,
    day INT NOT NULL,
    week INT NOT NULL,
    month INT NOT NULL,
    year INT NOT NULL,
    weekday INT NOT NULL
)""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplayS (
        songplay_id,
        start_time,
        user_id,
        level,
        song_id,
        artist_id,
        session_id,
        location,
        user_agent
      )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id) DO NOTHING
""")

user_table_insert = ("""
    INSERT INTO users (
        user_id,
        first_name,
        last_name,
        gender,
        level
    )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO NOTHING
""")

song_table_insert = ("""
    INSERT INTO songs (
        song_id,
        title,
        artist_id,
        year,
        duration
    )
    values (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists (
        artist_id,
        name,
        location,
        latitude,
        longitude
    )
    values (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""
    INSERT INTO time (
        start_time,
        hour,
        day,
        week,
        month,
        year,
        weekday
    )
    values (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT 
        songs.song_id AS songid, 
        artists.artist_id AS artistid
    FROM songs 
    INNER JOIN artists ON
        songs.artist_id = artists.artist_id
    WHERE 
        songs.title = %s 
        AND artists.name = %s 
        AND songs.duration = %s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]