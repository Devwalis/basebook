# Investigação de CVEs

## Escopo

Foi analisada a imagem `biblioteca-grupo6:v1`, registrada no primeiro scan do
grupo. O Docker Scout encontrou 0 vulnerabilidades CRITICAL, 7 HIGH, 8 MEDIUM e
27 LOW, totalizando 42 vulnerabilidades em 18 pacotes.

As 15 vulnerabilidades selecionadas estão na planilha
`planilha-vulnerabilidades.csv`: 5 HIGH, 5 MEDIUM e 5 LOW.

## Origem das vulnerabilidades

As vulnerabilidades selecionadas vieram de dois locais:

- componentes e dependências Python presentes na imagem base;
- pacotes Debian presentes na imagem base `python:3.12-slim`.

As vulnerabilidades Python não eram necessárias para executar o BaseBook. Elas
apareciam porque as ferramentas `pip`, `setuptools`, `bandit` e `pip-audit`
estavam sendo colocadas dentro da imagem de produção.

## Correção aplicada

A aplicação usa apenas a biblioteca padrão do Python. Portanto, a imagem final
foi simplificada para não carregar ferramentas de desenvolvimento e auditoria:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN python -m pip uninstall --yes pip setuptools

CMD ["python", "main.py"]
```

Essa alteração removeu `pip`, `setuptools`, `urllib3` e `msgpack` da imagem
final, eliminando as CVEs Python selecionadas sem alterar o código da aplicação.

## Resultado do scan

As 11 vulnerabilidades Python selecionadas não aparecem no scan V2. As quatro
vulnerabilidades LOW selecionadas em `tar`, `glibc`, `coreutils` e `systemd`
permaneceram porque o Docker Scout informa que não há versão corrigida.

Também permaneceram duas HIGH e uma MEDIUM em pacotes Debian que não estavam
entre as 15 selecionadas: `zlib`, `gcc-14` e `tar`.

## Comparação V1 × V2

| Indicador | V1 — antes | V2 — depois |
|---|---:|---:|
| CRITICAL | 0 | 0 |
| HIGH | 7 | 2 |
| MEDIUM | 8 | 1 |
| LOW | 27 | 26 |
| Total de vulnerabilidades | 42 | 29 |
| Pacotes vulneráveis | 18 | 14 |
| Tamanho da imagem | 163 MB | 45,01 MB |
| Imagem base | `python:3.12-slim` | `python:3.12-slim` |
| Aplicação funcionando | Sim | Sim |

## Validação

- Build V1: aprovado.
- Build V2: aprovado.
- Testes automatizados: 6 aprovados com `python3 -m unittest discover -s tests -q`.
- Login administrativo na V2: aprovado.
- Menu de bibliotecário na V2: exibido corretamente.
- Versão do Python na V2: 3.12.15.
- Scan V2: 0 CRITICAL, 2 HIGH, 1 MEDIUM e 26 LOW.

## Evidências

- `scan-v1.txt`: saída completa do scan V1.
- `scan-v2.txt`: saída completa do scan V2 autenticado.
- `imagem-v2.txt`: digest e tamanho da V2.
- `teste-app-v2-login.txt`: login e menu administrativo na V2.
- `teste-app-v2.md`: resumo do teste funcional da V2.
- `recomendacao-v2-resumo.txt`: resumo em português da recomendação da imagem base.
- `planilha-vulnerabilidades.csv`: investigação das 15 vulnerabilidades.
