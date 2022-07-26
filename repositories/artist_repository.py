from db.run_sql import run_sql

from models.artist import Artist

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id

def select_all():
    sql = "Select * FROM artists"
    results = run_sql(sql)

    artists = []
    for row in results:
        artist = Artist(row["name"], row["id"])
        artists.append(artist)
    
    return artists

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        result = results[0]
        artist = Artist(result['name'], result['id'])
    return artist