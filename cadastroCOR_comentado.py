# ==================================================================
# SISTEMA DE CADASTRO DE ALUNOS (CRUD em Arquivo Texto) --- EXERCICIO 28
# Cadastra, lista, altera e exclui alunos, salvando tudo em um
# arquivo .txt para que os dados não se percam ao fechar o programa
# ==================================================================

import os  # Importa o módulo 'os' para manipulação e verificação de arquivos no sistema operacional
from colorama import Fore, Style, init  # Importa classes de cores e estilos para formatar saídas no terminal

# init() prepara o terminal para interpretar corretamente as cores
init()  # Inicializa a biblioteca Colorama

# Nome do arquivo onde os alunos ficam gravados
ARQUIVO = "alunos.txt"  # Define a constante global com o nome do arquivo texto

# Cabeçalho gravado no início do arquivo, só para deixar organizado
# quando alguém abrir o alunos.txt em um editor de texto comum
CABECALHO = (  # Define a constante com a string multilinha do cabeçalho
    "# ================================================\n"  # Linha decorativa no arquivo
    "# ARQUIVO DE ALUNOS - GERADO PELO SISTEMA EM PYTHON\n"  # Título no arquivo
    "# NAO EDITE ESTE ARQUIVO MANUALMENTE\n"  # Aviso no arquivo
    "# FORMATO: NOME (20 colunas) ; NOTA\n"  # Formatação usada no arquivo
    "# ================================================\n"  # Linha decorativa no arquivo
)  # Fecha a atribuição da constante CABECALHO

# Largura usada na caixa do menu (efeito visual)
LARGURA_MENU = 44  # Define a largura padrão em caracteres para o menu visual

# Larguras das colunas da tabela de listagem
COL_NOME = 20  # Define a largura da coluna 'Nome'
COL_NOTA = 8  # Define a largura da coluna 'Nota'
COL_SITUACAO = 11  # Define a largura da coluna 'Situação'


# ------------------------------------------------------------
# Garante que o arquivo já exista com o cabeçalho, antes de
# começarmos a acrescentar (append) registros nele
# ------------------------------------------------------------
def garantir_cabecalho():  # Define a função responsável por criar o arquivo com cabeçalho caso não exista
    if not os.path.exists(ARQUIVO):  # Verifica se o arquivo ainda NÃO existe no diretório
        try:  # Inicia bloco para tratamento de exceção ao tentar criar/escrever o arquivo
            with open(ARQUIVO, "w", encoding="utf-8") as dados:  # Abre o arquivo no modo escrita ("w")
                dados.write(CABECALHO)  # Escreve o cabeçalho inicial no arquivo criado
        except PermissionError:  # Captura erro caso o programa não tenha permissão de escrita
            print(Fore.RED + "✘ Não foi possível criar o arquivo alunos.txt." + Style.RESET_ALL)  # Exibe erro em vermelho


# ------------------------------------------------------------
# Lê o arquivo texto e devolve uma lista de dicionários,
# ignorando as linhas de cabeçalho (que começam com #) e
# pulando, sem travar o programa, qualquer linha corrompida
# ------------------------------------------------------------
def carregar_alunos():  # Define a função responsável por carregar os alunos do arquivo texto
    alunos = []  # Inicializa uma lista vazia para armazenar os alunos lidos
    if not os.path.exists(ARQUIVO):  # Verifica se o arquivo não existe
        return alunos  # Retorna a lista vazia se o arquivo não existir

    try:  # Inicia bloco para tratamento de exceção ao tentar ler o arquivo
        with open(ARQUIVO, "r", encoding="utf-8") as dados:  # Abre o arquivo no modo leitura ("r")
            linhas = dados.readlines()  # Lê todas as linhas do arquivo e armazena numa lista
    except PermissionError:  # Captura erro caso o programa não tenha permissão de leitura
        print(Fore.RED + "✘ Não foi possível abrir o arquivo alunos.txt." + Style.RESET_ALL)  # Exibe erro em vermelho
        return alunos  # Retorna a lista vazia em caso de erro de permissão

    for linha in linhas:  # Itera sobre cada linha lida do arquivo
        linha_limpa = linha.strip()  # Remove espaços em branco e quebras de linha nas extremidades
        # Ignora linhas em branco e linhas de cabeçalho (comentários)
        if linha_limpa == "" or linha_limpa.startswith("#"):  # Checa se a linha está vazia ou é comentário
            continue  # Pula para a próxima iteração do laço
        try:  # Inicia bloco para tratamento de conversão de dados da linha
            partes = linha_limpa.split(";")  # Divide a linha em partes usando o delimitador ";"
            nome = partes[0].strip()  # Extrai o nome e remove espaços adicionais
            nota = float(partes[1].strip())  # Extrai a nota e converte para número de ponto flutuante (float)
            alunos.append({"nome": nome, "nota": nota})  # Adiciona um dicionário com nome e nota à lista de alunos
        except (ValueError, IndexError):  # Captura erro se o split falhar ou se a nota não for número válido
            # Linha mal formatada (sem ";" ou nota inválida) é ignorada
            continue  # Pula linhas corrompidas e prossegue o laço

    return alunos  # Retorna a lista completa com os alunos carregados


