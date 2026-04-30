import shutil
import hashlib
import time
from pathlib import Path


class GatewayLogistico:
    def __init__(self):
        self.base_path = Path.cwd()
        self.dock = self.base_path / "dock_recebimento"
        self.armazem = self.base_path / "armazem_logistico"

        self.dock.mkdir(exist_ok=True)
        self.armazem.mkdir(exist_ok=True)

    def calcular_hash(self, arquivo):
        sha256 = hashlib.sha256()
        with open(arquivo, "rb") as f:
            for bloco in iter(lambda: f.read(4096), b""):
                sha256.update(bloco)
        return sha256.hexdigest()

    def classificar_arquivo(self, nome):
        nome = nome.lower()

        if "fragil" in nome:
            return "zona_A_fragil"
        elif "perigoso" in nome:
            return "zona_B_perigoso"
        elif "urgente" in nome:
            return "zona_C_prioridade"
        else:
            return "zona_D_geral"

    def processar_arquivo(self, arquivo):
        hash_arquivo = self.calcular_hash(arquivo)
        destino_nome = self.classificar_arquivo(arquivo.name)

        destino_pasta = self.armazem / destino_nome
        destino_pasta.mkdir(exist_ok=True)

        destino_final = destino_pasta / arquivo.name
        shutil.move(str(arquivo), str(destino_final))

        print(f"[OK] {arquivo.name} → {destino_nome}")

    def iniciar_fluxo(self, pausado_flag, parar_flag):
        print("🚀 Sistema iniciado...")

        while not parar_flag():
            if pausado_flag():
                time.sleep(1)
                continue

            arquivos = list(self.dock.glob("*"))

            for arquivo in arquivos:
                try:
                    self.processar_arquivo(arquivo)
                except Exception as e:
                    print(f"[ERRO] {arquivo.name}: {e}")

            time.sleep(2)

        print("⛔ Sistema finalizado.")