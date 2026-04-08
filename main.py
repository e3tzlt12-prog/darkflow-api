import requests

API_KEY = "BXosrja5Rfwz9zKUlIgO8VaxdblG_GH9"

@app.get("/scan")
def scan():
    url = f"https://api.polygon.io/v3/trades/options?limit=50&apiKey={API_KEY}"
    
    res = requests.get(url)
    data = res.json()

    results = []

    for trade in data.get("results", []):
        if trade.get("size", 0) > 100:  # فلتر حجم
            results.append({
                "symbol": trade.get("ticker"),
                "type": "CALL/PUT",
                "strike": "?",
                "volume": trade.get("size")
            })

    return results
