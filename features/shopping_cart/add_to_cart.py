import os
from errors.invalid_option import invalid_option
from errors.invalid_quantity import invalid_quantity
from features.shopping_cart.list_products import list_products
from features.shopping_cart.list_products import loads_products_data


def add_to_cart() -> None:
    products_data = loads_products_data()
    print("Agregar al carrito")
    product_code = input("Ingrese código de producto: ")
    if product_code.upper() not in products_data:
        os.system("clear")
        print("ERROR: Código de producto no existe")
        add_to_cart()
    try:
        quantity = int(input("Cantidad: "))
        # FIXME: raise error if quantity is negative
        if quantity <= 0:
            invalid_quantity()
            # FIXME: resume quantity input if invalid input
            add_to_cart()
    except ValueError:
        invalid_option()
        add_to_cart()

    print(f"✅ Producto agregado al carrito.")
