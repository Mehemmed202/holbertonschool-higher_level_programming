#!/usr/bin/python3

from flask import Flask, render_template, request
import json, csv

app = Flask(__name__)

@app.route("/products")
def show_products():
    source = request.args.get("source")  # json və ya csv
    product_id = request.args.get("id")  # opsional
    products = []
    error = None

    if source == "json":
        try:
            with open("products.json", "r") as f:
                products = json.load(f)
        except Exception as e:
            error = "Failed to read JSON file"
    elif source == "csv":
        try:
            with open("products.csv", "r") as f:
                reader = csv.DictReader(f)
                products = [dict(row) for row in reader]
        except Exception as e:
            error = "Failed to read CSV file"
    else:
        error = "Wrong source"

    # id filter
    if product_id and not error:
        product_id = int(product_id)
        filtered = [p for p in products if int(p["id"]) == product_id]
        if filtered:
            products = filtered
        else:
            error = "Product not found"
            products = []

    return render_template("product_display.html", products=products, error=error)

if __name__ == "__main__":
    app.run(debug=True)

