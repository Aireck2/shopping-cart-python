
from typing import Iterable
from utils.extract_price import extract_price
from utils.highlight import highlight
from services.cart import ProductCartData, loads_cart_data


def show_cart() -> None:
    cart_data = loads_cart_data()

    print(highlight("\n🛒 Carrito\n", color="white", bold=True))

    if len(cart_data) == 0:
        print(highlight("\n¡El carrito está vacío!\n", color="white"))
        return

    list_cart(items=cart_data.items())


def list_cart(items: Iterable[tuple[str, ProductCartData]]) -> None:
    total = 0.0
    print(highlight("Lista de productos:\n", color="white"))
    for code, item in items:
        quantity = item['quantity']
        price = float(extract_price(item['price']))
        subtotal = quantity * price
        total += subtotal

        print(
            f"- x{quantity} | Código: {code} | Producto: {item['name']} | Precio: {item['price']} | Subtotal: S/.{subtotal:.2f}")

    print(highlight(f"\nTotal a pagar: S/.{total:,.2f}\n", color="white"))
