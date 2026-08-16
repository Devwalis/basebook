PERFIS = ("leitor", "bibliotecario")
DIAS_EMPRESTIMO = 7
DIAS_RENOVACAO = 7
LIMITE_EMPRESTIMOS = 10


def proximo_id(dados, chave):
    return dados["proximos_ids"][chave]


def avancar_id(dados, chave):
    dados["proximos_ids"][chave] += 1