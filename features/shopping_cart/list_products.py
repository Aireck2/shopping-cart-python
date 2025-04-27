from services.products import loads_products_data
from utils.highlight import highlight


def list_products() -> None:
    products_data = loads_products_data()
    print(highlight("\nLista de productos\n", color="white", bold=True))
    for product in products_data:
        print(
            f"Código: {product} | Producto: {products_data[product]['name']} | Precio: {products_data[product]['price']}")
