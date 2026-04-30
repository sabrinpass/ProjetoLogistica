# 🚀 Gateway WMS - Controle Logístico com Interface Gráfica

## 📌 Sobre o Projeto

Este projeto simula um **Gateway de Controle Logístico (WMS)** com interface gráfica, capaz de:

* Gerar dados automaticamente (simulando entrada de cargas)
* Processar arquivos em tempo real
* Classificar automaticamente cargas por tipo
* Organizar arquivos em zonas logísticas
* Controlar execução com botões (iniciar, pausar, parar)

👉 O objetivo é transformar uma automação simples em uma **ferramenta operacional visual**, semelhante a sistemas utilizados na indústria.

---

## 🧠 Arquitetura do Sistema

O projeto é dividido em dois componentes principais:

### 🔹 1. Backend (Cérebro)

Arquivo: `logiflow_core.py`

Responsável por:

* Leitura de arquivos
* Cálculo de hash (SHA-256)
* Classificação de cargas:

  * Fragil → Zona A
  * Perigoso → Zona B
  * Urgente → Zona C
  * Normal → Zona D
* Movimentação de arquivos

---

### 🔹 2. Frontend (Interface)

Arquivo: `painel_controle.py`

Responsável por:

* Interface gráfica (CustomTkinter)
* Controle do sistema via botões
* Execução paralela (threads)
* Gerenciamento de estados (executando, pausado, parado)

---

## ⚙️ Funcionalidades

### 🎮 Controle do Gerador de Dados

* ▶️ Iniciar Gerador
* ⏸️ Pausar Gerador
* ⛔ Parar Gerador

Simula entrada contínua de arquivos no sistema.

---

### ⚙️ Controle de Processamento

* ▶️ Iniciar Processamento
* ⏸️ Pausar Processamento
* ⛔ Parar Processamento

Processa e organiza os arquivos automaticamente.

---

## 📁 Estrutura do Projeto

```
ProjetoLogistica/
│
├── logiflow_core.py
├── painel_controle.py
├── dock_recebimento/
├── armazem_logistico/
└── __pycache__/
```

---

## 📦 Instalação

### 1. Instalar dependência

```bash
pip install customtkinter
```

---

### 2. Executar o sistema

```bash
python painel_controle.py
```

---

## 🧪 Como Usar

1. Execute o sistema
2. Clique em **INICIAR GERADOR**
3. Clique em **INICIAR PROCESSAMENTO**

---

### 🔄 Fluxo esperado

1. Arquivos são criados automaticamente
2. Sistema identifica o tipo
3. Arquivos são movidos para:

```
armazem_logistico/
├── zona_A_fragil
├── zona_B_perigoso
├── zona_C_prioridade
└── zona_D_geral
```

---

## 🧾 Exemplo de arquivos gerados

```
pedido_fragil_1.txt
pedido_perigoso_2.txt
pedido_urgente_3.txt
pedido_normal_4.txt
```

---

## 🧠 Tecnologias utilizadas

* Python 3
* CustomTkinter (GUI)
* Threading (processamento paralelo)
* Pathlib (manipulação de arquivos)
* Hashlib (segurança de dados)

---

## 💡 Conceitos aplicados

* Automação de processos
* Simulação de fluxo logístico
* Controle de concorrência (threads)
* Interface operacional
* Classificação de dados
* Organização de arquivos

---

## 🚀 Possíveis Evoluções

* 📊 Dashboard com métricas em tempo real
* 📈 Integração com Power BI
* 📁 Leitura de arquivos Excel / SAP
* ☁️ Integração com SharePoint
* 🧠 Classificação inteligente (Machine Learning)
* 📦 Transformar em aplicação `.exe`

---

## 🎯 Objetivo Profissional

Este projeto demonstra habilidades em:

* Desenvolvimento de sistemas logísticos
* Automação de processos industriais
* Integração entre backend e frontend
* Manipulação de dados e arquivos
* Criação de interfaces operacionais

---

## 👨‍💻 Autor

Projeto desenvolvido para estudo e aplicação prática em:

* Logística
* Dados
* Automação
* Indústria 4.0

---

## ⭐ Considerações Finais

Este projeto simula um cenário real de operação logística, permitindo:

✔ Testar automações
✔ Simular fluxo de dados
✔ Validar lógica de processamento
✔ Evoluir para soluções reais

---

💥 **Não é apenas um script — é um sistema operacional de logística em miniatura.**
