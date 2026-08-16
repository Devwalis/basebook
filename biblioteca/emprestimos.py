from datetime import date, timedelta

from biblioteca import models, storage


def emprestimos_ativos(dados, usuario_id):
    return [
        e
        for e in dados["emprestimos"]
        if e["usuario_id"] == usuario_id and e["data_devolucao"] is None
    ]


def esta_atrasado(emprestimo):
    if emprestimo["data_devolucao"] is not None:
        return False
    return emprestimo["data_prevista"] < date.today().isoformat()


def tem_atraso(dados, usuario_id):
    return any(esta_atrasado(e) for e in emprestimos_ativos(dados, usuario_id))


def pode_emprestar(dados, usuario):
    ativos = emprestimos_ativos(dados, usuario["id"])
    if len(ativos) >= models.LIMITE_EMPRESTIMOS:
        return False, f"Usuário atingiu o limite de {models.LIMITE_EMPRESTIMOS} empréstimos."
    if tem_atraso(dados, usuario["id"]):
        return False, "Usuário possui empréstimo em atraso."
    return True, None


def emprestar(dados, usuario, obra, exemplar):
    ok, motivo = pode_emprestar(dados, usuario)
    if not ok:
        return None, motivo
    if not exemplar["disponivel"]:
        return None, "Exemplar já está emprestado."

    hoje = date.today()
    registro = {
        "id": models.proximo_id(dados, "emprestimo"),
        "usuario_id": usuario["id"],
        "livro_id": obra["id"],
        "exemplar_id": exemplar["id"],
        "data_emprestimo": hoje.isoformat(),
        "data_prevista": (hoje + timedelta(days=models.DIAS_EMPRESTIMO)).isoformat(),
        "data_devolucao": None,
        "renovacoes": 0,
    }
    exemplar["disponivel"] = False
    exemplar["emprestado_para"] = usuario["id"]
    dados["emprestimos"].append(registro)
    models.avancar_id(dados, "emprestimo")
    storage.salvar(dados)
    return registro, None


def renovar(dados, emprestimo):
    if emprestimo["data_devolucao"] is not None:
        return None, "Empréstimo já devolvido; não pode ser renovado."
    if esta_atrasado(emprestimo):
        return None, "Empréstimo em atraso; não pode ser renovado."

    nova_prevista = date.fromisoformat(emprestimo["data_prevista"]) + timedelta(
        days=models.DIAS_RENOVACAO
    )
    emprestimo["data_prevista"] = nova_prevista.isoformat()
    emprestimo["renovacoes"] += 1
    storage.salvar(dados)
    return emprestimo, None