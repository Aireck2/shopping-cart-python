
import sys
import time

from utils.highlight import highlight


def process_payment() -> None:
    print("\nProcesando pago", end="")
    for _ in range(3):
        time.sleep(0.7)
        print(".", end="")
        sys.stdout.flush()
        time.sleep(0.5)
    print(highlight("\n✅ Pago realizado con éxito 🎉\n"))
