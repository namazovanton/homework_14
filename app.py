from flask import Flask

import functions


app = Flask(__name__)


@app.route("/movie/<title>")
def film_title(title):
    """Шаг 1"""
    matched_film = functions.search_by_title(title)
    return matched_film


@app.route("/movie/<int:year1>/to/<int:year2>")
def films_years(year1, year2):
    """Шаг 2"""
    matched_film = functions.search_by_range_of_years(year1, year2)
    return matched_film


@app.route("/rating/children")
def films_rating_children():
    """Шаг 3"""
    ratings_tuple = ('G', '')
    matched_films = functions.search_by_rating(ratings_tuple)
    return matched_films


@app.route("/rating/family")
def films_rating_family():
    """Шаг 3"""
    ratings_tuple = ('G', 'PG', 'PG-13')
    matched_films = functions.search_by_rating(ratings_tuple)
    return matched_films


@app.route("/rating/adult")
def films_rating_adult():
    """Шаг 3"""
    ratings_tuple = ('R', 'NC-17')
    matched_films = functions.search_by_rating(ratings_tuple)
    return matched_films


@app.route("/genre/<genre>")
def films_genre(genre):
    """Шаг 4"""
    matched_films = functions.search_by_genre(genre)
    return matched_films


app.run()
