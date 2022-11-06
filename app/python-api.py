from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from urllib.request import urlopen
import json

app = FastAPI()

url = "http://www.boredapi.com/api/activity/"
url2 = "https://yesno.wtf/api"

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/activity")
async def get_random_percentage():
    response = urlopen(url)
    data_json = json.loads(response.read())
    return {"activity": data_json.get("activity")}

@app.get("/break")
async def get_random_percentage():
    return {"text": "Have a coffee!", "picture": "https://coffee.alexflipnote.dev/random"}