# ------------------------------------------------------------
# Reescreve o arquivo inteiro (cabeçalho + alunos), usada
# depois de alterar ou excluir um registro.
# Devolve True se conseguiu salvar, False se deu erro.
# ------------------------------------------------------------
def salvar_todos(alunos):  # Define a função para regravar toda a lista no arquivo
    try:  # Inicia bloco para tratamento de exceções de escrita
        with open(ARQUIVO, "w", encoding="utf-8") as dados:  # Sobrescreve o arquivo no modo escrita ("w")
            dados.write(CABECALHO)  # Grava o cabeçalho no topo do arquivo
            for aluno in alunos:  # Itera sobre cada dicionário de aluno na lista
                dados.write(f"{aluno['nome']:<20};{aluno['nota']:.2f}\n")  # Escreve os dados formatados com alinhamento
        return True  # Retorna verdadeiro em caso de sucesso
    except PermissionError:  # Captura erro de permissão de escrita no arquivo
        print(Fore.RED + "✘ Não foi possível salvar. Feche o arquivo se estiver aberto." + Style.RESET_ALL)  # Exibe erro em vermelho
        return False  # Retorna falso indicando que a operação falhou


# ------------------------------------------------------------
# Exibe o menu principal dentro de uma caixa desenhada com
# caracteres Unicode (efeito de "moldura")
# ------------------------------------------------------------
def exibir_menu():  # Define a função de exibição visual do menu
    print(Fore.CYAN + "╔" + "═" * LARGURA_MENU + "╗" + Style.RESET_ALL)  # Imprime o topo da moldura em ciano
    print(  # Inicia o print para o título centralizado
        Fore.CYAN + "║" + Style.RESET_ALL +  # Borda esquerda
        Style.BRIGHT + Fore.WHITE + "SISTEMA DE CADASTRO DE ALUNOS".center(LARGURA_MENU) + Style.RESET_ALL +  # Texto do título
        Fore.CYAN + "║" + Style.RESET_ALL  # Borda direita
    )  # Fecha o print do título
    print(Fore.CYAN + "╠" + "═" * LARGURA_MENU + "╣" + Style.RESET_ALL)  # Imprime a linha divisória do menu
    print(Fore.CYAN + "║" + Style.RESET_ALL + "  1 - Cadastrar aluno".ljust(LARGURA_MENU) + Fore.CYAN + "║" + Style.RESET_ALL)  # Opção 1
    print(Fore.CYAN + "║" + Style.RESET_ALL + "  2 - Listar alunos".ljust(LARGURA_MENU) + Fore.CYAN + "║" + Style.RESET_ALL)  # Opção 2
    print(Fore.CYAN + "║" + Style.RESET_ALL + "  3 - Alterar aluno".ljust(LARGURA_MENU) + Fore.CYAN + "║" + Style.RESET_ALL)  # Opção 3
    print(Fore.CYAN + "║" + Style.RESET_ALL + "  4 - Excluir aluno".ljust(LARGURA_MENU) + Fore.CYAN + "║" + Style.RESET_ALL)  # Opção 4
    print(  # Inicia o print para a opção Sair
        Fore.CYAN + "║" + Style.RESET_ALL +  # Borda esquerda
        Fore.RED + "  0 - Sair".ljust(LARGURA_MENU) + Style.RESET_ALL +  # Texto da opção de sair em vermelho
        Fore.CYAN + "║" + Style.RESET_ALL  # Borda direita
    )  # Fecha o print da opção Sair
    print(Fore.CYAN + "╚" + "═" * LARGURA_MENU + "╝" + Style.RESET_ALL)  # Imprime o fundo da moldura em ciano


