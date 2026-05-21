# Cria a lista principal onde os dados dos alunos serão armazenados
alunos = []


# Função responsável por cadastrar um aluno
def registrar_aluno():

    # Exibe o título da área de cadastro
    print("\nRegistro do aluno:")

    # Loop utilizado para validar o nome digitado
    while True:

        # Solicita o nome do aluno, remove espaços extras e coloca em formato título
        nome = input("Digite o nome do aluno: ").strip().title()

        # Verifica se o nome contém apenas letras e espaços
        if nome.replace(" ", "").isalpha():

            # Encerra o loop caso o nome seja válido
            break

        else:
            # Exibe mensagem de erro caso o nome seja inválido
            print("\nDigite APENAS texto!")

    # Loop utilizado para validar a idade
    while True:

        try:
            # Solicita a idade e converte o valor para inteiro
            idade = int(input("Digite a idade: ").strip())

            # Verifica se a idade é menor que 1
            if idade < 1:

                # Exibe mensagem de erro para idade inválida
                print("\nDigite APENAS números maiores que 0!")

            else:
                # Encerra o loop caso a idade seja válida
                break

        # Captura erro caso o usuário digite algo diferente de número inteiro
        except ValueError:

            # Exibe mensagem de erro
            print("\nDigite APENAS números inteiros!")

    # Loop utilizado para validar a nota
    while True:

        try:
            # Solicita a nota e converte o valor para float
            nota = float(input("Digite a nota: ").strip().replace(",", "."))

            # Verifica se a nota está fora do intervalo permitido
            if nota > 10 or nota < 0:

                # Exibe mensagem de erro
                print("\nDigite APENAS números de 0 a 10!")

            else:
                # Encerra o loop caso a nota seja válida
                break

        # Captura erro caso seja digitado um valor inválido
        except ValueError:

            # Exibe mensagem de erro
            print("\nDigite APENAS números!")

    # Verifica se o aluno foi aprovado
    if nota >= 7:

        # Define a situação como aprovado
        stats = "aprovado"

    # Verifica se o aluno ficou de recuperação
    elif nota >= 5:

        # Define a situação como recuperação
        stats = "recuperação"

    else:
        # Define a situação como reprovado
        stats = "reprovado"

    # Cria um dicionário contendo os dados do aluno
    aluno = {

        # Armazena o nome do aluno
        "nome": nome,

        # Armazena a idade do aluno
        "idade": idade,

        # Armazena a nota do aluno
        "nota": nota,

        # Armazena a situação do aluno
        "status": stats
    }

    # Adiciona o aluno na lista principal
    alunos.append(aluno)

    # Exibe mensagem confirmando o cadastro
    print("\nAluno registrado!\n")


# Função responsável por calcular a média da sala
def media_sala():

    # Variável acumuladora da soma das notas
    soma = 0

    # Percorre todos os alunos cadastrados
    for aluno in alunos:

        # Soma a nota do aluno atual
        soma += aluno['nota']

    # Retorna o cálculo da média da sala
    return soma / len(alunos)


# Função responsável por exibir o relatório final
def relatorio():

    # Exibe o título do relatório
    print("\n--- RELATÓRIO ---\n")

    # Exibe o subtítulo da lista de alunos
    print("ALUNOS:")

    # Percorre todos os alunos cadastrados
    for aluno in alunos:

        # Exibe os dados formatados de cada aluno
        print(f"Nome: {aluno['nome']} || Idade: {aluno['idade']} || Nota: {aluno['nota']} || Situação: {aluno['status']}")

    # Define inicialmente o primeiro aluno como maior nota
    aluno_maior_nota = alunos[0]

    # Define inicialmente o primeiro aluno como menor nota
    aluno_menor_nota = alunos[0]

    # Variável que conta os alunos aprovados
    qtd_aprovados = 0

    # Variável que conta os alunos em recuperação
    qtd_recuperacao = 0

    # Variável que conta os alunos reprovados
    qtd_reprovados = 0

    # Percorre todos os alunos cadastrados
    for aluno in alunos:

        # Verifica se a nota atual é maior que a maior nota registrada
        if aluno['nota'] > aluno_maior_nota['nota']:

            # Atualiza o aluno com maior nota
            aluno_maior_nota = aluno

        # Verifica se a nota atual é menor que a menor nota registrada
        if aluno['nota'] < aluno_menor_nota['nota']:

            # Atualiza o aluno com menor nota
            aluno_menor_nota = aluno

        # Verifica se o aluno está aprovado
        if aluno['status'] == "aprovado":

            # Soma 1 ao contador de aprovados
            qtd_aprovados += 1

        # Verifica se o aluno está em recuperação
        elif aluno['status'] == "recuperação":

            # Soma 1 ao contador de recuperação
            qtd_recuperacao += 1

        else:
            # Soma 1 ao contador de reprovados
            qtd_reprovados += 1

    # Exibe a seção de notas
    print("\nNOTAS: ")

    # Exibe a média geral da sala
    print(f"Média da sala: {media_sala():.2f}")

    # Exibe o título da situação da sala
    print("\nSITUAÇÃO DA SALA:")

    # Exibe a quantidade de aprovados
    print(f"Aprovados: {qtd_aprovados}")

    # Exibe a quantidade de alunos em recuperação
    print(f"Recuperação: {qtd_recuperacao}")

    # Exibe a quantidade de alunos reprovados
    print(f"Reprovados: {qtd_reprovados}")

    # Exibe o aluno que possui a maior nota
    print(f"\nAluno com a maior nota: {aluno_maior_nota['nome']} || Nota: {aluno_maior_nota['nota']}")

    # Exibe o aluno que possui a menor nota
    print(f"Aluno com a menor nota: {aluno_menor_nota['nome']} || Nota: {aluno_menor_nota['nota']}")


# Exibe mensagem inicial do sistema
print("\nBEM-VINDO AO SISTEMA DE REGISTRAR ALUNOS")

# Exibe linha decorativa
print("--------------------------------------------------------------")


# Loop principal do programa
while True:

    # Chama a função responsável por cadastrar alunos
    registrar_aluno()

    # Loop utilizado para validar a resposta do usuário
    while True:

        # Pergunta se o usuário deseja cadastrar outro aluno
        continuar = input("Deseja adicionar outro aluno? (s/n): ").lower()

        # Verifica se o usuário digitou "s"
        if continuar == "s":

            # Sai do loop interno e continua o programa
            break

        # Verifica se o usuário digitou "n"
        elif continuar == "n":

            # Sai do loop interno
            break

        else:
            # Exibe mensagem de erro caso a resposta seja inválida
            print("\nDigite apenas 's' ou 'n'!")

    # Verifica se o usuário deseja encerrar o programa
    if continuar == "n":

        # Encerra o loop principal
        break


# Chama a função responsável por exibir o relatório final
relatorio()