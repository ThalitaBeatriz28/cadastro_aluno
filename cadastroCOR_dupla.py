from colorama import Fore, Style, init

# Inicializa a biblioteca Colorama para suporte a cores no terminal
init()

# ============================================================
# CONFIGURAÇÕES VISUAIS DA TABELA E DO MENU
# Define as dimensões do menu e o alinhamento das colunas
# ============================================================
LARGURA = 44
COL_NOME = 20
COL_NOTA = 8
COL_ESTADO = 11


# ------------------------------------------------------------
# EXIBIÇÃO DO MENU PRINCIPAL
# Desenha a moldura do menu usando caracteres Unicode
# ------------------------------------------------------------
def exibir_menu():
    print(Fore.CYAN + "╔" + "═" * LARGURA + "╗")
    print(Fore.CYAN + "║" + Style.BRIGHT + Fore.WHITE + "SISTEMA DE CADASTRO DE ALUNOS".center(LARGURA) + Style.RESET_ALL + Fore.CYAN + "║")
    print(Fore.CYAN + "╠" + "═" * LARGURA + "╣")
    print(Fore.CYAN + "║" + Fore.BLUE + "  1 - Cadastrar aluno".ljust(LARGURA) + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.BLUE + "  2 - Listar alunos".ljust(LARGURA) + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.BLUE + "  3 - Alterar aluno".ljust(LARGURA) + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.BLUE + "  4 - Excluir aluno".ljust(LARGURA) + Fore.CYAN + "║")
    print(Fore.CYAN + "║" + Fore.RED + "  0 - Sair".ljust(LARGURA) + Fore.CYAN + "║")
    print(Fore.CYAN + "╚" + "═" * LARGURA + "╝" + Style.RESET_ALL)


# ------------------------------------------------------------
# FLUXO E NAVEGAÇÃO DO SISTEMA
# Garante a criação inicial do arquivo e lida com o menu principal
# ------------------------------------------------------------
def menu():
    # Cria o arquivo .txt em modo exclusivo caso ele ainda não exista
    try:
        with open("dados_alunos.txt", "x", encoding="utf-8") as arquivo:
            pass
    except FileExistsError:
        pass

    # Loop de execução que mantém o programa ativo até a opção 0
    while True:
        try:
            exibir_menu()
            escolha = int(input(Fore.WHITE + "Escolha uma opção: " + Style.RESET_ALL))
            if escolha == 1:
                cadastro()
            elif escolha == 2:
                mostrar()
            elif escolha == 3:
                alterar()
            elif escolha == 4:
                excluir()
            elif escolha == 0:
                print(Fore.CYAN + "\n 🖑 Sistema encerrado. Até logo! 🖑 " + Style.RESET_ALL)
                break
            else:
                print(Fore.YELLOW + "✘ Digite apenas opções válidas!\n" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "✘ Digite apenas opções válidas!\n" + Style.RESET_ALL)


# ------------------------------------------------------------
# CADASTRO DE ALUNOS
# Valida as entradas do usuário em laços contínuos e grava no .txt
# ------------------------------------------------------------
def cadastro():
    print(Fore.CYAN + Style.BRIGHT + "\n===== CADASTRAR ALUNO =====" + Style.RESET_ALL)
    
    # Validação do nome
    while True:
        nome = input(Fore.WHITE + "Digite o nome do aluno: " + Style.RESET_ALL).strip().title()
        if nome == "":
            print(Fore.RED + "✘ O nome não pode ficar vazio!" + Style.RESET_ALL)
            continue
        
        # Remove espaços temporariamente para validar se contém apenas letras
        if not nome.replace(" ", "").isalpha():
            print(Fore.RED + "✘ Digite apenas letras, sem números ou símbolos!" + Style.RESET_ALL)
        else:
            break
        
    # Validação da nota
    while True:
        try:
            nota = float(input(Fore.WHITE + "Digite a nota do aluno: " + Style.RESET_ALL).strip().replace(",", "."))
            if nota < 0 or nota > 10:
                print(Fore.RED + "✘ Digite uma nota válida (0 a 10)!" + Style.RESET_ALL)
            else:
                break
        except ValueError:
            print(Fore.RED + "✘ Digite apenas números!\n" + Style.RESET_ALL)

    # Grava no arquivo apenas o nome formatado e a nota
    with open("dados_alunos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome.title()};{nota:.2f}\n")

    print(Fore.GREEN + "✔ Aluno cadastrado com sucesso!\n" + Style.RESET_ALL)


