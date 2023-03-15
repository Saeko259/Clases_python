from fastapi import FastAPI
from dotenv  import load_dotenv
import os

load_dotenv()
TITLE = os.getenv("TITLE")
VERSION = os.getenv("VERSION")
app = FastAPI(
    title=TITLE,
    version=VERSION
)

@app.get("/")
def hello_world():
    {
        "title":TITLE,
        "version":VERSION
    }
    return 'hello world'

