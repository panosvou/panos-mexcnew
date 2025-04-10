from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"msg": "Proxy API is running"})

@app.route('/kline')
def kline():
    symbol = request.args.get('symbol')
    interval = request.args.get('interval', '5m')
    limit = request.args.get('limit', '100')
    if not symbol:
        return jsonify({"error": "Missing symbol"}), 400
    try:
        url = f"https://contract.mexc.com/api/v1/klines?symbol={symbol}&interval={interval}&limit={limit}"
        response = requests.get(url)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
