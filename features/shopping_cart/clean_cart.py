import os

from services.cart import save_cart_data


def clean_cart() -> None:
    os.system("clear")
    save_cart_data({})
    print(f"\n✅ Todos los productos del carrito han sido eliminados.\n")
