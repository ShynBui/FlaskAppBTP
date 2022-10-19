import json

from App import app

def read_json(path):
    with open(path, "r") as f:
        return json.load(f)

def load_categories():
    return read_json(app.root_path + "/data/categories.json")

def load_products():
    return read_json(app.root_path + "/data/products.json")