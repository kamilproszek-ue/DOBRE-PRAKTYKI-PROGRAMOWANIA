from fastapi import FastAPI
import csv
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}

# Movie data model
class Movie:
    def __init__(self, movieId, title, genres):
        self.movieId = movieId
        self.title = title
        self.genres = genres

@app.get("/movies")
def get_movies():
    movies = []
    csv_path = os.path.join(os.path.dirname(__file__), "database", "movies.csv")
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movie = Movie(row["movieId"], row["title"], row["genres"])
            movies.append(movie.__dict__)
    return movies