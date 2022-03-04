# LOLlingStone - Music Database WebApp
<h3>Part of Final Project from CS551P Advanced Programming Course UoA</h3>
<a href = "http://lollingstone.herokuapp.com">Link</a> to the live version of the WebApp
<br>
Created by: Christopher Lee (ID: 52105866)

# Why and How the App Got Developed
The app is developed as a way for users to explore the database and discover new artist and music titles that spans from the 20s up until the year 2010. The app is developed in Python with Flask using SQLite3 database. Testing was done by using Behave and Selenium.

# Technical Details
WebApp type: Music database
<br>
Database: SQLite3. Created by using dataset from <a href="http://millionsongdataset.com">Million Song Dataset</a>, which can be found <a href="http://millionsongdataset.com/sites/default/files/AdditionalFiles/unique_artists.txt">here</a> and <a href="http://millionsongdataset.com/sites/default/files/AdditionalFiles/tracks_per_year.txt">here</a>
<br>
Tables: 2 (artists and tracklists. Both tables are linked by the artist_id)
<br>
Total artists in database: 26970 artists
<br>
Total tracklists in database: 476352 tracks
<br>
Number of pages:	5 (Homepage, Artists list, Tracks list, Search page, Artist’s Details page)
<br>
Templates:	artist_details.html, artists.html, home.html, search.html, tracks.html, and layout.html (all HTML files extends to layout.html)
<br>
Testing used: Selenium, Behave (4 test scenarios: home.py, artists.py, tracks.py, search.py)

# Design and Implementation
<h3>Homepage</h3>
<img src="https://user-images.githubusercontent.com/99973434/156806687-e40ea290-2906-4587-8c9b-98afc9a78e7b.png">
I’m feeling lucky button will redirect user into a random artist’s details page. Meanwhile the 
Tracks button will redirect user to a YouTube results page for a random track from the database. Both of these are done by implementing 'random() limit 1' in the SQLite3 query. In the middle of the homepage, statistics regarding the average tracks per artist and the total count of artists and tracks recorded in the database are shown dynamically by querying the totals from the SQLite database.

<h3>Artists Page</h3>
<img src="https://user-images.githubusercontent.com/99973434/156807514-993194e2-8064-4993-b815-292c8edc576f.png">
In the artists page, the entire artists’ names from the database are listed and the names are hyperlinked onto their own artist’s details page. Additionally, the MB links will redirect the user onto the respective artist’s MusicBrainz page. The third column of the table shows each artist’s count of tracks that are available in the database.

<h3>Artist's Details Page</h3>
<img src="https://user-images.githubusercontent.com/99973434/156807086-7364d3e6-f3e1-49d2-a106-75f5c9665d4a.png">
In each artist’s details page, users can view a list of the artist’s tracks that are available in the database. Clicking on the title of the tracks will redirect the user onto the YouTube search result for the artist track’s title. Below the artist’s name, a link to their MusicBrainz page and statistics of the artist are also shown. 

<h3>Tracks Page</h3>
<img src="https://user-images.githubusercontent.com/99973434/156807942-a0fab7d5-72bf-4c55-bb7a-f7dc08b30128.png">
In the tracks page, users can view the tracks that are available in the database by filtering the year they were released and the starting letter of the track title. This was done so that the browser would not load the whole tracklist data onto the page. 
Users can view tracks released in a particular year by selecting the year from the dropdown list and filter the track titles shown by choosing a single or multiple letters. Clicking on the title will redirect the user onto the YouTube search result page for the respective track and clicking on the artist’s name will redirect user onto the artist’s details page.

<h3>Search Page</h3>
<img src="https://user-images.githubusercontent.com/99973434/156808256-162ffc06-96fe-4fed-8a4d-3bec0c3b7f60.png">
Finally, users can also search for an artist or a track title by entering the search query in the search field and to filter the search result by choosing the radio button below the search field.

# Maintenance Details
The database can be expanded by adding the artist name into the unique_artists.csv file and the track name into the tracks_per_year.csv file. Please take note of the format of the respective csv files. 
<br><br>
For unique_artists.csv:
<br>
artist_name has to be unique in order for the tracks to be matched with the artist. This is due to the tracks_per_year.csv file provided by Million Song Dataset which does not contain the artist ID of the artist for each track. artist_id refers to the artist's unique ID in the database, which are then used to link an artist to its details page. artist_mbid refers to a 36 character Universally Unique Identifier from MusicBrainz Identifier that is permanently assigned to each entity in the database.
<br><br>
For tracks_per_year.csv
<br>
Please not that in order for the tracks to be shown on the webapp, each track has to have the year released attribute and the artist_name has to match one of the artist_name from the unique_artist.csv.
<br>br>
After making sure both of the files are in the correct format, you can now run the parse_csv.py script in order to build the artist_tracklist.db database file. The WebApp can then be run locally by typing 'python3 app.py'.
