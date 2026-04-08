from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API_KEY = os.getenv("API_KEY")

# الأسهم الجديدة 🔥
SYMBOLS = ["AAPL", "TSLA", "NVDA", "AMZN", "META", "SPY", "QQQ", "MU"]

@app.get("/scan")
def scan():
    results = []

    for symbol in SYMBOLS:
        url = f"https://api.polygon.io/v2/last/trade/{symbol}?apiKey={API_KEY}"
        
        res = requests.get(url)
        data = res.json()

        trade = data.get("results", {})

        size = trade.get("s", 0)
        price = trade.get("p", 0)

        premium = size * price

        # 🔥 فلتر Smart Money تقريبي
        if size > 100 and premium > 50000:
            results.append({
                "symbol": symbol,
                "type": "BUY" if size > 200 else "TRADE",
                "strike": "-",
                "volume": f"{size}",
                "premium": f"{int(premium)}$ 🔥"
            })

    return sorted(results, key=lambda x: int(x["volume"]), reverse=True)
