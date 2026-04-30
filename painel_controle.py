import customtkinter as ctk
import threading
import random
import time
from pathlib import Path
import logiflow_core as logic


# =========================
# GERADOR COM CONTROLE
# =========================
def gerar_dados(flag_pausado, flag_parar):
    pasta = Path("dock_recebimento")
    pasta.mkdir(exist_ok=True)

    tipos = ["fragil", "perigoso", "urgente", "normal"]
    contador = 1

    print("🟢 Gerador iniciado")

    while not flag_parar():
        if flag_pausado():
            time.sleep(1)
            continue

        tipo = random.choice(tipos)
        nome = f"pedido_{tipo}_{contador}.txt"

        arquivo = pasta / nome

        with open(arquivo, "w") as f:
            f.write(f"Arquivo {contador} - {tipo}")

        print(f"[GERADOR] {nome}")

        contador += 1
        time.sleep(2)

    print("🔴 Gerador finalizado")


# =========================
# INTERFACE
# =========================
class AppLogistica(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gateway WMS - Controle Total")
        self.geometry("500x400")

        self.gateway = logic.GatewayLogistico()

        # Controle PROCESSAMENTO
        self.executando = False
        self.pausado = False
        self.parar = False

        # Controle GERADOR
        self.gerando = False
        self.gerador_pausado = False
        self.parar_gerador = False

        # ================= BOTÕES GERADOR =================

        self.btn_gerar_start = ctk.CTkButton(
            self,
            text="INICIAR GERADOR",
            command=self.iniciar_gerador
        )
        self.btn_gerar_start.pack(pady=5)

        self.btn_gerar_pause = ctk.CTkButton(
            self,
            text="PAUSAR GERADOR",
            command=self.pausar_gerador_func,
            state="disabled"
        )
        self.btn_gerar_pause.pack(pady=5)

        self.btn_gerar_stop = ctk.CTkButton(
            self,
            text="PARAR GERADOR",
            command=self.parar_gerador_func,
            state="disabled"
        )
        self.btn_gerar_stop.pack(pady=5)

        # ================= BOTÕES PROCESSAMENTO =================

        self.btn_start = ctk.CTkButton(
            self,
            text="INICIAR PROCESSAMENTO",
            command=self.iniciar
        )
        self.btn_start.pack(pady=10)

        self.btn_pause = ctk.CTkButton(
            self,
            text="PAUSAR PROCESSAMENTO",
            command=self.pausar,
            state="disabled"
        )
        self.btn_pause.pack(pady=5)

        self.btn_stop = ctk.CTkButton(
            self,
            text="PARAR PROCESSAMENTO",
            command=self.parar_sistema,
            state="disabled"
        )
        self.btn_stop.pack(pady=5)

    # ================= GERADOR =================

    def iniciar_gerador(self):
        if not self.gerando:
            self.gerando = True
            self.parar_gerador = False
            self.gerador_pausado = False

            self.thread_gerador = threading.Thread(
                target=gerar_dados,
                args=(lambda: self.gerador_pausado, lambda: self.parar_gerador),
                daemon=True
            )
            self.thread_gerador.start()

            self.btn_gerar_pause.configure(state="normal")
            self.btn_gerar_stop.configure(state="normal")

    def pausar_gerador_func(self):
        self.gerador_pausado = not self.gerador_pausado

        if self.gerador_pausado:
            self.btn_gerar_pause.configure(text="RETOMAR GERADOR")
        else:
            self.btn_gerar_pause.configure(text="PAUSAR GERADOR")

    def parar_gerador_func(self):
        self.parar_gerador = True
        self.gerando = False
        self.gerador_pausado = False

        self.btn_gerar_pause.configure(state="disabled", text="PAUSAR GERADOR")
        self.btn_gerar_stop.configure(state="disabled")

    # ================= PROCESSAMENTO =================

    def iniciar(self):
        if not self.executando:
            self.executando = True
            self.parar = False

            self.thread = threading.Thread(
                target=self.gateway.iniciar_fluxo,
                args=(lambda: self.pausado, lambda: self.parar),
                daemon=True
            )
            self.thread.start()

            self.btn_pause.configure(state="normal")
            self.btn_stop.configure(state="normal")

    def pausar(self):
        self.pausado = not self.pausado

        if self.pausado:
            self.btn_pause.configure(text="RETOMAR PROCESSAMENTO")
        else:
            self.btn_pause.configure(text="PAUSAR PROCESSAMENTO")

    def parar_sistema(self):
        self.parar = True
        self.executando = False
        self.pausado = False

        self.btn_pause.configure(state="disabled", text="PAUSAR PROCESSAMENTO")
        self.btn_stop.configure(state="disabled")


# ================= EXECUÇÃO =================
if __name__ == "__main__":
    app = AppLogistica()
    app.mainloop()