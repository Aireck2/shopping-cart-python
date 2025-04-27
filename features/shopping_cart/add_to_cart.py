import os
from errors.custom_exception import CustomException
from errors.invalid_option import invalid_option
from services.cart import loads_cart_data, save_cart_data
from services.products import loads_products_data
from utils.highlight import highlight


def add_to_cart() -> None:
    products_data = loads_products_data()
    print("Agregar al carrito")
    try:
        product_code = input("Ingrese código de producto: ").upper()

        if product_code not in products_data:
            raise CustomException("ERROR: Código de producto no existe")

        quantity = int(input("Cantidad: "))

        if quantity <= 0:
            raise CustomException("ERROR: Cantidad no puede ser 0 o negativo")

    except ValueError:
        invalid_option()
    except CustomException as e:
        print(highlight(f'\n{e}\n', color="yellow", bold=True))
    else:
        os.system("clear")
        cart_data = loads_cart_data()
        if (cart_data.get(product_code)):
            cart_data[product_code]['quantity'] += quantity
            print("\n✅ Se actualizo la cantidad del producto en el carrito.\n")
        else:
            cart_data[product_code] = {
                "name": products_data[product_code]["name"],
                "price": products_data[product_code]["price"],
                "quantity": quantity
            }
            print("\n✅ Producto agregado al carrito.\n")

        save_cart_data(cart_data)
