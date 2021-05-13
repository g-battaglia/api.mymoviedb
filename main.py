from fastapi import FastAPI
from movies import GetMoviesInstance
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()

origins = ["*"]

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
