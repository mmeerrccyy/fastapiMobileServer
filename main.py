from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware

load_dotenv()

from fastapi import FastAPI
from google.cloud import bigquery

from query_collection import QUERY_ALL_OS, QUERY_AMOUNT_DEVICES_PER_OS

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

@app.get("/all-os")
def get_mobile_phones():
    query_job = bg_client.query(QUERY_ALL_OS)
    results = query_job.result()
    return [dict(row) for row in results]


@app.get("/devices-per-os")
def get_devices_per_os():
    query_job = bg_client.query(QUERY_AMOUNT_DEVICES_PER_OS)
    results = query_job.result()
    return [dict(row) for row in results]

