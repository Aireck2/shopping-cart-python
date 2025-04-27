import os

from errors.custom_exception import CustomException
from services.cart import loads_cart_data, save_cart_data
from utils.highlight import highlight


def remove_from_cart() -> None:
    cart_data = loads_cart_data()
    print("Eliminar del carrito")
    try:
        product_code = input("Ingrese código de producto: ").upper()

        if product_code not in cart_data:
            raise CustomException(
                "ERROR: Código de producto no existe en el carrito")

    except CustomException as e:
        print(highlight(f'\n{e}\n', color="yellow", bold=True))

    else:
        os.system("clear")
        cart_data.pop(product_code)
        save_cart_data(cart_data)
        print(f"\n✅ Producto {product_code} eliminado del carrito.\n")
