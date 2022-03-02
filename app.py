import os.path, sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)
working_dir = os.path.dirname(__file__)
db_file = os.path.join(working_dir, 'artist_tracklist.db')

def get_db_conn():
    connection = sqlite3.connect(db_file)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    return cursor


@app.route('/')
def home():
    cursor = get_db_conn()
    cursor.close()
    return render_template('home.html', title='Homepage')


@app.route('/artists')
def artists():
    cursor = get_db_conn()
    cursor.execute('SELECT * FROM artists ORDER BY artist_name ASC')
    artist_names = cursor.fetchall()
    cursor.execute('SELECT * FROM tracklists ORDER BY artist_name ASC')
    tracks = cursor.fetchall()
    artlist = {}
    #calculating number of tracks released by an artist
    for row in tracks:
        if row[2] not in artlist:
            artlist[row[2]] = 1
        else:
            artlist[row[2]] += 1
    cursor.close()
    return render_template('artists.html', title='Artists List', artist_names=artist_names, artlist=artlist)
    

@app.route('/tracks', methods = ["GET", "POST"])
def tracks():
    tracks = None
    year = None
    letter = ""
    filters = None
    sum = None
    cursor = get_db_conn()
    if request.method == "POST":
        year = request.form["year"]
        letter = request.form.getlist("letter")
        
        if letter != []:
            #to filter track titles starting with numbers
            if "number" in letter:
                letter.remove("number")
                for i in range(10):
                    letter.append(str(i))
            #assemble syntax through python (hopefully safe because no outside input except for predefined value)
            syntax = f'SELECT * FROM tracklists WHERE track_name LIKE "{letter[0]}%" '
            for i in letter[1:]:   
                syntax += f'OR track_name LIKE "{i}%" '
            syntax += 'AND year = ? ORDER BY track_name'
            cursor.execute(syntax, (year,))
        else:
            cursor.execute('SELECT * FROM tracklists WHERE year = ? ORDER BY track_name', (year,))
    #description text for enabled filters on search box 
    if letter != []:
        filters = (",").join(letter)
    tracks = cursor.fetchall()
    cursor.close()
    return render_template('tracks.html', title='Tracklist', filters=filters, letter=letter, tracks=tracks, year=year, sum=sum)

@app.route('/search', methods = ["GET", "POST"])
def search():
    cursor = get_db_conn()
    search_type = None
    query = ""
    artists = None
    tracks = None
    statement = ""

    if request.method == "POST":
        search_type = request.form["search_type"]
        query_escaped = "%" + request.form["query"] + "%"
        query = request.form["query"]
   
        if search_type == "track":
            cursor.execute("SELECT * FROM tracklists WHERE track_name LIKE ?", (query_escaped,))
            tracks = cursor.fetchall()
            #print error statement if query not found
            if len(tracks) == 0:
                statement = f'"{query}" not found'
        elif search_type == "artist":
            cursor.execute("SELECT * FROM artists WHERE artist_name LIKE ?", (query_escaped,))
            artists = cursor.fetchall()
            #print error statement if query not found
            if len(artists) == 0:
                statement = f'"{query}" not found'

    cursor.close()
    return render_template('search.html', title='Search', query=query, search_type=search_type, artists=artists, tracks=tracks, statement=statement)

@app.route('/artist_details/<id>')
def artist_details(id):
    cursor = get_db_conn()
    cursor.execute('SELECT * FROM tracklists WHERE artist_id = ? ORDER BY track_name', (id,))
    tracks = cursor.fetchall()
    artist = tracks[0][2]
    song_count = len(tracks)
    cursor.execute('SELECT * FROM artists WHERE artist_id = ?', (id,))
    artist_detail = cursor.fetchall()
    cursor.close()
    return render_template('artist_details.html', title=f'{artist} - Artist Details', tracks=tracks, song_count=song_count, artist_detail=artist_detail)


if __name__ == '__main__':
    app.run(debug=True)