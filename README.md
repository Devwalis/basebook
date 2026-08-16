# BaseBook — Sistema de Biblioteca

Sistema simples de biblioteca executado pelo terminal, desenvolvido em Python, com
persistência dos dados em arquivo JSON.

## Funcionalidades

- Cadastro de usuários (login, nome, senha e perfil)
- Cadastro de livros (obra com múltiplos exemplares)
- Empréstimo de livros (prazo de 7 dias, renovação, limite de 10 e bloqueio por atraso)
- Devolução de livros (reativa o exemplar e registra o histórico)
- Login por usuário/senha com perfis **leitor** e **bibliotecário**

## Perfis de acesso

| Ação | Leitor | Bibliotecário |
|---|---|---|
| Cadastrar usuário | Não | Sim |
| Cadastrar/remover livro | Não | Sim |
| Emprestar livro | Só para si | Para qualquer usuário |
| Renovar empréstimo | Só os seus | Qualquer |
| Devolver livro | Só os seus | Qualquer |

## Requisitos

- Python 3.12+
- Sem dependências externas (apenas biblioteca padrão)

## Como executar

```bash
python3 main.py
```

Usuário padrão (bibliotecário): `admin` / `admin123`

Os dados são salvos automaticamente em `dados/biblioteca.json`.

## Regras de negócio

- Cada empréstimo dura **7 dias** e pode ser renovado por mais **7 dias**.
- Não é possível emprestar um exemplar que já esteja emprestado.
- Usuário com empréstimo **em atraso** não pode emprestar nem renovar.
- Máximo de **10 empréstimos ativos** por usuário.

## Estrutura do projeto

```
biblioteca/
├── app.py          # menu e fluxos do terminal
├── usuarios.py     # cadastro e autenticação de usuários
├── livros.py       # cadastro e remoção de obras/exemplares
├── emprestimos.py  # empréstimo, renovação e regras
├── devolucoes.py   # devolução de livros
├── models.py       # constantes e regras compartilhadas
└── storage.py      # leitura/escrita do JSON
dados/biblioteca.json
docs/
├── baseline-v1.0.0.md
└── verificacao.md
```

## Documentação

- [Baseline v1.0.0](docs/baseline-v1.0.0.md)
- [Registro de verificação](docs/verificacao.md)

## Versão

Versão atual: **1.0.0** (baseline aprovada, tag `v1.0.0`).