from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# ✅ حل مشكلة الاتصال (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scan")
def scan():
    data = [
        {"symbol": "TSLA", "type": "CALL", "strike": 381, "volume": "60.9K"},
        {"symbol": "AMZN", "type": "PUT", "strike": 251, "volume": "80.8K"},
        {"symbol": "SPXW", "type": "CALL", "strike": 6700, "volume": "9.8K"},
    ]

    random.shuffle(data)
    return data