# ------------------------------------------------------------
# Pede um nome ao usuário e SÓ sai do laço quando o valor
# digitado for texto válido (sem números/símbolos e não vazio).
# Serve tanto para cadastrar quanto para buscar um aluno.
# ------------------------------------------------------------
def ler_nome(mensagem):  # Define a função auxiliar para leitura e validação de nomes
    while True:  # Laço infinito até que a entrada seja considerada válida
        nome = input(mensagem).strip().title()  # Lê o input, remove espaços sobressalentes e formata em Title Case

        if nome == "":  # Valida se a string fornecida está vazia
            print(Fore.RED + "✘ O nome não pode ficar vazio!" + Style.RESET_ALL)  # Alerta o usuário em vermelho
            continue  # Reinicia o laço pedindo a entrada novamente

        if not nome.replace(" ", "").isalpha():  # Remove espaços temporariamente para checar se contém apenas letras
            print(Fore.RED + "✘ Digite apenas letras, sem números ou símbolos!" + Style.RESET_ALL)  # Alerta sobre caracteres inválidos
            continue  # Reinicia o laço

        return nome  # Retorna o nome válido e encerra a função


# ------------------------------------------------------------
# Pede uma nota ao usuário e SÓ sai do laço quando o valor
# digitado for um número válido entre 0 e 10. Aceita vírgula
# ou ponto como separador decimal (ex: 8,5 ou 8.5).
# ------------------------------------------------------------
def ler_nota(mensagem):  # Define a função auxiliar para leitura e validação de notas
    while True:  # Laço infinito para garantir entrada válida
        entrada = input(mensagem).strip().replace(",", ".")  # Lê o input, remove espaços e troca vírgula por ponto

        try:  # Tenta realizar a conversão do input para o tipo float
            nota = float(entrada)  # Converte a string limpa para float
        except ValueError:  # Trata exceção caso a conversão para float falhe
            print(Fore.RED + "✘ Digite apenas números." + Style.RESET_ALL)  # Exibe mensagem de erro
            continue  # Reinicia a solicitação de entrada

        if nota < 0 or nota > 10:  # Valida o intervalo numérico permitido para a nota
            print(Fore.RED + "✘ A nota deve estar entre 0 e 10." + Style.RESET_ALL)  # Informa intervalo correto
            continue  # Reinicia a solicitação de entrada

        return nota  # Retorna a nota válida em formato float


# ------------------------------------------------------------
# Cadastra um novo aluno, acrescentando uma linha ao arquivo
# ------------------------------------------------------------
def cadastrar_aluno():  # Define a função de cadastro de um novo aluno
    print(Fore.CYAN + Style.BRIGHT + "\n===== CADASTRAR ALUNO =====" + Style.RESET_ALL)  # Exibe título do menu de cadastro

    # ler_nome() e ler_nota() ficam presos em while True até vir um valor válido
    nome = ler_nome("Digite o nome do aluno: ")  # Solicita e valida o nome
    nota = ler_nota("Digite a nota do aluno: ")  # Solicita e valida a nota

    garantir_cabecalho()  # Executa a garantia da existência do arquivo/cabeçalho antes da gravação

    try:  # Tenta abrir e gravar a nova entrada no arquivo
        # Modo "a" (append) acrescenta a linha sem apagar quem já existe
        with open(ARQUIVO, "a", encoding="utf-8") as dados:  # Abre o arquivo no modo de adição ("a")
            dados.write(f"{nome:<20};{nota:.2f}\n")  # Grava o nome ajustado a 20 caracteres e nota com 2 casas decimais
    except PermissionError:  # Trata falha de acesso para escrita
        print(Fore.RED + "✘ Não foi possível salvar. Feche o arquivo se estiver aberto." + Style.RESET_ALL)  # Exibe erro
        return  # Sai da função em caso de falha

    print(Fore.GREEN + "✔ Aluno cadastrado com sucesso!" + Style.RESET_ALL)  # Exibe confirmação de cadastro


