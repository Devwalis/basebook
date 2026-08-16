# Baseline v1.0.0 — Sistema de Biblioteca (BaseBook)

## Identificação

| Campo | Valor |
|---|---|
| Nome do sistema | BaseBook — Sistema de Biblioteca |
| Identificação da baseline | `docs/baseline-v1.0.0.md` |
| Versão | 1.0.0 |
| Data | 2026-08-16 |
| Integrantes responsáveis | Gabriel, Jader, Plínio, Wallisson |
| Status | Aprovada |

## Itens de Configuração

Identificação dos Itens de Configuração (ICs) controlados nesta baseline, conforme a
etapa de análise do projeto.

| Nome | Tipo | Estado/versão | Justificativa |
|---|---|---|---|
| Código-fonte do sistema (`biblioteca/`) | Código | 1.0.0 | Núcleo do sistema: regras de usuários, livros, empréstimos e devoluções. Sem ele não há sistema executável. |
| Ponto de entrada (`main.py`) | Código | 1.0.0 | Arquivo que inicia a aplicação no terminal. |
| Dados de persistência (`dados/biblioteca.json`) | Dados | Estado inicial (usuário admin + contadores) | Define o estado inicial controlado do sistema, incluindo o usuário bibliotecário padrão e a sequência de ids. |
| Documentação de configuração (`.gitignore`) | Configuração | 1.0.0 | Controla arquivos que não devem ser versionados, evitando poluição do repositório. |
| README (`README.md`) | Documentação | 1.0.0 | Documenta o funcionamento, requisitos e forma de executar o sistema. |
| Registro de verificação (`docs/verificacao.md`) | Documentação | 1.0.0 | Evidência de que o sistema foi verificado e considerado estável antes da baseline. |
| Documento da baseline (`docs/baseline-v1.0.0.md`) | Documentação | 1.0.0 | Registra o estado aprovado dos ICs, funcionalidades, ambiente e limitações. |
| Ambiente de execução | Ambiente | Python 3.12, Linux | Necessário para reproduzir o comportamento testado do sistema. |
| Repositório Git e branches | Infraestrutura | `main`, `develop`, `feature/*`, `release/1.0.0` | Permite rastrear e reproduzir o histórico de desenvolvimento e a versão aprovada. |
| Tag `v1.0.0` | Infraestrutura | Aponta para o commit aprovado | Referência técnica para localizar exatamente o estado aprovado como versão oficial. |

## Funcionalidades incluídas

1. **Cadastro de usuários** — usuário com login, nome, senha e perfil (leitor ou
   bibliotecário). O bibliotecário cadastra usuários; o leitor não.
2. **Cadastro de livros** — obra com título e múltiplos exemplares, cada um com
   identificador e disponibilidade. Permite remover a obra inteira ou um exemplar
   específico (quando disponível).
3. **Empréstimo de livros** — empresta um exemplar disponível para um usuário
   cadastrado por 7 dias. Impede empréstimo de exemplar já emprestado, de usuário
   com empréstimo em atraso e de usuário com 10 empréstimos ativos. Permite
   renovação de 7 dias para empréstimos não atrasados.
4. **Devolução de livros** — registra a devolução, reativa o exemplar e o torna
   novamente disponível para empréstimo.

Funcionalidades adicionais (decisões da equipe além do mínimo exigido): login por
usuário/senha, perfis de acesso, prazo de 7 dias, renovação, limite de 10
empréstimos, bloqueio por atraso e múltiplos exemplares por obra.

## Ambiente

| Item | Configuração |
|---|---|
| Linguagem | Python 3.12 |
| Sistema operacional testado | Linux |
| Dependências | Nenhuma (apenas biblioteca padrão) |
| Execução | `python3 main.py` a partir da raiz do repositório |
| Usuário padrão | `admin` / `admin123` (perfil bibliotecário) |
| Persistência | Arquivo `dados/biblioteca.json` (JSON), criado e lido automaticamente |

## Limitações conhecidas

- Senhas armazenadas em texto puro (sem hash) — adequado apenas para fins
  educacionais.
- Não há recuperação de senha.
- Renovação sem limite de vezes, desde que o empréstimo não esteja em atraso.
- Os dados não são compartilhados entre múltiplas execuções simultâneas.
- Sem interface gráfica; sistema executado exclusivamente pelo terminal.
- O cadastro de livros não inclui autor, ISBN ou editora (apenas título), conforme
  escopo mínimo da atividade.
- Verificação de atraso baseada na data do sistema operacional.

## Evolução planejada

Melhorias consideradas para versões futuras, **fora do escopo da v1.0.0**:

- **ISBN nos livros** — identificador único por obra para complementar o cadastro
  (a duplicidade já é impedida pelo título; o ISBN é um complemento do registro,
  não uma necessidade desta versão).
- **Data de aquisição por exemplar** — controle patrimonial indicando quando cada
  exemplar entrou no acervo.
- **Segregação admin/bibliotecário** — criar um perfil `admin` com permissões
  ampliadas (remover usuários e livros/exemplares), mantendo o bibliotecário com
  permissão apenas de cadastro e operações de empréstimo/devolução. Na v1.0.0, o
  usuário padrão `admin` é do tipo bibliotecário.
- **Outros metadados de livro** — autor, editora, gênero e ano de publicação.

Essas evoluções deverão ser desenvolvidas em branches de feature próprias
(ex.: `feature/isbn`, `feature/data-aquisicao`) seguindo o Git Flow, e incorporadas
em uma nova baseline (v1.1.0 ou superior).

## Observação

A baseline representa um estado conhecido, controlado e aprovado do sistema — não
necessariamente um sistema perfeito. As limitações acima são aceitas e documentadas
para esta versão.