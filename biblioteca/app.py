from biblioteca import storage, usuarios


def tela_login(dados):
    while True:
        print("\n=== LOGIN ===")
        login = input("Usuário: ").strip()
        senha = input("Senha: ")
        autenticado = usuarios.autenticar(dados, login, senha)
        if autenticado is not None:
            return autenticado
        print("Usuário ou senha inválidos.")


def fluxo_cadastrar_usuario(dados):
    print("\n=== CADASTRAR USUÁRIO ===")
    login = input("Login: ")
    nome = input("Nome completo: ")
    senha = input("Senha: ")
    perfil = input("Perfil (leitor/bibliotecario): ").strip().lower()
    novo, erro = usuarios.cadastrar(dados, login, nome, senha, perfil)
    if erro:
        print(erro)
    else:
        print(f"Usuário '{novo['nome']}' cadastrado (id {novo['id']}, perfil {novo['perfil']}).")


def menu_bibliotecario(dados, usuario_logado):
    print("\n=== SISTEMA DE BIBLIOTECA (BIBLIOTECÁRIO) ===")
    print("1 - Cadastrar usuário")
    print("9 - Sair")
    opcao = input("Opção: ").strip()
    if opcao == "1":
        fluxo_cadastrar_usuario(dados)
    elif opcao == "9":
        return False
    else:
        print("Opção inválida.")
    return True


def menu_leitor(dados, usuario_logado):
    print("\n=== SISTEMA DE BIBLIOTECA (LEITOR) ===")
    print("5 - Sair")
    opcao = input("Opção: ").strip()
    if opcao == "5":
        return False
    print("Opção inválida.")
    return True


def rodar():
    dados = storage.carregar()
    usuario = tela_login(dados)
    print(f"Bem-vindo(a), {usuario['nome']}!")
    continuar = True
    while continuar:
        if usuario["perfil"] == "bibliotecario":
            continuar = menu_bibliotecario(dados, usuario)
        else:
            continuar = menu_leitor(dados, usuario)
    print("Saindo do sistema. Até logo!")