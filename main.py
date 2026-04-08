from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# CORS (مهم)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = "BXosrja5Rfwz9zKUlIgO8VaxdblG_GH9"

@app.get("/scan")
def scan():
    url = f"https://api.polygon.io/v3/reference/options/contracts?limit=50&apiKey={API_KEY}"
    
    res = requests.get(url)
    data = res.json()

    results = []

    for item in data.get("results", []):
        # فلترة بسيطة (Smart Money تقريبي)
        if item.get("strike_price", 0) > 100:
            results.append({
                "symbol": item.get("ticker"),
                "type": item.get("contract_type"),
                "strike": item.get("strike_price"),
                "volume": "🔥"
            })

    return results[:10]
