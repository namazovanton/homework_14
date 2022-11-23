import json
import sqlite3


def search_by_title(filmname):
    """Шаг 1"""
    matched_film = {}
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
        SELECT title, country, release_year, listed_in, description 
        FROM netflix 
        WHERE title = '{filmname}'
        OR title LIKE '{filmname}%'
        OR title LIKE '%{filmname}%'
        OR title LIKE '%{filmname}'
        ORDER BY release_year DESC 
        LIMIT 1
        """
        cursor.execute(query)
        matched_film["title"], matched_film["country"], \
        matched_film["release_year"], matched_film["genre"], \
        matched_film["description"] = cursor.fetchone()
        print(matched_film)
    return json.dumps(matched_film)


def search_by_range_of_years(first_year, second_year):
    """Шаг 2"""
    films_list = []
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
        SELECT title, release_year
        FROM netflix 
        WHERE release_year BETWEEN {first_year} AND {second_year}
        OR release_year BETWEEN {second_year} AND {first_year}
        ORDER BY release_year DESC 
        LIMIT 100
        """
        cursor.execute(query)
        for row in cursor.fetchall():
            matched_film = {"title": row[0], "release_year": int(row[1])}
            films_list.append(matched_film)
    return json.dumps(films_list)


def search_by_rating(ratings_tuple):
    """Шаг 3"""
    films_list = []
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
        SELECT title, release_year, description
        FROM netflix
        WHERE rating IN {ratings_tuple}
        ORDER BY release_year DESC
        LIMIT 100
        """
        cursor.execute(query)
        for row in cursor.fetchall():
            print(row)
            matched_film = {"title": row[0], "release_year": int(row[1]), "description": row[2]}
            films_list.append(matched_film)
    return json.dumps(films_list)


def search_by_genre(genre):
    """Шаг 4"""
    films_list = []
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
        SELECT title, description
        FROM netflix
        WHERE listed_in = '{genre}'
        OR listed_in LIKE '{genre}%'
        OR listed_in LIKE '%{genre}%'
        OR listed_in LIKE '%{genre}'
        ORDER BY release_year DESC
        LIMIT 10
        """
        cursor.execute(query)
        for row in cursor.fetchall():
            matched_film = {"title": row[0], "description": row[1]}
            films_list.append(matched_film)
    return json.dumps(films_list)


def search_by_filters(type, year, genre):
    """Шаг 6"""
    films_list = []
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        query = f"""
        SELECT title, description
        FROM netflix
        WHERE "type" = '{type}'
        AND "release_year" = {year}
        AND listed_in = '{genre}'
        OR listed_in LIKE '{genre}%'
        OR listed_in LIKE '%{genre}%'
        OR listed_in LIKE '%{genre}'
        ORDER BY release_year DESC
        LIMIT 10
        """
        cursor.execute(query)
        for row in cursor.fetchall():
            matched_film = {"title": row[0], "description": row[1]}
            films_list.append(matched_film)
    return json.dumps(films_list)
