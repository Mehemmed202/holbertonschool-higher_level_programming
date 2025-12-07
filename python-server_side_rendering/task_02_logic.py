#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/items")
def items():

    with open(items.json, "r") as f:
        data = json.loads(f)
        items = data.get("items", [])

    return render_template(items.html, items=items)


if __name__ == "__main__":
    app.run()
