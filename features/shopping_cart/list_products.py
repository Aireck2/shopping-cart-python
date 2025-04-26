import json
from typing import TypedDict, Dict


class ProductData(TypedDict):
    name: str
    price: str


def loads_products_data() -> Dict[str, ProductData]:
    with open("features/shopping_cart/products_data.json") as file:
        return json.load(file)


def list_products() -> None:
    products_data = loads_products_data()
    print("\nLista de productos")
    print("Código | Nombre | Precio")
    print("-------|--------|-------")
    for product in products_data:
        print(
            f"Código: {product} | Producto: {products_data[product]['name']} | Precio: {products_data[product]['price']}")
