from datetime import date

from biblioteca import storage


# Ponto de instrumentação futuro: registro de devoluções.
def devolver(dados, emprestimo, obra, exemplar):
    if emprestimo["data_devolucao"] is not None:
        return None, "Empréstimo já devolvido."

    emprestimo["data_devolucao"] = date.today().isoformat()
    exemplar["disponivel"] = True
    exemplar["emprestado_para"] = None
    storage.salvar(dados)
    return emprestimo, None
