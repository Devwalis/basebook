# Verificação do Sistema — Pré-baseline v1.0.0

Registro da etapa de verificação do estado do sistema antes do estabelecimento da
baseline. Data: 2026-08-16.

## Checklist

| Verificação | Resultado | Observação |
|---|---|---|
| 1. Cadastro de usuários funciona | OK | Login por usuário/senha, perfis leitor e bibliotecário, ids sequenciais, login duplicado rejeitado |
| 2. Cadastro de livros funciona | OK | Obra com múltiplos exemplares, ids sequenciais, remoção de obra/exemplar |
| 3. Empréstimo de livros funciona | OK | Empréstimo por 7 dias, impede livro já emprestado, limite de 10, bloqueio por atraso |
| 4. Devolução de livros funciona | OK | Reativa o exemplar e registra a data de devolução |
| 5. Nenhuma alteração importante sem commit | OK | Working tree limpa |
| 6. Arquivos necessários estão versionados | OK | Código, dados iniciais, documentação e `.gitignore` |
| 7. Não existem arquivos desnecessários no repositório | OK | Apenas arquivos do projeto; `__pycache__` ignorado |
| 8. README corresponde ao funcionamento atual | OK | README documenta funcionalidades, requisitos, execução e credenciais padrão |
| 9. Outra pessoa consegue executar o projeto | OK | Execução documentada com `python3 main.py` e credenciais padrão |
| 10. Testes automatizados do sistema | OK | 6 testes executados com `python3 -m unittest discover -s tests -q` |

## Problemas encontrados e correções

| # | Problema encontrado | Correção realizada |
|---|---|---|
| 1 | README era o template padrão do GitLab, sem informações do projeto | README substituído por documentação do sistema (feito na release) |
| 2 | Sem instruções de execução | Adicionadas instruções de execução e credenciais padrão no README |
| 3 | Empréstimo permitia emprestar exemplar já emprestado na primeira implementação | Corrigido com `fix: impede empréstimo de livro indisponível` |
| 4 | Dados de execução podiam poluir o repositório | Criado `.gitignore` para `__pycache__/` e `*.pyc` |

## Conclusão

Após as correções, o sistema está estável e apto a receber a baseline v1.0.0.

## Atualização — Auditoria Docker da Aula 27

Em 07/10/2026, foi realizada uma auditoria separada das imagens Docker V1 e V2.
Essa atividade não altera o registro histórico da pré-baseline. Os resultados
estão documentados em:

- [Ficha final da auditoria](../entregaveis/relatorio-final.md)

Na V2, a aplicação foi executada com Python 3.12, o login administrativo foi
validado e os 6 testes automatizados permaneceram aprovados.
