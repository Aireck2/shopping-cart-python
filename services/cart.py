import json
from typing import Dict

from services.products import ProductData


class ProductCartData(ProductData):
    quantity: int


def loads_cart_data() -> Dict[str, ProductCartData]:
    with open("data/cart_data.json") as file:
        return json.load(file)


def save_cart_data(cart_data: Dict[str, ProductCartData]) -> None:
    with open("data/cart_data.json", "w") as file:
        json.dump(cart_data, file)
