import csv
from datetime import datetime
import os
from typing import Dict

from services.cart import ProductCartData
from utils.extract_price import extract_price

filename = 'purchase_history.csv'
fieldnames = ["datetime", "code", "name",
              "price", "quantity", "subtotal"]


def process_purchase(data: Dict[str, ProductCartData]) -> None:
    purchase = loads_purchase_history()
    merged = data | dict(purchase)
    save_purchase_history(merged)
    print(f"\n✅ Compra registrada con éxito 🎉\n")


def loads_purchase_history() -> Dict[str, ProductCartData]:
    if not os.path.exists(filename):
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
    with open(filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return {row["code"]: row for row in reader}


def save_purchase_history(cart_data: Dict[str, ProductCartData]) -> None:
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for code, item in cart_data.items():
            # Make sure price is a float
            price = float(extract_price(item['price']))
            quantity = int(item['quantity'])  # Make sure quantity is int
            subtotal = price * quantity

            writer.writerow({
                "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "code": code,
                "name": item['name'],
                "price": f"S/{price:.2f}",
                "quantity": quantity,
                "subtotal": f"S/{subtotal:.2f}"
            })
