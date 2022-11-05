from fastapi import FastAPI

app = FastAPI()

@app.get("/percentage")
async def get_random_percentage():
    return {'percentage': 'hello world'}
