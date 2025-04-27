import re


def extract_price(price_str: str) -> float:
    match = re.search(r'\d+(\.\d+)?', price_str)
    if not match:
        raise ValueError(f"Formato de precio no válido: {price_str}")
    return float(match.group())