# ------------------------------------------------------------
# LISTAGEM E ESTATÍSTICAS
# Lê os dados do arquivo, calcula dinamicamente o estado (situação)
# e renderiza a tabela formatada com o resumo da turma
# ------------------------------------------------------------
def mostrar():
    print(Fore.CYAN + Style.BRIGHT + "\n===== ALUNOS CADASTRADOS =====" + Style.RESET_ALL)

    try:
        with open("dados_alunos.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.readlines()
    except FileNotFoundError:
        print(Fore.YELLOW + "⚠ Nenhum aluno cadastrado ainda!\n" + Style.RESET_ALL)
        return

    if not conteudo:
        print(Fore.YELLOW + "⚠ Nenhum aluno cadastrado ainda!\n" + Style.RESET_ALL)
        return

    # Bordas divisórias da tabela
    topo = "╔" + "═" * (COL_NOME + 2) + "╦" + "═" * (COL_NOTA + 2) + "╦" + "═" * (COL_ESTADO + 2) + "╗"
    meio = "╠" + "═" * (COL_NOME + 2) + "╬" + "═" * (COL_NOTA + 2) + "╬" + "═" * (COL_ESTADO + 2) + "╣"
    fim = "╚" + "═" * (COL_NOME + 2) + "╩" + "═" * (COL_NOTA + 2) + "╩" + "═" * (COL_ESTADO + 2) + "╝"

    print(Fore.CYAN + topo)
    print(Fore.CYAN + "║ " + Style.BRIGHT + Fore.WHITE + "NOME".ljust(COL_NOME) + Style.RESET_ALL +
          Fore.CYAN + " ║ " + Style.BRIGHT + Fore.WHITE + "NOTA".center(COL_NOTA) + Style.RESET_ALL +
          Fore.CYAN + " ║ " + Style.BRIGHT + Fore.WHITE + "ESTADO".center(COL_ESTADO) + Style.RESET_ALL + Fore.CYAN + " ║")
    print(Fore.CYAN + meio)

    aprovados = 0
    reprovados = 0
    maior_nome = ""
    maior_nota = -1
    menor_nome = ""
    menor_nota = 11
    total_validos = 0

    try:
        for linha in conteudo:
            linha = linha.strip()
            if not linha:
                continue
            partes = linha.split(";")
            nome = partes[0].strip().title()
            nota = float(partes[1].strip())
            total_validos += 1
            
            estado = "Aprovado" if nota >= 6 else "Reprovado"

            if estado == "Aprovado":
                cor = Fore.GREEN
                aprovados += 1
            else:
                cor = Fore.RED
                reprovados += 1

            if nota > maior_nota:
                maior_nota = nota
                maior_nome = nome
            if nota < menor_nota:
                menor_nota = nota
                menor_nome = nome

            print(Fore.CYAN + "║ " + Style.RESET_ALL + Fore.WHITE + nome.title().ljust(COL_NOME) +
                  Fore.CYAN + " ║ " + Style.RESET_ALL + f"{nota:.2f}".center(COL_NOTA) +
                  Fore.CYAN + " ║ " + cor + estado.center(COL_ESTADO) + Style.RESET_ALL + Fore.CYAN + " ║")

        print(Fore.CYAN + fim + Style.RESET_ALL)

        print(Fore.MAGENTA + f"\nTotal de alunos: {total_validos}")
        print(Fore.GREEN + f"Aprovados: {aprovados}")
        print(Fore.RED + f"Reprovados: {reprovados}")
        print(Fore.YELLOW + f"★ Maior nota: {maior_nome.title()} ({maior_nota:.2f})")
        print(Fore.YELLOW + f"★ Menor nota: {menor_nome.title()} ({menor_nota:.2f})\n" + Style.RESET_ALL)
    except Exception:
        print(Fore.RED + "✘ Erro na listagem!" + Style.RESET_ALL)


# ------------------------------------------------------------
# ALTERAÇÃO DE DADOS
# Busca contínua do aluno e atualização do NOME e da NOTA no arquivo
# ------------------------------------------------------------
def alterar():
    print(Fore.MAGENTA + Style.BRIGHT + "\n===== ALTERAR ALUNO =====" + Style.RESET_ALL)

    try:
        with open("dados_alunos.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.readlines()
    except FileNotFoundError:
        print(Fore.YELLOW + "⚠ Nenhum aluno cadastrado ainda!\n" + Style.RESET_ALL)
        return

    if not conteudo:
        print(Fore.YELLOW + "⚠ Nenhum aluno cadastrado ainda!\n" + Style.RESET_ALL)
        return

    while True:
        nome_aluno = input(Fore.WHITE + "Digite o nome do aluno que deseja alterar: " + Style.RESET_ALL).strip()
        
        if not (nome_aluno and nome_aluno.replace(" ", "").isalpha()):
            print(Fore.RED + "✘ Digite um nome válido apenas com letras!\n" + Style.RESET_ALL)
            continue

        existe = False
        novo_conteudo = []

        for linha in conteudo:
            linha_limpa = linha.strip()
            if not linha_limpa:
                continue

            partes = linha_limpa.split(";")
            nome = partes[0].strip().title()
            nota = float(partes[1].strip())

            if nome.lower() == nome_aluno.lower():
                existe = True
                print(Fore.GREEN + f"\nAluno encontrado! Nome atual: {nome.title()} | Nota atual: {nota:.2f}" + Style.RESET_ALL)

                # Solicitação do novo nome
                while True:
                    novo_nome = input(Fore.WHITE + "Digite o novo nome (Clique ENTER para não alterar o nome): " + Style.RESET_ALL).strip().title()
                    if novo_nome == "":
                        novo_nome = nome.title()  # Mantém o nome antigo se nada for digitado
                        break
                    elif not novo_nome.replace(" ", "").isalpha():
                        print(Fore.RED + "✘ Digite apenas letras, sem números ou símbolos!" + Style.RESET_ALL)
                    else:
                        break

                # Solicitação da nova nota
                while True:
                    try:
                        nova_nota = float(input(Fore.WHITE + "Digite a nova nota: " + Style.RESET_ALL).strip().replace(",", "."))
                        if nova_nota < 0 or nova_nota > 10:
                            print(Fore.RED + "✘ Digite uma nota válida (0 a 10)!" + Style.RESET_ALL)
                        else:
                            break
                    except ValueError:
                        print(Fore.RED + "✘ Digite apenas números!\n" + Style.RESET_ALL)

                novo_conteudo.append(f"{novo_nome.title()};{nova_nota:.2f}\n")
            else:
                novo_conteudo.append(f"{nome.title()};{nota:.2f}\n")

        if existe:
            with open("dados_alunos.txt", "w", encoding="utf-8") as arquivo:
                arquivo.writelines(novo_conteudo)
            print(Fore.GREEN + "✔ Dados do aluno alterados com sucesso!\n" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "✘ Aluno não encontrado! Tente novamente.\n" + Style.RESET_ALL)


# ------------------------------------------------------------
# EXCLUSÃO DE REGISTRO
# Localiza o aluno, confirma a intenção e sobrescreve sem o registro
# ------------------------------------------------------------
def excluir():
    print(Fore.RED + Style.BRIGHT + "\n===== EXCLUIR ALUNO =====" + Style.RESET_ALL)

    try:
        with open("dados_alunos.txt", "r", encoding="utf-8") as arquivo:
            conteudo = arquivo.readlines()
    except FileNotFoundError:
        print(Fore.YELLOW + "⚠ Nenhum aluno cadastrado ainda!\n" + Style.RESET_ALL)
        return

    if not conteudo:
        print(Fore.YELLOW + "⚠ Nenhum aluno cadastrado ainda!\n" + Style.RESET_ALL)
        return

    while True:
        nome_excluir = input(Fore.WHITE + "Digite o nome do aluno que deseja excluir: " + Style.RESET_ALL).strip().title()

        if not (nome_excluir and nome_excluir.replace(" ", "").isalpha()):
            print(Fore.RED + "✘ Digite um nome válido apenas com letras!\n" + Style.RESET_ALL)
            continue

        existe = False
        novo_conteudo = []

        for linha in conteudo:
            linha_limpa = linha.strip()
            if not linha_limpa:
                continue
                
            partes = linha_limpa.split(";")
            nome = partes[0].strip()
            nota = float(partes[1].strip())
            estado = "Aprovado" if nota >= 6 else "Reprovado"

            if nome.lower() == nome_excluir.lower():
                existe = True
                print(Fore.GREEN + f"\nAluno encontrado! Nome: {nome} | Nota: {nota:.2f} | Estado: {estado}" + Style.RESET_ALL)

                while True:
                    escolha = input(Fore.YELLOW + "Tem certeza que deseja excluir? (S/N): " + Style.RESET_ALL).strip().lower()
                    if escolha == "s":
                        print(Fore.GREEN + "✔ Aluno excluído com sucesso!\n" + Style.RESET_ALL)
                        break
                    elif escolha == "n":
                        novo_conteudo.append(f"{nome};{nota:.2f}\n")
                        print(Fore.MAGENTA + "Exclusão cancelada!\n" + Style.RESET_ALL)
                        break
                    else:
                        print(Fore.RED + "✘ Digite apenas 'S' ou 'N'!\n" + Style.RESET_ALL)
            else:
                novo_conteudo.append(f"{nome};{nota:.2f}\n")

        if existe:
            with open("dados_alunos.txt", "w", encoding="utf-8") as arquivo:
                arquivo.writelines(novo_conteudo)
            break
        else:
            print(Fore.RED + "✘ Aluno não encontrado! Tente novamente.\n" + Style.RESET_ALL)


menu()