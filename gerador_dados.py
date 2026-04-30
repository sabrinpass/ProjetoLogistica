import time
from pathlib import Path
import random

pasta = Path("dock_recebimento")
pasta.mkdir(exist_ok=True)

tipos = ["fragil", "perigoso", "urgente", "normal"]

contador = 1

while True:
    tipo = random.choice(tipos)
    nome = f"pedido_{tipo}_{contador}.txt"

    arquivo = pasta / nome

    with open(arquivo, "w") as f:
        f.write(f"Arquivo de teste {contador} - {tipo}")

    print(f"Gerado: {nome}")

    contador += 1
    time.sleep(3)