from fastapi import FastAPI
from movies import GetMoviesInstance
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

origins = [
    "http://localhost",
    "http://127.0.0.1:5500/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/{name}')
def home(name: str, l: int = 5):
    prova = GetMoviesInstance(name, limit=l)
    dict = prova.get_sorted_recommendations()
    return dict #list