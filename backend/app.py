from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf

print("Loading app.py…")

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"status": "Backend is running!"})

@app.route("/price/<ticker>")
def get_price(ticker):
    ticker = ticker.upper()
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")

        if data.empty:
            return jsonify({"error": "Invalid ticker or no data available"}), 404

        price = float(data["Close"].iloc[-1])

        return jsonify({
            "ticker": ticker,
            "price": price
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ⭐⭐⭐ MOVE THE MOMENTUM ROUTE HERE ⭐⭐⭐
@app.route("/momentum/<ticker>")
def momentum(ticker):
    ticker = ticker.upper()
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1mo")  # last 30 days

        if data.empty:
            return jsonify({"error": "Invalid ticker or no data"}), 404

        close_prices = data["Close"]
        latest = close_prices.iloc[-1]

        momentum_7d = latest - close_prices.iloc[-7] if len(close_prices) >= 7 else None
        momentum_30d = latest - close_prices.iloc[0] if len(close_prices) >= 30 else None

        return jsonify({
            "ticker": ticker,
            "latest_price": float(latest),
            "momentum_7d": float(momentum_7d) if momentum_7d is not None else None,
            "momentum_30d": float(momentum_30d) if momentum_30d is not None else None
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ⭐ Keep this LAST ⭐
if __name__ == "__main__":
    print("URL MAP:", app.url_map)
    app.run(debug=True)
