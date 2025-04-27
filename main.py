import os
from typing import Callable

from errors.invalid_option import invalid_option

from features.menu import show_menu
from features.shopping_cart.checkout import checkout
from features.shopping_cart.clean_cart import clean_cart
from features.shopping_cart.remove_from_cart import remove_from_cart
from features.shopping_cart.show_cart import show_cart
from features.shopping_cart.add_to_cart import add_to_cart
from features.shopping_cart.list_products import list_products

from utils.highlight import highlight


def cart_and_menu() -> None:
    os.system("clear")
    show_cart()


def list_and_menu() -> None:
    os.system("clear")
    list_products()


def exit_program() -> None:
    print("\nHasta pronto 👋")
    exit()


def default_action() -> None:
    os.system("clear")
    invalid_option()


def handle_action(action: int) -> None:
    options: dict[int, Callable[[], None]] = {
        1: list_and_menu,
        2: add_to_cart,
        3: remove_from_cart,
        4: clean_cart,
        5: cart_and_menu,
        6: checkout,
        7: exit_program
    }
    options.get(action, default_action)()


def main():
    while True:
        print(highlight("\nBienvenido a la tienda virtual 🛍️\n",
              color="white", bold=True))
        show_menu()
        try:
            action: int = int(input("¿Qué deseas hacer? (1-7): "))
            handle_action(action)
        except ValueError:
            default_action()
        except KeyboardInterrupt:
            exit_program()


main()
