import os.path, sqlite3
from flask import Flask, render_template

app = Flask(__name__)
working_dir = os.path.dirname(__file__)
db_file = os.path.join(working_dir, 'artist_tracklist.db')

def get_db_conn():
    connection = sqlite3.connect(db_file)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    return cursor


@app.route('/')
@app.route('/home')
def home():
    cursor = get_db_conn()
    cursor.close()
    return render_template('home.html', title='Homepage')


@app.route('/artists')
def artists():
    cursor = get_db_conn()
    cursor.execute('SELECT * FROM artists ORDER BY artist_name ASC')
    artist_names = cursor.fetchall()
    cursor.close()
    return render_template('artists.html', title='Artists List', artist_names=artist_names)
    

@app.route('/tracks')
def tracks():
    cursor = get_db_conn()
    cursor.execute('SELECT * FROM tracklists ORDER BY track_name')
    tracks = cursor.fetchall()
    return render_template('tracks.html', title='Tracks List', tracks = tracks)


@app.route('/artist_details/<id>')
def artist_details(id):
    cursor = get_db_conn()
    cursor.execute('SELECT * FROM tracklists WHERE artist_id = ? ORDER BY track_name', (id,))
    tracks = cursor.fetchall()
    artist = tracks[0][2]
    cursor.execute('SELECT * FROM artists WHERE artist_id = ?', (id,))
    artist_detail = cursor.fetchall()
    cursor.close()
    return render_template('artist_details.html', title=f'{artist} - Artist Details', tracks=tracks, artist_detail=artist_detail)


#"""
if __name__ == '__main__':
    app.run(debug=True)
#"""