from fastapi import FastAPI

app = FastAPI()
@app.get("/hello")
async def hello():
    return {"message": "Hello back!"}


@app.post("/webhook")
async def accept():
    return {"accepted": 1}