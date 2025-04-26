from utils.highlight import highlight


def invalid_quantity() -> None:
    print('\n')
    print(highlight("❌ ERROR: Cantidad no puede ser 0 o negativo", "yellow", True))
    print('\n')
