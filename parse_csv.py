import csv
import sqlite3

#creates connection to SQLite Database
connection = sqlite3.connect("artist_tracklist.db")
cursor = connection.cursor()

#prevent duplicates before creating table
cursor.execute('DROP TABLE IF EXISTS artists')
cursor.execute('DROP TABLE IF EXISTS tracklists')
cursor.execute('CREATE TABLE artists (artist_id TEXT, artist_name TEXT, artist_mbid TEXT)')
cursor.execute('CREATE TABLE tracklists (artist_id TEXT, track_id TEXT, artist_name TEXT, track_name TEXT, year INTEGER, FOREIGN KEY (artist_name) REFERENCES artists(artist_name), FOREIGN KEY (artist_id) REFERENCES artists(artist_id))')

#reading from artist csv file
with open('dataset/unique_artists.csv', newline='') as artist_file:
    reader = csv.reader(artist_file, delimiter=",")
    next(reader)                                    #skip header line
    print("Processing artists names")
    for row in reader:
        #print(row)
        artist_id = row[0]
        artist_mbid = row[1]
        track_id = row[2]
        artist_name = row[3]
        cursor.execute('INSERT INTO artists VALUES (?, ?, ?)', (artist_id, artist_name, artist_mbid))
        connection.commit()

with open('dataset/tracks_2009_2010.csv', newline='') as tracks_file:
    reader = csv.reader(tracks_file, delimiter=",")
    next(reader)                                    #skip header line
    print("Processing track names")
    id_list = []
    for row in reader:
        #print(row)
        year = row[0]
        track_id = row[1]
        artist_name = row[2]
        track_name = row[3]  
        #fetch artist_id from artists table
        cursor.execute('SELECT * FROM artists WHERE artist_name = ?', (artist_name,))
        ids = cursor.fetchall()
        #if artist_id for this track cannot be found, skip adding it into the database
        if ids == []:
            continue
        artist_id = ids[0][0]
        id_list.append(artist_id)
        cursor.execute('INSERT INTO tracklists VALUES (?, ?, ?, ?, ?)', (artist_id, track_id, artist_name,track_name, year))
        connection.commit()
    #print(id_list)

with open('dataset/unique_artists.csv', newline='') as artist_file:
    reader = csv.reader(artist_file, delimiter=",")
    next(reader)                                    #skip header line
    print("Deleting artists' names if not found in tracklist")
    for row in reader:
        #print(row)
        artist_id = row[0]
        if artist_id not in id_list:
            #print(row[3])
            cursor.execute('DELETE FROM artists WHERE artist_id = ?', (artist_id,))
            connection.commit()


connection.close()