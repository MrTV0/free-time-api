from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from urllib.request import urlopen
import json

app = FastAPI()

url = "https://yesno.wtf/api"

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/percentage")
async def get_random_percentage():
    return {"title": "https://coffee.alexflipnote.dev/random"}

@app.get("/prin")
async def get_random_percentage():
    response = urlopen(url)

    data_json = json.loads(response.read())

    return {"tell": data_json.get("answer")}

