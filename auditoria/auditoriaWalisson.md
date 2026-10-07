# Relatório — Build e Scan V1

**Responsável:** Walisson
**Grupo:** 6
**Imagem:** `biblioteca-grupo6:v1`
**Data:** 01/10/2026

---

## 1. Ambiente

| Item                | Valor                        |
| ------------------- | ---------------------------- |
| Sistema operacional | Debian GNU/Linux 13 (Trixie) |
| Docker              | 29.8.2                       |
| Docker Scout        | consultar `ambiente-v1.txt`  |
| Git                 | 2.47.3                       |
| Kernel              | 6.12.107+deb13-amd64         |

**Evidência detalhada:** `ambiente-v1.txt`

---

## 2. Repositório

| Item   | Valor                                    |
| ------ | ---------------------------------------- |
| URL    | https://github.com/Devwalis/basebook.git |
| Branch | `feat/auditoria`                         |
| Commit | consultar `repositorio-v1.txt`           |
| Remote | `origin`                                 |

**Evidências:**

* `repositorio-v1.txt`
* `estrutura-v1.txt`

A estrutura contém os diretórios principais `biblioteca/`, `dados/`, `docs/`, `tests/` e os arquivos principais da aplicação.

---

## 3. Dockerfile original

Imagem base utilizada:

```text
python:3.12-slim
```

Dockerfile V1:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY . .

CMD ["python", "main.py"]
```

**Evidência:** `dockerfile-v1.txt`

---

## 4. Build V1

### Comando

```bash
docker build -t biblioteca-grupo6:v1 .
```

### Resultado

Build concluído com sucesso.

Imagem criada:

```text
biblioteca-grupo6:v1
```

Digest gerado durante o build:

```text
sha256:cd17437d459978827af88f07fe36a9e9916af0def878989f441e41fcccced923
```

**Tamanho da imagem:** consultar `imagem-v1.txt`.

**Evidência detalhada:** `build-v1.log`

---

## 5. Teste da aplicação

### Comando

```bash
docker run --rm -it biblioteca-grupo6:v1
```

### Resultado

A aplicação iniciou corretamente dentro do container.

Login administrativo:

```text
admin / admin123
```

Resultado:

```text
Bem-vindo(a), Administrador!
```

O menu administrativo foi apresentado corretamente.

### Funcionalidades

| Funcionalidade       | Resultado               |
| -------------------- | ----------------------- |
| Login administrativo | OK                      |
| Cadastro de usuário  | preencher após teste    |
| Cadastro de livro    | preencher após teste    |
| Listagem de livros   | preencher após teste    |
| Remoção de livro     | não testado / preencher |
| Empréstimo           | não testado / preencher |
| Renovação            | não testado / preencher |
| Devolução            | não testado / preencher |

### Observação

O primeiro teste automatizado utilizando `printf` apresentou `EOFError` devido ao fluxo interativo da aplicação. O teste interativo posterior permitiu autenticação administrativa e acesso ao menu.

**Evidências:**

* `teste-app-v1.log`
* `teste-app-v1.md`

---

## 6. Scan V1

### Comando

```bash
docker scout cves biblioteca-grupo6:v1
```

### Resultado

| Severidade | Quantidade |
| ---------- | ---------: |
| CRITICAL   |          0 |
| HIGH       |          7 |
| MEDIUM     |          8 |
| LOW        |         27 |
| **Total**  |     **42** |

O Scan identificou 42 vulnerabilidades distribuídas em 18 pacotes.

**Imagem base:**

```text
python:3.12-slim
```

### Observações

A imagem não apresentou vulnerabilidades CRITICAL, porém foram identificadas 7 vulnerabilidades HIGH, 8 MEDIUM e 27 LOW.

O Docker Scout também forneceu recomendações de atualização da imagem base.

**Evidências:**

* `scan-v1.txt`
* `scan-v1-resumo.txt`
* `recommendations-v1.txt`

---

## 7. Arquivos de evidência

| Arquivo                  | Conteúdo                          |
| ------------------------ | --------------------------------- |
| `ambiente-v1.txt`        | Versões e informações do ambiente |
| `repositorio-v1.txt`     | Git, branch, remote e commit      |
| `estrutura-v1.txt`       | Estrutura do projeto              |
| `dockerfile-v1.txt`      | Dockerfile original               |
| `build-v1.log`           | Log completo do build             |
| `imagem-v1.txt`          | Informações e tamanho da imagem   |
| `teste-app-v1.log`       | Log do teste da aplicação         |
| `teste-app-v1.md`        | Resumo dos testes funcionais      |
| `scan-v1.txt`            | Scan completo do Docker Scout     |
| `scan-v1-resumo.txt`     | Resumo das vulnerabilidades       |
| `recommendations-v1.txt` | Recomendações do Docker Scout     |
