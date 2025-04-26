from utils.highlight import highlight


def invalid_option() -> None:
    print(highlight("❌ ERROR: Opción no válida, ingrese un número válido", "yellow", True))
    print("Ejemplo: 1")