# ------------------------------------------------------------
# Lista os alunos em uma tabela bonita, com bordas e cores
# ------------------------------------------------------------
def listar_alunos():  # Define a função para listagem e exibição dos alunos
    print(Fore.CYAN + Style.BRIGHT + "\n===== ALUNOS CADASTRADOS =====" + Style.RESET_ALL)  # Exibe título da seção de listagem

    alunos = carregar_alunos()  # Obtém a lista atualizada de alunos através do arquivo
    if not alunos:  # Checa se a lista retornada está vazia
        print(Fore.YELLOW + "⚠ Nenhum aluno cadastrado ainda." + Style.RESET_ALL)  # Avisa que não existem dados a serem listados
        return  # Sai da função

    # Bordas da tabela, calculadas a partir da largura de cada coluna
    topo = "╔" + "═" * (COL_NOME + 2) + "╦" + "═" * (COL_NOTA + 2) + "╦" + "═" * (COL_SITUACAO + 2) + "╗"  # Borda superior da tabela
    meio = "╠" + "═" * (COL_NOME + 2) + "╬" + "═" * (COL_NOTA + 2) + "╬" + "═" * (COL_SITUACAO + 2) + "╣"  # Divisória do cabeçalho da tabela
    fim = "╚" + "═" * (COL_NOME + 2) + "╩" + "═" * (COL_NOTA + 2) + "╩" + "═" * (COL_SITUACAO + 2) + "╝"  # Borda inferior da tabela

    print(Fore.CYAN + topo + Style.RESET_ALL)  # Imprime o topo da tabela
    print(  # Inicia o print para o cabeçalho com os nomes das colunas
        Fore.CYAN + "║ " + Style.RESET_ALL + Style.BRIGHT +  # Moldura e início do texto
        "NOME".ljust(COL_NOME) + Style.RESET_ALL +  # Coluna Nome
        Fore.CYAN + " ║ " + Style.RESET_ALL + Style.BRIGHT +  # Moldura intermediária
        "NOTA".center(COL_NOTA) + Style.RESET_ALL +  # Coluna Nota
        Fore.CYAN + " ║ " + Style.RESET_ALL + Style.BRIGHT +  # Moldura intermediária
        "SITUAÇÃO".center(COL_SITUACAO) + Style.RESET_ALL +  # Coluna Situação
        Fore.CYAN + " ║" + Style.RESET_ALL  # Moldura direita
    )  # Finaliza o print do cabeçalho
    print(Fore.CYAN + meio + Style.RESET_ALL)  # Imprime a linha do meio da tabela

    aprovados = 0  # Inicializa contador de alunos aprovados
    reprovados = 0  # Inicializa contador de alunos reprovados
    maior = alunos[0]  # Define provisoriamente o primeiro aluno como o de maior nota
    menor = alunos[0]  # Define provisoriamente o primeiro aluno como o de menor nota

    # Percorre a lista de alunos e monta uma linha da tabela para cada um
    for aluno in alunos:  # Itera por cada aluno carregado
        nome = aluno["nome"]  # Extrai o nome do dicionário atual
        nota = aluno["nota"]  # Extrai a nota do dicionário atual

        if nota >= 6:  # Define se o aluno atingiu a média de aprovação (>= 6)
            situacao_texto = "APROVADO"  # Define o texto da situação
            cor_situacao = Fore.GREEN  # Atribui cor verde para aprovados
            aprovados += 1  # Incrementa a contagem de aprovados
        else:  # Caso a nota seja menor que 6
            situacao_texto = "REPROVADO"  # Define o texto da situação
            cor_situacao = Fore.RED  # Atribui cor vermelha para reprovados
            reprovados += 1  # Incrementa a contagem de reprovados

        # Compara notas para descobrir o maior e o menor aluno da turma
        if nota > maior["nota"]:  # Checa se a nota do aluno atual supera a maior registrada
            maior = aluno  # Atualiza a referência do aluno com maior nota
        if nota < menor["nota"]:  # Checa se a nota do aluno atual é inferior à menor registrada
            menor = aluno  # Atualiza a referência do aluno com menor nota

        linha_tabela = (  # Monta a string formatada para a linha da tabela correspondente ao aluno
            Fore.CYAN + "║ " + Style.RESET_ALL +  # Borda esquerda
            nome[:COL_NOME].ljust(COL_NOME) +  # Trunca e alinha o nome na coluna
            Fore.CYAN + " ║ " + Style.RESET_ALL +  # Separador
            f"{nota:.2f}".center(COL_NOTA) +  # Formata nota com 2 casas e centraliza
            Fore.CYAN + " ║ " + Style.RESET_ALL +  # Separador
            cor_situacao + situacao_texto.center(COL_SITUACAO) + Style.RESET_ALL +  # Exibe situação colorida centralizada
            Fore.CYAN + " ║" + Style.RESET_ALL  # Borda direita
        )  # Conclui a construção da linha
        print(linha_tabela)  # Exibe a linha formatada no terminal

    print(Fore.CYAN + fim + Style.RESET_ALL)  # Imprime o fechamento da tabela

    # Resumo da turma
    print(Fore.MAGENTA + f"\nTotal de alunos : {len(alunos)}" + Style.RESET_ALL)  # Exibe o total geral de alunos
    print(Fore.GREEN + f"Aprovados       : {aprovados}" + Style.RESET_ALL)  # Exibe a contagem de aprovados em verde
    print(Fore.RED + f"Reprovados      : {reprovados}" + Style.RESET_ALL)  # Exibe a contagem de reprovados em vermelho
    print(Fore.YELLOW + f"★ Maior nota    : {maior['nome']} ({maior['nota']:.2f})" + Style.RESET_ALL)  # Exibe o aluno com maior nota
    print(Fore.YELLOW + f"★ Menor nota    : {menor['nome']} ({menor['nota']:.2f})" + Style.RESET_ALL)  # Exibe o aluno com menor nota


