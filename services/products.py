import json
from typing import Dict, TypedDict


class ProductData(TypedDict):
    name: str
    price: str


def loads_products_data() -> Dict[str, ProductData]:
    with open("data/products_data.json") as file:
        return json.load(file)
