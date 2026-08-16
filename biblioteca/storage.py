import json
import os

CAMINHO_DADOS = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "dados",
    "biblioteca.json",
)


def carregar():
    with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar(dados):
    with open(CAMINHO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)