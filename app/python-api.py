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
async def get_activity(bored: Bored):
    if bored.activity_sel:
        activity_urling = activity_url + "?type=" + bored.activity_sel
        if bored.participants_amount and bored.participants_amount > 0:
            activity_urlings = activity_urling + "&participants=" + str(bored.participants_amount)
            response = urlopen(activity_urlings)
            activity_json = json.loads(response.read())
            if activity_json.get("activity") == None:
                return {"activity": "No activity found!"}
            else:
                return {"activity": activity_json.get("activity") + "!", "type": activity_json.get("type"), "part_amount": activity_json.get("participants")}
        else:
            response = urlopen(activity_urling)
            activity_json = json.loads(response.read())
            return {"activity": activity_json.get("activity") + "!", "type": activity_json.get("type"), "part_amount": activity_json.get("participants")}
    if bored.participants_amount and bored.participants_amount > 0:
        activity_urling = activity_url + "?participants=" + str(bored.participants_amount)
        response = urlopen(activity_urling)
        activity_json = json.loads(response.read())
        return {"activity": activity_json.get("activity") + "!", "type": activity_json.get("type"), "part_amount": activity_json.get("participants")}
    else:
        response = urlopen(activity_url)
        activity_json = json.loads(response.read())
        return {"activity": activity_json.get("activity") + "!", "type": activity_json.get("type"), "part_amount": activity_json.get("participants")}

@app.get("/choice")
async def get_choice():
    response = urlopen(yesno_url)
    yesno_json = json.loads(response.read())
    return {"text": yesno_json.get("answer")}

@app.get("/yesnos/{amount}")
async def get_yes_no(amount: int, max_amount: int):
    strYesNo = ""
    yes = 0
    no = 0
    if max_amount >= amount and amount > 0:
        if max_amount > 10:
            return {"error": "Please insert a maximum amount of 10 or lower!"}
        for i in range(amount):
            response = urlopen(yesno_url)
            yesno_json = json.loads(response.read())
            yesno = yesno_json.get("answer")
            strYesNo = strYesNo + yesno + " "
            if yesno == "yes":
                yes = yes + 1
            else:
                no = no + 1
        if yes > no:
            return {"fullString": strYesNo, "winner": "Yes wins over no!"}
        elif yes == no:
            return {"fullString": strYesNo, "winner": "It's a tie!"}
        else:
            return {"fullString": strYesNo, "winner": "No wins over yes!"}
    else:
        return {"error": "Please insert a number higher than 0 and lower than " + str(max_amount + 1) + "!"}

@app.get("/break")
async def get_coffee():
    return {"text": "Have a coffee!", "picture": "https://coffee.alexflipnote.dev/HrMCgJMACXc_coffee.png"}
