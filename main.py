from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

from fastapi import FastAPI
from google.cloud import bigquery

from query_collection import QUERY_ALL_TEAMS, QUERY_AMOUNT_DEVICES_PER_OS

app = FastAPI()
bg_client = bigquery.Client()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/all-teams")
def get_mobile_phones():
    query_job = bg_client.query(QUERY_ALL_TEAMS)
    results = query_job.result()
    return [dict(row) for row in results]
