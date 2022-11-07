from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from urllib.request import urlopen
from pydantic import BaseModel
import json

app = FastAPI()

activity_url = "http://www.boredapi.com/api/activity/"
yesno_url = "https://yesno.wtf/api"
#coffee_url = "https://coffee.alexflipnote.dev/random"

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#class Item(BaseModel):
#    name: str
#    description: str | None = None
#    price: float
#    tax: float | None = None

@app.get("/activity")
async def get_activity():
    response = urlopen(activity_url)
    activity_json = json.loads(response.read())
    return {"activity": activity_json.get("activity"), "type": activity_json.get("type")}

@app.get("/break")
async def get_coffee():
    response = urlopen(yesno_url)
    coffee_json = json.loads(response.read())
    return {"text": "Have a coffee!", "picture": yesno_url.get("answer")}

