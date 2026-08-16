from biblioteca import models, storage


def cadastrar(dados, titulo, quantidade=1):
    titulo = titulo.strip()
    if not titulo:
        return None, "Título é obrigatório."
    if quantidade < 1:
        return None, "Quantidade deve ser ao menos 1."

    obra = buscar_por_titulo(dados, titulo)
    if obra is None:
        obra = {
            "id": models.proximo_id(dados, "livro"),
            "titulo": titulo,
            "exemplares": [],
        }
        dados["livros"].append(obra)
        models.avancar_id(dados, "livro")

    for _ in range(quantidade):
        obra["exemplares"].append(
            {
                "id": models.proximo_id(dados, "exemplar"),
                "disponivel": True,
                "emprestado_para": None,
            }
        )
        models.avancar_id(dados, "exemplar")

    storage.salvar(dados)
    return obra, None


def buscar_por_titulo(dados, titulo):
    titulo = titulo.strip().lower()
    for obra in dados["livros"]:
        if obra["titulo"].lower() == titulo:
            return obra
    return None


def buscar_por_id(dados, obra_id):
    for obra in dados["livros"]:
        if obra["id"] == obra_id:
            return obra
    return None


def remover_obra(dados, obra):
    if any(not ex["disponivel"] for ex in obra["exemplares"]):
        return False, "Existem exemplares emprestados; não é possível remover a obra."
    dados["livros"].remove(obra)
    storage.salvar(dados)
    return True, None


def remover_exemplar(dados, obra, exemplar_id):
    for exemplar in obra["exemplares"]:
        if exemplar["id"] == exemplar_id:
            if not exemplar["disponivel"]:
                return False, "Exemplar está emprestado; não é possível removê-lo."
            obra["exemplares"].remove(exemplar)
            storage.salvar(dados)
            return True, None
    return False, "Exemplar não encontrado."


def listar_disponiveis(obra):
    return [ex for ex in obra["exemplares"] if ex["disponivel"]]