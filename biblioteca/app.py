from biblioteca import livros, storage, usuarios


def tela_login(dados):
    while True:
        print("\n=== LOGIN ===")
        login = input("Usuário: ").strip()
        senha = input("Senha: ")
        autenticado = usuarios.autenticar(dados, login, senha)
        if autenticado is not None:
            return autenticado
        print("Usuário ou senha inválidos.")


def escolher_obra(dados):
    if not dados["livros"]:
        print("Nenhum livro cadastrado.")
        return None
    titulo = input("Título do livro: ").strip()
    obra = livros.buscar_por_titulo(dados, titulo)
    if obra is None:
        print("Livro não encontrado.")
        return None
    return obra


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


def fluxo_cadastrar_livro(dados):
    print("\n=== CADASTRAR LIVRO ===")
    titulo = input("Título: ")
    quantidade = input("Quantidade de exemplares [1]: ").strip()
    quantidade = int(quantidade) if quantidade else 1
    obra, erro = livros.cadastrar(dados, titulo, quantidade)
    if erro:
        print(erro)
    else:
        print(f"Obra '{obra['titulo']}' registrada com {len(obra['exemplares'])} exemplares.")


def fluxo_remover_livro(dados):
    print("\n=== REMOVER LIVRO ===")
    obra = escolher_obra(dados)
    if obra is None:
        return
    print("1 - Remover obra inteira")
    print("2 - Remover exemplar específico")
    opcao = input("Opção: ").strip()
    if opcao == "1":
        ok, erro = livros.remover_obra(dados, obra)
        print("Obra removida." if ok else erro)
    elif opcao == "2":
        for ex in obra["exemplares"]:
            estado = "Disponível" if ex["disponivel"] else f"Emprestado (usuário {ex['emprestado_para']})"
            print(f"Exemplar {ex['id']}: {estado}")
        exemplar_id = input("Id do exemplar: ").strip()
        ok, erro = livros.remover_exemplar(dados, obra, int(exemplar_id))
        print("Exemplar removido." if ok else erro)
    else:
        print("Opção inválida.")


def fluxo_listar_livros(dados):
    print("\n=== LIVROS CADASTRADOS ===")
    if not dados["livros"]:
        print("Nenhum livro cadastrado.")
        return
    for obra in dados["livros"]:
        print(f"\n[{obra['id']}] {obra['titulo']} ({len(obra['exemplares'])} exemplares)")
        for ex in obra["exemplares"]:
            estado = "Disponível" if ex["disponivel"] else f"Emprestado (usuário {ex['emprestado_para']})"
            print(f"    Exemplar {ex['id']}: {estado}")


def menu_bibliotecario(dados, usuario_logado):
    print("\n=== SISTEMA DE BIBLIOTECA (BIBLIOTECÁRIO) ===")
    print("1 - Cadastrar usuário")
    print("2 - Cadastrar livro")
    print("3 - Remover livro")
    print("4 - Listar livros")
    print("9 - Sair")
    opcao = input("Opção: ").strip()
    if opcao == "1":
        fluxo_cadastrar_usuario(dados)
    elif opcao == "2":
        fluxo_cadastrar_livro(dados)
    elif opcao == "3":
        fluxo_remover_livro(dados)
    elif opcao == "4":
        fluxo_listar_livros(dados)
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