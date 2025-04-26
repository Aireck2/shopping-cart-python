import os
from typing import Callable
from errors.invalid_option import invalid_option
from features.menu import show_menu
from features.shopping_cart.add_to_cart import add_to_cart
from features.shopping_cart.list_products import list_products


def add_and_menu() -> None:
    add_to_cart()
    main()


def list_and_menu() -> None:
    os.system("clear")
    list_products()
    main()


def exit_program() -> None:
    print("\nHasta pronto 👋")
    exit()


def default_action() -> None:
    os.system("clear")
    invalid_option()
    main()


def handle_action(action: int) -> None:
    options: dict[int, Callable[[], None]] = {
        1: list_and_menu,
        2: add_and_menu,
        3: default_action,
        4: default_action,
        5: default_action,
        6: default_action,
        7: exit_program
    }
    options.get(action, default_action)()


def main():
    print("\nBienvenido a la tienda virtual 🛍️\n")
    show_menu()
    try:
        action: int = int(input("¿Qué deseas hacer? (1-7): "))
        handle_action(action)
    except ValueError:
        default_action()


main()
