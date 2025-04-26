from typing import TypedDict


class MenuItem(TypedDict):
    id: int
    label: str


menu_list: list[MenuItem] = [
    {
        "id": 1,
        "label": "1. Ver catálogo"
    },
    {
        "id": 2,
        "label": "2. Agregar producto al carrito",
    },
    {
        "id": 3,
        "label": "3. Eliminar producto del carrito"
    },
    {
        "id": 4,
        "label": "4. Vaciar carrito"
    },
    {
        "id": 5,
        "label": "5. Mostrar carrito"
    },
    {
        "id": 6,
        "label": "6. Finalizar compra"
    },
    {
        "id": 7,
        "label": "7. Salir"
    }
]


def show_menu() -> None:
    for item in menu_list:
        print(item.get("label"))
    print("\n")
