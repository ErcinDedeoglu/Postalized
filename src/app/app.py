from flask import Flask, request, jsonify
from postal.parser import parse_address
from postal.expand import expand_address

app = Flask(__name__)

@app.route('/parse', methods=['POST'])
def parse():
    address = request.json.get('address')
    parsed = parse_address(address)
    return jsonify(parsed)

@app.route('/expand', methods=['POST'])
def expand():
    address = request.json.get('address')
    expanded = expand_address(address)
    return jsonify(expanded)
