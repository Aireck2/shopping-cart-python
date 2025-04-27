from utils.highlight import highlight


def invalid_option() -> None:
    print(highlight(
        "\nERROR: Opción no válida, ingrese un número válido. Ejemplo: 1\n", "yellow", True))
