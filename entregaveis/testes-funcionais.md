# Testes funcionais das imagens V1 e V2

## Funcionalidades verificadas

| Funcionalidade | V1 | V2 |
|---|---|---|
| Cadastro de usuário | OK | OK |
| Busca de livro | OK | OK |
| Cadastro de livro | OK | OK |
| Empréstimo | OK | OK |
| Renovação | OK | OK |
| Devolução | OK | OK |
| Remoção de obra | OK | OK |
| Login administrativo e menu | OK | OK |

## Comandos

Os fluxos de negócio foram executados em containers descartáveis usando os
mesmos testes de asserção nas duas imagens:

```bash
docker run --rm -i biblioteca-grupo6:v1 python -
docker run --rm -i biblioteca-grupo6:v2 python -
```

Os resultados completos estão em:

- `auditoria/teste-funcional-v1.txt`;
- `auditoria/teste-funcional-v2.txt`;
- `auditoria/teste-app-v1-login.txt`;
- `auditoria/teste-app-v2-login.txt`.

Resultado em ambas as imagens:

```text
OK: cadastro, busca, empréstimo, renovação, devolução e remoção
```
