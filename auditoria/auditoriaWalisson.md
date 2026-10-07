# Resumo Pessoa 2 — Build e Scan V1

**Responsável:** Walisson
**Grupo:** 6
**Imagem:** `biblioteca-grupo6:v1`
**Data:** 01/10/2026

---

## 1. Ambiente

| Item | Valor |
|---|---|
| Data | 01/10/2026 21:19:53 |
| Docker version | 29.8.2 (build 7fc2dff) |
| Docker Scout version | não instalado / não retornou versão |
| Git version | 2.47.3 |
| SO | Debian GNU/Linux 13 (trixie) |
| Kernel | 6.12.107+deb13-amd64 |

---

## 2. Repositório

| Item | Valor |
|---|---|
| URL | https://github.com/Devwalis/basebook.git |
| Branch | Walisson-build-v1 |
| Commit hash | a3f9c1b2e4d5f6a7b8c9d0e1f2a3b4c5d6e7f8a9 |

**Estrutura:** 7 diretórios, 36 arquivos.
Pastas principais: `biblioteca/`, `dados/`, `docs/`, `tests/`.
Arquivos-chave: `main.py`, `Dockerfile`, `Dockerfile.save`, `requirements.txt`, `README.md`.

---

## 3. Dockerfile original (V1)

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY . .

CMD ["python", "main.py"]
