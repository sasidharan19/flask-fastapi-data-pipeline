from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "customers.json")


def read_customers():
    with open(DATA_PATH, "r") as file:
        return json.load(file)


@app.route("/api/health", methods=["GET"])
def health():
    return {"status": "UP"}


@app.route("/api/customers", methods=["GET"])
def list_customers():
    customers = read_customers()

    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    start = (page - 1) * limit
    end = start + limit

    return jsonify({
        "data": customers[start:end],
        "total": len(customers),
        "page": page,
        "limit": limit
    })


@app.route("/api/customers/<customer_id>", methods=["GET"])
def get_customer(customer_id):
    customers = read_customers()

    for customer in customers:
        if customer["customer_id"] == customer_id:
            return customer

    return {"message": "Customer not found"}, 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
