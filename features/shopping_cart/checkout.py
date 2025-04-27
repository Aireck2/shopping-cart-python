from errors.custom_exception import CustomException
from features.shopping_cart.show_cart import list_cart
from services.cart import loads_cart_data, save_cart_data
from services.checkout import process_payment
from services.purchase import process_purchase
from utils.highlight import highlight


def checkout() -> None:
    cart_data = loads_cart_data()
    try:
        if len(cart_data) == 0:
            raise CustomException(
                "Finalizar compra: No hay productos en el carrito")

        print(highlight("\nFinalizar compra\n", color="white", bold=True))
        print(highlight("Resumen de compra:\n", color="white"))
        list_cart(items=cart_data.items())

        response = input(
            "¿Deseas finalizar la compra? (S/N): ").strip().lower()
        if response == "s":
            process_payment()
            process_purchase(data=cart_data)
            save_cart_data({})

        elif response == "n":
            raise CustomException("¡No has finalizado la compra!")
        else:
            raise CustomException("Finalizar compra: Opción no válida")
    except CustomException as e:
        print(highlight(f'\n{e}\n', color="yellow", bold=True))
