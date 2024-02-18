import uvicorn
from fastapi import FastAPI

from database.db import create_tables
from routes.song import routes_song
from pathlib import Path
from mangum import Mangum
from os import getenv

from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.get("/")
def hello_world():
    return {'message': 'Hello from FastAPI!'}
@app.get("/env")
def hello_world():
    return {'message': getenv("AWS_SECRET_ACCESS_KEY")}
app.include_router(routes_song, prefix="/song")
handler = Mangum(app)

create_tables()

if __name__ == "__main__":
    uvicorn.run(f"{Path(__file__).stem}:app", host="0.0.0.0", port=8000, env_file=".env")