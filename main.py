from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # πολύ σημαντικό!
    allow_credentials=True,
    allow_methods=["*"],  # επιτρέπει OPTIONS και POST
    allow_headers=["*"],
)

class NameRequest(BaseModel):
    name: str

@app.post("/kalimera")
def say_good_morning(data: NameRequest):
    return {"message": f"Καλημέρα {data.name}!"}
