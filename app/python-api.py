from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from urllib.request import urlopen
from pydantic import BaseModel
import json

app = FastAPI()

activity_url = "http://www.boredapi.com/api/activity/"
yesno_url = "https://yesno.wtf/api"

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Bored(BaseModel):
    activity_sel: str | None = None
    participants_amount: int | None = None

@app.post("/activity")
async def create_item(bored: Bored):
    if bored.activity_sel:
        activity_urling = activity_url + "?type=" + bored.activity_sel
        if bored.participants_amount and bored.participants_amount > 0:
            activity_urlings = activity_urling + "?participants=" + str(bored.participants_amount)
            response = urlopen(activity_urlings)
            activity_json = json.loads(response.read())
            return {"activity": activity_json.get("activity"), "type": activity_json.get("type"), "part_amount": activity_json.get("participants")}
        else:
            response = urlopen(activity_urling)
            activity_json = json.loads(response.read())
            return {"activity": activity_json.get("activity"), "type": activity_json.get("type"), "part_amount": activity_json.get("participants")}
    if bored.participants_amount and bored.participants_amount > 0:
        activity_urling = activity_url + "?participants=" + str(bored.participants_amount)
        response = urlopen(activity_urling)
        activity_json = json.loads(response.read())
        return {"activity": activity_json.get("activity"), "type": activity_json.get("type"), "part_amount": activity_json.get("participants")}
    else:
        response = urlopen(activity_url)
        activity_json = json.loads(response.read())
        return {"activity": activity_json.get("activity"), "type": activity_json.get("type"), "part_amount": activity_json.get("participants")}

@app.get("/choice")
async def get_random_percentage():
    response = urlopen(yesno_url)
    yesno_json = json.loads(response.read())
    return {"text": yesno_json.get("answer")}

@app.get("/break")
async def get_random_percentage():
    return {"text": "Have a coffee!", "picture": "https://coffee.alexflipnote.dev/HrMCgJMACXc_coffee.png"}

@app.post("/bored/")
async def create_item(bored: Bored):
    if bored.activity_sel:
        activity_urling = activity_url + "?type=" + bored.activity_sel
        return activity_urling
    else:
        return bored
