from fastapi import FastAPI
from movies import GetMoviesInstance



app = FastAPI()

@app.get('/{name}')
def home(name: str, l: int = 5):
    prova = GetMoviesInstance(name, limit=l)
    dict = prova.get_sorted_recommendations()
    return dict #list