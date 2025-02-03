from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
import math

app = Flask(__name__)
CORS(app)

id_to_receipt = {}

@app.route('/receipts/process', methods=['POST'])
def process_receipts():
    data = request.get_json()
    id = str(uuid.uuid4())
    id_to_receipt[id] = data
    return jsonify({"id": id})

@app.route('/receipts/<id>/points', methods=['GET'])
def get_points(id):             
    receipt = id_to_receipt[id]
    pts = 0
    for c in receipt["retailer"]:
        if c.isalnum():
            pts += 1
    if float(receipt["total"]).is_integer():
        pts += 50
    if float(receipt["total"]) % 0.25 == 0:
        pts += 25
    pts += 5 * (len(receipt["items"]) // 2) 
    for i in receipt["items"]:
        if len(i["shortDescription"].strip()) % 3 == 0:
            pts += math.ceil(float(i["price"]) * 0.2)
    if int(receipt["purchaseDate"][-2:]) % 2 == 1:
        pts += 6
    if 1400 < int(receipt["purchaseTime"][:2] + receipt["purchaseTime"][3:]) < 1600:
        pts += 10
    return jsonify({"points": pts})


if __name__ == '__main__':
    app.run(debug=True, port=8000, host="0.0.0.0")
