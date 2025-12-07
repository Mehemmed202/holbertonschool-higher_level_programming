#!/usr/bin/python3

from flask import Flask, render_template, request
import json, csv, sqlite3

app = Flask(__name__)

def get_products_from_sqlite(product_id=None):
    try:
        conn = sqlite3.connect("products.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        if product_id:
            cursor.execute("SELECT * FROM Products WHERE id = ?", (product_id,))
        else:
            cursor.execute("SELECT * FROM Products")
        rows = cursor.fetchall()
        products = [dict(row) for row in rows]
        conn.close()
        return products, None
    except Exception as e:
        return [], "Database error: " + str(e)

@app.route("/products")
def show_products():
    source = request.args.get("source")  # json, csv, sql
    product_id = request.args.get("id")  # opsional
    products = []
    error = None

    try:
        if product_id:
            product_id_int = int(product_id)
        else:
            product_id_int = None
    except ValueError:
        error = "Invalid id"
        product_id_int = None

    if not error:
        if source == "json":
            try:
                with open("products.json", "r") as f:
                    products = json.load(f)
                if product_id_int:
                    filtered = [p for p in products if p["id"] == product_id_int]
                    if filtered:
                        products = filtered
                    else:
                        error = "Product not found"
                        products = []
            except Exception as e:
                error = "Failed to read JSON file"

        elif source == "csv":
            try:
                with open("products.csv", "r") as f:
                    reader = csv.DictReader(f)
                    products = [dict(row) for row in reader]
                    for p in products:
                        p["id"] = int(p["id"])
                        p["price"] = float(p["price"])
                if product_id_int:
                    filtered = [p for p in products if p["id"] == product_id_int]
                    if filtered:
                        products = filtered
                    else:
                        error = "Product not found"
                        products = []
            except Exception as e:
                error = "Failed to read CSV file"

        elif source == "sql":
            products, db_error = get_products_from_sqlite(product_id_int)
            if db_error:
                error = db_error
            elif product_id_int and not products:
                error = "Product not found"

        else:
            error = "Wrong source"

    return render_template("product_display.html", products=products, error=error)

if __name__ == "__main__":
    app.run(debug=True)