# ------------------------------------------------------------
# Altera o nome e/ou a nota de um aluno já cadastrado
# ------------------------------------------------------------
def alterar_aluno():  # Define a função responsável pela alteração dos dados de um aluno
    print(Fore.CYAN + Style.BRIGHT + "\n===== ALTERAR ALUNO =====" + Style.RESET_ALL)  # Exibe o título da tela de alteração

    alunos = carregar_alunos()  # Carrega os alunos salvos no arquivo
    if not alunos:  # Verifica se a lista está vazia
        print(Fore.YELLOW + "⚠ Nenhum aluno cadastrado ainda." + Style.RESET_ALL)  # Exibe aviso de lista vazia
        return  # Encerra a função

    while True:  # Entra num laço de busca para a alteração
        # Reaproveita ler_nome() também na busca, já que todo nome salvo é só letras
        nome_procurado = ler_nome("Digite o nome do aluno que deseja alterar: ")  # Pede o nome do alvo da busca

        # Variável de controle para saber se o aluno foi encontrado
        encontrado = False  # Flag de controle inicializada como False

        for aluno in alunos:  # Percorre cada aluno da lista
            if aluno["nome"] == nome_procurado:  # Checa se encontrou o aluno correspondente
                encontrado = True  # Marca que o aluno foi localizado

                # ler_nome() e ler_nota() só devolvem valor quando estiver correto
                novo_nome = ler_nome("Digite o novo nome: ")  # Solicita validação e entrada do novo nome
                nova_nota = ler_nota("Digite a nova nota: ")  # Solicita validação e entrada da nova nota

                aluno["nome"] = novo_nome  # Atualiza o nome do registro na memória
                aluno["nota"] = nova_nota  # Atualiza a nota do registro na memória
                break  # Para a iteração no loop de busca

        if not encontrado:  # Se a flag continuar como False
            print(Fore.RED + "✘ Aluno não encontrado! Tente novamente." + Style.RESET_ALL)  # Informa que a busca falhou
            continue  # Repete o loop para o usuário tentar outro nome

        if salvar_todos(alunos):  # Reescreve o arquivo inteiro salvando as modificações feitas
            print(Fore.GREEN + "✔ Aluno alterado com sucesso!" + Style.RESET_ALL)  # Notifica o êxito
        break  # Sai do laço while principal da função


