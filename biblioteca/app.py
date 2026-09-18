from biblioteca import devolucoes, emprestimos, livros, storage, usuarios


def tela_login(dados):
    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1 - Usuário ")
        print("2 - Sair")
        op=input("")
        if op=="1":
            print("\n=== LOGIN ===")        
            login = input("Usuário: ").strip()
            senha = input("Senha: ")
            autenticado = usuarios.autenticar(dados, login, senha)
            if autenticado is not None:
                return autenticado
            print("Usuário ou senha inválidos.")
        elif op==2:
            break
        else:
            print("Opção inválida.")


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


def escolher_usuario(dados, usuario_logado):
    if usuario_logado["perfil"] == "leitor":
        return usuario_logado
    termo = input("Login ou id do usuário: ").strip()
    alvo = usuarios.buscar(dados, termo)
    if alvo is None:
        print("Usuário não encontrado.")
        return None
    return alvo


def escolher_emprestimo_ativo(dados, usuario):
    ativos = emprestimos.emprestimos_ativos(dados, usuario["id"])
    if not ativos:
        print("Nenhum empréstimo ativo para esse usuário.")
        return None
    for e in ativos:
        print(formatar_emprestimo(e))
    codigo = input("Id do empréstimo: ").strip()
    for e in ativos:
        if str(e["id"]) == codigo:
            return e
    print("Empréstimo inválido.")
    return None


def formatar_emprestimo(e):
    devolucao = e["data_devolucao"] or "em aberto"
    marca = " [ATRASADO]" if emprestimos.esta_atrasado(e) else ""
    return (
        f"[{e['id']}] usuário {e['usuario_id']} | livro {e['livro_id']} "
        f"exemplar {e['exemplar_id']} | em {e['data_emprestimo']} | "
        f"prevista {e['data_prevista']} | devolução {devolucao} | "
        f"renovações {e['renovacoes']}{marca}"
    )


def exibir_emprestimo(registro):
    print(f"Empréstimo {registro['id']} registrado. Devolução prevista em {registro['data_prevista']}.")


def fluxo_emprestar(dados, usuario_logado):
    print("\n=== EMPRESTAR LIVRO ===")
    alvo = escolher_usuario(dados, usuario_logado)
    if alvo is None:
        return
    obra = escolher_obra(dados)
    if obra is None:
        return
    disponiveis = livros.listar_disponiveis(obra)
    if not disponiveis:
        print("Todos os exemplares desta obra estão emprestados.")
        return
    for ex in disponiveis:
        print(f"Exemplar disponível: {ex['id']}")
    exemplar_id = input("Id do exemplar: ").strip()
    exemplar = next((ex for ex in disponiveis if str(ex["id"]) == exemplar_id), None)
    if exemplar is None:
        print("Exemplar inválido.")
        return
    registro, erro = emprestimos.emprestar(dados, alvo, obra, exemplar)
    if erro:
        print(erro)
    else:
        exibir_emprestimo(registro)


def fluxo_renovar(dados, usuario_logado):
    print("\n=== RENOVAR EMPRÉSTIMO ===")
    alvo = escolher_usuario(dados, usuario_logado)
    if alvo is None:
        return
    emprestimo = escolher_emprestimo_ativo(dados, alvo)
    if emprestimo is None:
        return
    renovado, erro = emprestimos.renovar(dados, emprestimo)
    if erro:
        print(erro)
    else:
        print(
            f"Renovado. Nova devolução prevista em {renovado['data_prevista']} "
            f"(renovações: {renovado['renovacoes']})."
        )


def fluxo_meus_emprestimos(dados, usuario):
    print("\n=== MEUS EMPRÉSTIMOS ===")
    ativos = emprestimos.emprestimos_ativos(dados, usuario["id"])
    if not ativos:
        print("Nenhum empréstimo ativo.")
        return
    for e in ativos:
        print(formatar_emprestimo(e))


def fluxo_todos_emprestimos(dados):
    print("\n=== TODOS OS EMPRÉSTIMOS ===")
    if not dados["emprestimos"]:
        print("Nenhum empréstimo registrado.")
        return
    for e in dados["emprestimos"]:
        print(formatar_emprestimo(e))


def fluxo_devolver(dados, usuario_logado):
    print("\n=== DEVOLVER LIVRO ===")
    alvo = escolher_usuario(dados, usuario_logado)
    if alvo is None:
        return
    emprestimo = escolher_emprestimo_ativo(dados, alvo)
    if emprestimo is None:
        return
    obra = livros.buscar_por_id(dados, emprestimo["livro_id"])
    exemplar = next((ex for ex in obra["exemplares"] if ex["id"] == emprestimo["exemplar_id"]), None)
    devolvido, erro = devolucoes.devolver(dados, emprestimo, obra, exemplar)
    if erro:
        print(erro)
    else:
        print(f"Empréstimo {devolvido['id']} devolvido em {devolvido['data_devolucao']}.")


def menu_bibliotecario(dados, usuario_logado):
    print("\n=== SISTEMA DE BIBLIOTECA (BIBLIOTECÁRIO) ===")
    print("1 - Cadastrar usuário")
    print("2 - Cadastrar livro")
    print("3 - Remover livro")
    print("4 - Listar livros")
    print("5 - Emprestar livro")
    print("6 - Renovar empréstimo")
    print("7 - Devolver livro")
    print("8 - Ver todos os empréstimos")
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
    elif opcao == "5":
        fluxo_emprestar(dados, usuario_logado)
    elif opcao == "6":
        fluxo_renovar(dados, usuario_logado)
    elif opcao == "7":
        fluxo_devolver(dados, usuario_logado)
    elif opcao == "8":
        fluxo_todos_emprestimos(dados)
    elif opcao == "9":
        return False
    else:
        print("Opção inválida.")
    return True


def menu_leitor(dados, usuario_logado):
    print("\n=== SISTEMA DE BIBLIOTECA (LEITOR) ===")
    print("1 - Meus empréstimos")
    print("2 - Emprestar livro")
    print("3 - Renovar empréstimo")
    print("4 - Devolver livro")
    print("5 - Sair")
    opcao = input("Opção: ").strip()
    if opcao == "1":
        fluxo_meus_emprestimos(dados, usuario_logado)
    elif opcao == "2":
        fluxo_emprestar(dados, usuario_logado)
    elif opcao == "3":
        fluxo_renovar(dados, usuario_logado)
    elif opcao == "4":
        fluxo_devolver(dados, usuario_logado)
    elif opcao == "5":
        return False
    else:
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