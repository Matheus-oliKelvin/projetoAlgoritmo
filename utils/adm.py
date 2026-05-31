import  json
from datetime import datetime
from utils.geral import *
from rich import print
from rich.table import Table


def cadastrar_animal_unico(animais: dict):
    especie_animal= input("Digite a especie do animal: ").lower().strip()
    raca_animal= input("Digite a raça do animal: ").lower().strip()
    peso_animal= float(input("Digite o peso do animal: "))

    data_pesagem= datetime.now().strftime("%Y-%m-%d")

    while True:
        identificacao_animal = input("Digite a identificação desse animal: ").lower().strip()

        if verificar_existe(animais, identificacao_animal):
            print("[yellow]Essa identificação já está cadastrada!Digite novamente[/yellow]\n")

        else:
            break
    
    while True:
        status_animal= input("Qual o status desse animal: ").lower().strip()

        if status_animal not in ("a venda", "lactacao", "engorda", "gestacao", "postura"):
            print("Status inválido! Digite novamente\n")
        else:
            break
    
    if status_animal == "a venda":
        preco_animal= float(input("Digite o preço desse animal: "))
    else:
        preco_animal= None

    lote_pertencente= None

    animais[identificacao_animal] = {
        "especie": especie_animal,
        "raca": raca_animal,
        "historico_peso": [{"peso":peso_animal, "data":data_pesagem}],
        "status": status_animal,
        "preco": preco_animal,
        "lote":  lote_pertencente
    }
    
    with open("data/animais.json", "w") as arquivo:
        json.dump(animais, arquivo, indent=4)

    print("\n[green]Animal cadastrado![/green]")

    pausar()



def cadastrar_animais_lote(lotes: dict, animais: dict):

    while True:
        nome_lote=input("Digite o nome desse lote: ")

        if verificar_existe(lotes, nome_lote):
            print("[yellow]Esse lote já está cadastrado!Digite novamente[/yellow]\n")

        else:
            break

    especie_lote = input("Digite a espécie dos animais do lote: ").lower().strip()
    raca_lote=input("Digite a raça dos animais do lote : ").lower().strip()

    peso_medio= float(input("Digite o peso médio do lote :"))
    data_pesagem= datetime.now().strftime("%Y-%m-%d")

    quantidade_lote = int(input("Digite a quantidade de animais do lote :"))


    while True:
        status_lote= input("Digite o status dos animais do lote : ").lower()

        if status_lote not in ["a venda", "lactacao", "engorda", "gestacao"]:
            print("Status inválido! Digite novamente\n")
        else:
            break

    if status_lote == "a venda":
        preco_lote= float(input("Digite o preço desse lote: "))

      
    else:
        preco_lote= None

    lotes[nome_lote] = {
    "especie": especie_lote,
    "raca": raca_lote,
    "quantidade": quantidade_lote,
    "historico_peso":[{"peso":peso_medio, "data":data_pesagem}],
    "status": status_lote,
    "preco": preco_lote,
    }
    
    with open("data/lotes.json", "w") as arquivo:
        json.dump(lotes, arquivo, indent=4)

    print("\n[green]Lote cadastrado![/green]")


    for i in range (1,lotes[nome_lote]["quantidade"]+1):

        identificacao_animal = "0"+ str(i) +" - " + nome_lote

        animais[identificacao_animal] = {
        "especie": especie_lote,
        "raca": raca_lote,
        "historico_peso": [{"peso":peso_medio, "data":data_pesagem}],
        "status": status_lote,
        "preco": None,
        "lote":  nome_lote
    }
    with open("data/animais.json", "w") as arquivo:
        json.dump(animais, arquivo, indent=4)

    pausar()
    limpar()

def mostrar_Animais (estoque: dict, identificacoes: list):
    tabela = Table(title="[bold cyan] ESTOQUE ANIMAIS  [/bold cyan]", border_style="cyan")

    tabela.add_column("ID", style="yellow", justify="center")
    tabela.add_column("Espécie", style="purple")
    tabela.add_column("Raça", style="white")
    tabela.add_column("Peso", style="green", justify="right")
    tabela.add_column("Status", style="magenta")
    tabela.add_column("Preço (R$)", style="blue", justify="right")
    tabela.add_column("Lote", style="red", justify="center")

    for identificacao in identificacoes:

        peso_atual= estoque[identificacao]["historico_peso"][-1].get("peso")


        tabela.add_row(
            identificacao,
            estoque[identificacao]["especie"].upper(),
            estoque[identificacao]["raca"],
            str(peso_atual),
            estoque[identificacao]["status"],
            str(estoque[identificacao]["preco"]),
            str(estoque[identificacao]["lote"])
        )

    print(tabela)

def mostrar_menu_adm(animais: dict, lotes: dict, login: dict):

    while True:
        print("1- Cadastrar animais ") 
        print("2- Buscar animais ") 
        print("3- Atualizar animais ") 
        print("4- Remover animais")
        print("5- Visualizar estoque de animais")
        print("6- Registrar produção de leite")
        print("7- Adicionar produtos fabricados")
        print("8- Visualizar estoque de produtos")
        print("9- Analisar produtividade ( com @ )")
        print("0- Sair")

        opcao= int(input(" >  "))
        if validar_opcao(opcao, 0 , 9):
            break
        else:
            print(" [yellow] Opção invalida! Digite novamente [/yellow] \n")

    if opcao == 0:
        deslogar(login)

    elif opcao == 1:
        while True:
            print("1- Cadastrar animal único")
            print("2- Cadastrar por Lote")

            opcao= int(input("Digite a opção desejada: "))

            if validar_opcao(opcao,1,2):
                break
            else:
                print("Opção invalida! Digite novamente\n")
        
        if opcao == 1:
            cadastrar_animal_unico(animais)
        else:
            cadastrar_animais_lote(lotes,animais)

    elif opcao == 2:

        while True:
            print("1- Buscar Animal ")
            print("2- Buscar Lote")

            opcao= int(input("> "))

            if validar_opcao(opcao,1,2):
                break
            else:
                print("Opção invalida! Digite novamente\n")

        if opcao == 1:
            identificacao_animal= input("Digite a identificação do animal que deseja buscar: ").lower().strip()

            if buscar_por_identificacao(animais,identificacao_animal) is None:
                print("\nAnimal não encontrado no sistema!")
            else:
                mostrar_Animais(animais,[identificacao_animal])
                

       
       

       