# ------------------------------------------------------------
# Exclui um aluno do arquivo texto
# ------------------------------------------------------------
def excluir_aluno():  # Define a função de exclusão de alunos
    print(Fore.CYAN + Style.BRIGHT + "\n===== EXCLUIR ALUNO =====" + Style.RESET_ALL)  # Exibe título do menu de exclusão

    alunos = carregar_alunos()  # Lê os dados cadastrados atualmente
    if not alunos:  # Se não existirem cadastros
        print(Fore.YELLOW + "⚠ Nenhum aluno cadastrado ainda." + Style.RESET_ALL)  # Exibe aviso
        return  # Sai da função

    while True:  # Laço para lidar com a digitação do nome para remoção
        # Reaproveita ler_nome() também na busca, já que todo nome salvo é só letras
        nome_procurado = ler_nome("Digite o nome do aluno que deseja excluir: ")  # Coleta o nome digitado validado

        encontrado = False  # Sinalizador para saber se o aluno foi localizado
        novos_alunos = []  # Cria uma nova lista auxiliar que armazenará todos os alunos, exceto o excluído

        for aluno in alunos:  # Percorre os cadastros originais
            if aluno["nome"] == nome_procurado and not encontrado:  # Identifica a primeira ocorrência do aluno procurado
                encontrado = True  # Marca como encontrado para ignorar o registro (não adiciona esse aluno na nova lista = exclui)
            else:  # Para todos os outros registros
                novos_alunos.append(aluno)  # Adiciona à nova lista mantida

        if not encontrado:  # Caso a busca não tenha retornado correspondência
            print(Fore.RED + "✘ Aluno não encontrado! Tente novamente." + Style.RESET_ALL)  # Notifica usuário
            continue  # Volta para o início do laço repedindo a digitação do nome

        if salvar_todos(novos_alunos):  # Reescreve o arquivo gravando apenas a lista filtrada sem o aluno removido
            print(Fore.GREEN + "✔ Aluno excluído com sucesso!" + Style.RESET_ALL)  # Confirmação de remoção

        break  # Sai do laço após a exclusão e gravação bem-sucedidas


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# Mantém o menu ativo até o usuário escolher sair (opção 0)
# ------------------------------------------------------------
while True:  # Laço principal de execução constante do programa
    exibir_menu()  # Chama a função para desenhar a interface do menu
    opcao = input(Fore.WHITE + "Escolha uma opção: " + Style.RESET_ALL).strip()  # Lê e limpa a opção escolhida pelo usuário

    if opcao == "1":  # Se o usuário escolheu a opção '1'
        cadastrar_aluno()  # Executa o cadastro do aluno
    elif opcao == "2":  # Se o usuário escolheu a opção '2'
        listar_alunos()  # Exibe a lista completa de alunos
    elif opcao == "3":  # Se o usuário escolheu a opção '3'
        alterar_aluno()  # Inicia o fluxo de alteração de cadastro
    elif opcao == "4":  # Se o usuário escolheu a opção '4'
        excluir_aluno()  # Inicia o fluxo para deleção de cadastro
    elif opcao == "0":  # Se o usuário escolheu a opção '0'
        print(Fore.CYAN + "\n 🖑 Sistema encerrado. Até logo! 🖑 " + Style.RESET_ALL)  # Mensagem de encerramento
        break  # Interrompe o laço principal, finalizando o script Python
    else:  # Caso o valor digitado não corresponda a nenhuma opção acima
        print(Fore.RED + "✘ Opção inválida. Tente novamente." + Style.RESET_ALL)  # Alerta opção inexistente e repete a exibição do menu