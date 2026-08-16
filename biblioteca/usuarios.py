from biblioteca import models, storage


def cadastrar(dados, login, nome, senha, perfil):
    login = login.strip().lower()
    nome = nome.strip()
    if not login or not nome or not senha:
        return None, "Usuário, nome e senha são obrigatórios."
    if perfil not in models.PERFIS:
        return None, "Perfil inválido. Use 'leitor' ou 'bibliotecario'."
    if any(u["usuario"] == login for u in dados["usuarios"]):
        return None, "Já existe um usuário com esse login."

    usuario = {
        "id": models.proximo_id(dados, "usuario"),
        "usuario": login,
        "nome": nome,
        "senha": senha,
        "perfil": perfil,
    }
    dados["usuarios"].append(usuario)
    models.avancar_id(dados, "usuario")
    storage.salvar(dados)
    return usuario, None


def autenticar(dados, login, senha):
    login = login.strip().lower()
    for usuario in dados["usuarios"]:
        if usuario["usuario"] == login and usuario["senha"] == senha:
            return usuario
    return None


def buscar(dados, termo):
    termo = termo.strip().lower()
    for usuario in dados["usuarios"]:
        if usuario["usuario"] == termo or str(usuario["id"]) == termo:
            return usuario
    return None