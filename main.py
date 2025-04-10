from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'msg': 'Proxy API is running'})

@app.route('/kline')
def kline_proxy():
    symbol = request.args.get('symbol')
    interval = request.args.get('interval', '5m')
    limit = request.args.get('limit', 100)

    if not symbol:
        return jsonify({'error': 'Missing symbol parameter'}), 400

    url = f"https://api.mexc.com/api/v1/klines?symbol={symbol}&interval={interval}&limit={limit}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
