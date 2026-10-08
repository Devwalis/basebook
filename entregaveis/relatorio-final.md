# Ficha final de auditoria Docker

## 1. Identificação

| Campo | Valor |
|---|---|
| Grupo | 6 |
| Integrantes | Gabriel, Jader, Plínio e Wallisson |
| Sistema | BaseBook — Sistema de Biblioteca |
| Data da auditoria | 07/10/2026 |

## 2. Imagem V1

| Campo | Valor |
|---|---|
| Nome | `biblioteca-grupo6:v1` |
| Imagem base | `python:3.12-slim` |
| Tamanho registrado pelo grupo | 163 MB |
| Usuário | `root` |
| Aplicação funcionando | Sim |

### Scan V1 oficial do grupo

| Severidade | Quantidade |
|---|---:|
| CRITICAL | 0 |
| HIGH | 7 |
| MEDIUM | 8 |
| LOW | 27 |
| Total | 42 |

O scan V1 oficial está em `auditoria/scan-v1.txt` e foi registrado antes das
correções.

## 3. Vulnerabilidades investigadas

| # | CVE/GHSA | Severidade | Corrigida? | Como foi corrigida |
|---:|---|---|---|---|
| 1 | CVE-2026-97689 | HIGH | Sim | Remoção da dependência Python desnecessária |
| 2 | CVE-2026-97687 | HIGH | Sim | Remoção da dependência Python desnecessária |
| 3 | GHSA-6v7p-g79w-8964 | HIGH | Sim | Remoção da dependência Python desnecessária |
| 4 | CVE-2026-57585 | HIGH | Sim | Remoção da dependência Python desnecessária |
| 5 | CVE-2025-47273 | HIGH | Sim | Remoção do componente Python da imagem final |
| 6 | CVE-2026-97688 | MEDIUM | Sim | Remoção da dependência Python desnecessária |
| 7 | CVE-2026-59890 | MEDIUM | Sim | Remoção do componente Python da imagem final |
| 8 | CVE-2025-8869 | MEDIUM | Sim | Remoção do `pip` da imagem final |
| 9 | CVE-2026-13346 | MEDIUM | Sim | Remoção do `pip` da imagem final |
| 10 | CVE-2026-6357 | MEDIUM | Sim | Remoção do `pip` da imagem final |
| 11 | CVE-2026-1703 | LOW | Sim | Remoção do `pip` da imagem final |
| 12 | CVE-2005-2541 | LOW | Não | Docker Scout não informa versão corrigida |
| 13 | CVE-2019-9192 | LOW | Não | Docker Scout não informa versão corrigida |
| 14 | CVE-2026-56392 | LOW | Não | Docker Scout não informa versão corrigida |
| 15 | CVE-2023-31439 | LOW | Não | Docker Scout não informa versão corrigida |

O detalhamento por pacote, versão, origem e fonte está em
`entregaveis/planilha-vulnerabilidades.csv`.

## 4. Correções realizadas

- Alteração da imagem base para `python:3.12-slim`.
- Remoção de `pip` e `setuptools` da imagem final.
- Remoção de ferramentas de auditoria que não são necessárias em runtime.
- Criação do `.dockerignore` para evitar cópia de testes, documentação,
  auditoria, repositório Git e arquivos de desenvolvimento para a imagem.

Dockerfile final:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN python -m pip uninstall --yes pip setuptools

CMD ["python", "main.py"]
```

## 5. Imagem V2

| Campo | Valor |
|---|---|
| Nome | `biblioteca-grupo6:v2` |
| Imagem base | `python:3.12-slim` |
| Tamanho | 45,01 MB |
| Usuário | `root` |
| Aplicação funcionando | Sim |

### Scan V2

| Severidade | Quantidade |
|---|---:|
| CRITICAL | 0 |
| HIGH | 2 |
| MEDIUM | 1 |
| LOW | 26 |
| Total | 29 |

## 6. Comparação V1 × V2

| Indicador | V1 — antes | V2 — depois |
|---|---:|---:|
| CRITICAL | 0 | 0 |
| HIGH | 7 | 2 |
| MEDIUM | 8 | 1 |
| LOW | 27 | 26 |
| Total | 42 | 29 |
| Tamanho | 163 MB | 45,01 MB |
| Usuário | `root` | `root` |
| Aplicação funcionando | Sim | Sim |

### Observação sobre o `docker scout compare`

O comando foi executado e está registrado em `auditoria/compare-v1-v2.md`.
O compare local usa uma reconstrução da V1 com o contexto atualmente disponível
e encontrou 2 HIGH, 6 MEDIUM e 27 LOW. O scan oficial V1 do grupo encontrou 7
HIGH, 8 MEDIUM e 27 LOW porque foi produzido anteriormente com outro contexto
de build. Para a ficha da atividade, a comparação principal usa o scan V1
oficial registrado pelo grupo e o scan V2 final.

## 7. Teste de funcionamento

Os principais fluxos foram executados nas duas imagens:

- cadastro de usuário;
- cadastro e busca de livro;
- empréstimo;
- renovação;
- devolução;
- remoção de obra;
- login administrativo e menu de bibliotecário.

Os resultados estão em `testes-funcionais.md`.

## 8. Conclusão

1. A principal origem foi a presença de componentes Python desnecessários e de
   pacotes Debian herdados da imagem base.
2. Das 15 vulnerabilidades escolhidas, 11 foram corrigidas.
3. Quatro permaneceram.
4. Elas permaneceram porque o Docker Scout não informa uma versão corrigida para
   os pacotes Debian correspondentes.
5. A aplicação continuou funcionando nas versões V1 e V2.
6. A V2 removeu ferramentas que não eram necessárias em runtime, reduziu a
   imagem de 163 MB para 45,01 MB e reduziu o total oficial de vulnerabilidades
   de 42 para 29.

## 9. Evidências

- `auditoria/scan-v1.txt`;
- `auditoria/scan-v2.txt`;
- `auditoria/compare-v1-v2.md`;
- `auditoria/scan-v1-reproduzido.txt`;
- `auditoria/imagem-v1-reproduzida.txt`;
- `auditoria/imagem-v1.txt`;
- `auditoria/imagem-v2.txt`;
- `auditoria/teste-funcional-v1.txt`;
- `auditoria/teste-funcional-v2.txt`;
- `auditoria/teste-app-v1-login.txt`;
- `auditoria/teste-app-v2-login.txt`;
- `entregaveis/planilha-vulnerabilidades.csv`;
- `entregaveis/testes-funcionais.md`.
