# Lista para armazenar os produtos
ListaProdutos = [] 


# Classe do produto
class Produto:

    # Inicializa nome e preço
    def __init__(self, nome, preco):

        self.nome = nome
        self.preco = preco


    # Mostra os detalhes do produto
    def Detalhes(self):

        print(f"Nome do produto: {self.nome} || Preço: R${self.preco:.2f}")


# Função para cadastrar produtos
def cadastrarprod():

    # Validação do nome
    while True:

        nomeprod = input("Digite o nome do produto: ").strip().title()

        # Verifica se digitou apenas letras
        if nomeprod.isalpha():

            break
        else:

            print("\nDigite APENAS texto!")


    # Validação do preço
    while True:

        try:

            precoprod = float(input("Digite o preço do produto: ").strip().replace("," , "."))

            # Verifica se o preço é válido
            if precoprod <= 0:

                print("\nDigite APENAS números maiores que 0!")
            else:

                break


        # Trata erro de valor inválido
        except ValueError:

            print("\nDigite APENAS números!")

    # Adiciona o produto na lista
    ListaProdutos.append(Produto(nomeprod, precoprod))

    # Confirma cadastro