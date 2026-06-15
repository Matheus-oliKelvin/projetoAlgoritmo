import  json
from datetime import datetime
from utils.geral import *
from rich import print
from rich.table import Table
import matplotlib.pyplot as plt

HECTARES_FAZENDA = 120.5

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

        if verificar_status(status_animal):
            break
        else:
            print("[yellow]Status inválido, digite novamente:[/yellow]\n")
    
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
        nome_lote=input("Digite o nome desse lote: ").lower().strip()

        if verificar_existe(lotes, nome_lote):
            print("[yellow]Esse lote já está cadastrado!Digite novamente[/yellow]\n")

        else:
            break

    especie_lote = input("Digite a espécie dos animais do lote: ").lower().strip()
    raca_lote=input("Digite a raça dos animais do lote : ").lower().strip()

    peso= float(input("Digite o peso médio do lote :"))
    data_pesagem= datetime.now().strftime("%Y-%m-%d")

    quantidade_lote = int(input("Digite a quantidade de animais do lote :"))


    while True:
        status_lote= input("Digite o status dos animais do lote : ").lower().strip()

        if verificar_status(status_lote):
            break
        else:
            print("Status inválido! Digite novamente\n")


    if status_lote == "a venda":
        preco_lote= float(input("Digite o preço desse lote: "))

      
    else:
        preco_lote= None

    lotes[nome_lote] = {
    "especie": especie_lote,
    "raca": raca_lote,
    "quantidade": quantidade_lote,
    "historico_peso":[{"peso":peso,"data":data_pesagem}],
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
        "historico_peso": [{"peso":peso, "data":data_pesagem}],
        "status": status_lote,
        "preco": None,
        "lote":  nome_lote
    }
    with open("data/animais.json", "w") as arquivo:
        json.dump(animais, arquivo, indent=4)

    pausar()

def cadastrar_produtos(produtos: dict):
        
    nome_produto = input("Digite o nome do produto: ").lower().strip()

    if nome_produto in produtos:
        print("[yellow]Produto já cadastrado! Deseja adcionar mais desse produto ao estoque? (1-sim) (0-não)")

        opcao= int(input(">"))

        if opcao == 0:
            return

        peso_produto = float(input("Digite o peso que deseja adcionar ao estoque: "))

        produtos[nome_produto]["peso"] += peso_produto


    
    else:
        peso_produto = float(input("Digite o peso do produto: "))
        valor_produto = float(input("Digite o valor de venda (por kg) do produto: "))

        
        produtos[nome_produto] = {
            "peso": peso_produto,
            "valor": valor_produto
        }

    with open("data/produtos.json", "w") as arquivo:
        json.dump(produtos, arquivo, indent=4)


    print("[green]Produto cadastrado![/green]\n")


def registrar_producao_leite(producao_leite: dict, animais: dict):

    if  not verificar_ordenha_disponivel(producao_leite, animais) :
        print ("Não existe nenhum animal disponível para a ordenha!")
        pausar()
        return

    else:
        animais_para_ordenha= verificar_ordenha_disponivel(producao_leite, animais)

    mostrar_Animais(animais, animais_para_ordenha)

    while True:
        print("Digite a identificação do animal que deseja registrar a produção de leite diária: ")
        identificacao_animal = input(">").lower().strip()

        if identificacao_animal not in animais_para_ordenha:
            print("[yellow]Identificação inválida, digite novamente![/yellow]\n")
        else:
            break
    
    quantidade_leite= float(input("Digite a quantidade de leite (em litros): "))

    data_retirada= datetime.now().strftime("%Y-%m-%d")


    nova_ordenha= {"quantidade_leite": quantidade_leite, "data_retirada": data_retirada}

    if identificacao_animal not in producao_leite:
        producao_leite[identificacao_animal] = []

    producao_leite[identificacao_animal].append(nova_ordenha)


    with open("data/producao_leite.json", "w") as arquivo:
        json.dump(producao_leite, arquivo, indent=4)

    print("\n[green] Produção de leite registrada ![/green]")
    pausar()



def verificar_status(status: str):

    if status not in ("a venda", "lactacao", "engorda", "gestacao", "postura"):
            return False
    return True

def verificar_preco(preco: float):

    if preco < 0 :
        return False
    
    return True


def verificar_peso (peso: float):

    if peso < 0:
        return False
    
    return True

def verificar_ordenha_disponivel(producao_leite: dict,animais: dict):

    data_hoje= datetime.now().strftime("%Y-%m-%d")

    animais_ordenhados_hoje= []

    animais_disponiveis= []

    for animal in producao_leite:

        for registro in producao_leite[animal]:
            if registro["data_retirada"] == data_hoje:
                animais_ordenhados_hoje.append(animal)
                break

    for animal in animais:
        if animais[animal]["status"] == "lactacao" and animal not in animais_ordenhados_hoje:
            animais_disponiveis.append(animal)
    
    return animais_disponiveis

def analisar_ganho_peso_anual (animais:dict):

    ano_atual = datetime.now().year

    ganho_peso= 0

    for animal in animais:
        pesagens_ano_atual= []

        for pesagem in animais[animal]["historico_peso"]:
            data_pesagem = pesagem["data"]

            data_pesagem = datetime.strptime(data_pesagem, "%Y-%m-%d")

            ano = data_pesagem.year

            if ano == ano_atual:

                dados= { "peso": pesagem["peso"], "data": pesagem["data"]}

                pesagens_ano_atual.append(dados)
        
        if len(pesagens_ano_atual) >= 2:

            pesagens_ordenadas = sorted(pesagens_ano_atual, key=lambda pesagem: pesagem["data"])

            primeira_pesagem = pesagens_ordenadas[0]
            ultima_pesagem =   pesagens_ordenadas[-1]

            ganho_peso += ultima_pesagem["peso"] - primeira_pesagem["peso"]

           
    return ganho_peso
        

def analisar_produtividade(animais: dict, historico_arroba_por_hectare_anual: list ):
    ja_analisado= False

    ano_atual = datetime.now().year

    arroba_por_hectare_anual = 0.0

    for historico in historico_arroba_por_hectare_anual:

       if historico["ano"] == ano_atual:
            ja_analisado= True

            arroba_por_hectare_anual = historico["arroba_por_hectare"]
            break

    if not ja_analisado:
        ganho_peso_em_arroba= analisar_ganho_peso_anual(animais)  / 15.0

        arroba_por_hectare_anual = ganho_peso_em_arroba / HECTARES_FAZENDA

        registro_anual= {"ano":ano_atual, "arroba_por_hectare": arroba_por_hectare_anual}

        historico_arroba_por_hectare_anual.append(registro_anual)
        

        with open("data/historico_arroba.json", "w") as arquivo:
            json.dump(historico_arroba_por_hectare_anual, arquivo, indent=4)


    print(f"Seu @ por hectare nesse ano foi de : {arroba_por_hectare_anual}")

    if arroba_por_hectare_anual <= 8.0:
        print("\nSua produtividade está INEFICIENTE!")

    elif arroba_por_hectare_anual <= 12.0:
        print("\nSua produtividade está na MÉDIA NACIONAL!")

    elif arroba_por_hectare_anual <= 18.0:
        print("\nSua produtividade está BOA!")

    elif arroba_por_hectare_anual <= 25.0:
        print("\nSua produtividade está EXCELENTE!")
    
    else:
        print("\nSua produtividade está EXCEPCIONAL!")

    print("Deseja ver o gráfico de produtividade ao longo dos anos? (1-sim) (0-não)")
    opcao= int(input(">"))

    anos=[]
    valores=[]

    for historico in historico_arroba_por_hectare_anual:
        anos.append(historico["ano"])
        valores.append(historico["arroba_por_hectare"])

    if opcao == 1:

        plt.plot(valores, anos, marker="o", color="blue")

        
        plt.title("Evolução da Produtividade")
        plt.xlabel("Arroba por Hectare")
        plt.ylabel("Ano")
        plt.grid(True)  

       
        plt.show()



def buscar_animais( animais: dict):

    identificacao= input("Digite a identifcação desse animal: ")

    if verificar_existe(animais,identificacao):

        mostrar_Animais(animais,[identificacao]) 

    else:
        print("\n[red]Animal não encontrado no sistema![/red]")


def buscar_lotes( lotes: dict):

    nome_lote= input("Digite o nome desse lote: ").lower().strip()

    if verificar_existe(lotes,nome_lote):

        mostrar_Lotes(lotes,[nome_lote])

    else:
        print("\n[red]Lote não encontrado no sitema![/red]")


def atualizar(identificacao: str, dicionario: dict, tipo_atualizacao: str, novo_dado, nome_arquivo: str, animais: dict):

    
    if tipo_atualizacao == "peso":

        dicionario [identificacao]["historico_peso"].append({tipo_atualizacao: novo_dado, "data": datetime.now().strftime("%Y-%m-%d")})

    else:
        dicionario [identificacao][tipo_atualizacao] = novo_dado

    
    with open(f"data/{nome_arquivo}.json", "w") as arquivo:
        json.dump(dicionario, arquivo, indent=4)
    
    if nome_arquivo == "lotes":

        if tipo_atualizacao == "peso":
            for animal in animais:
                if identificacao in animal:
                    animais[animal]["historico_peso"].append({
                            "peso": novo_dado,
                            "data": datetime.now().strftime("%Y-%m-%d")
                        })
        
        else:
            for animal in animais:
                if identificacao in animal:
                    animais[animal][tipo_atualizacao] = novo_dado
           
        with open("data/animais.json", "w", encoding="utf-8") as arq_animais:
            json.dump(animais, arq_animais, indent=4, ensure_ascii=False)


def atualizar_animais(animais: dict):

    identificacao_animal = input(f"Digite a identificação do animal que deseja atualizar:  ")

    if  not verificar_existe( animais, identificacao_animal):

        print("[yellow]Identificação não encontrada no sistema![/yellow]\n")

        return


    atualizacao=input("O que você deseja atualizar: ").lower().strip()

    if atualizacao == "status":

        status_atual= animais[identificacao_animal]["status"]

        print(f"Status atual: {status_atual}")

        while True:
            novo_status= input("Digite o novo status : ")

            if verificar_status(novo_status):
                break
            else:
                print("Status inválido! Digite novamente\n")

        atualizar(identificacao_animal,animais, atualizacao, novo_status,"animais", animais)
        
        print("[green]Status atualizado![/green]")

    elif atualizacao == "preco":

        if animais[identificacao_animal]["preco"] is None:
            print("[yellow]Esse animal não está à venda![/yellow]\n")
        else:

            preco_atual= animais[identificacao_animal]["preco"]

            print(f"Preço atual: {preco_atual}")

            novo_preco = float(input("Digite o novo preço: "))

            while True:
                if verificar_preco(novo_preco):
                    break
                else:
                    print("Preço inválido! Digite novamente\n")

            atualizar(identificacao_animal, animais,atualizacao, novo_preco,"animais", animais)

            print("[green]Preço atualizado![/green]")

    elif atualizacao == "peso":

        peso_atual= animais[identificacao_animal]["historico_peso"][-1].get("peso")
        print(f"Peso atual: {peso_atual}")


        novo_peso = float(input("Digite o novo peso: "))

        while True:
            if verificar_peso(novo_peso):
                break
            else:
                print("Peso inválido! Digite novamente\n")

        atualizar(identificacao_animal, animais,atualizacao, novo_peso,"animais", animais)

        print("[green]Peso atualizado![/green]")

    else:
        print("[red]Atualização inválida![/red]\n")

def atualizar_lotes(lotes: dict, animais:dict):

    nome_lote = input(f"Digite o nome do lote que deseja alterar:  ")

    if  not verificar_existe( lotes, nome_lote):

        print("[yellow]Lote não encontrado no sistema![/yellow]\n")

        return


    atualizacao=input("O que você deseja atualizar: ").lower().strip()

    if atualizacao == "status":
        
        status_atual= [nome_lote]["status"]
        print(f"Status atual: {status_atual}")

        while True:
            novo_status= input("Digite o novo status desse lote: ")

            if verificar_status(novo_status):
                break
            else:
                print("Status inválido! Digite novamente\n")

        atualizar(nome_lote,lotes, atualizacao, novo_status,"lotes",animais)
        
        print("[green]Status atualizado![/green]")

    elif atualizacao == "preco":

        if lotes[nome_lote]["preco"] is None:
            print("[yellow]Esse Lote não está à venda![/yellow]\n")
        else:

            preco_atual = lotes[nome_lote]["preco"]

            print(f"Preço atual: {preco_atual}")

            novo_preco = float(input("Digite o novo preço do lote: "))

            while True:
                if verificar_preco(novo_preco):
                    break
                else:
                    print("Preço inválido! Digite novamente\n")

            atualizar(nome_lote, lotes,atualizacao, novo_preco,"lotes",animais)

            print("[green]Preço atualizado![/green]")

    elif atualizacao == "peso":

        peso_atual= lotes[nome_lote]["historico_peso"][-1].get("peso")

        print(f"Peso atual: {peso_atual}")


        novo_peso = float(input("Digite o novo peso: "))

        while True:
            if verificar_peso(novo_peso):
                break
            else:
                print("Peso inválido! Digite novamente\n")

        atualizar(nome_lote, lotes,atualizacao, novo_peso,"lotes",animais)

        print("[green]Peso médio atualizado![/green]")

    else:
        print("[red]Atualização inválida![/red]\n")


def atualizar_despesas(despesas: dict):
   
    if  not despesas:
        print("Cadastre suas despesas:")

        alimentacao_gastos = float(input("Quanto você gasta com alimentação?: "))
        controle_doencas_gastos = float(input("Quanto você gasta com para evitar e tratar doenças?: "))
        funcionarios_gastos = float(input("Quanto você gasta com os funcionários da sua fazenda?: "))
        infraestrutura_gastos = float(input("Quanto você gasta com a infraestrutura da sua fazenda?: "))

        despesas["alimentacao"] = alimentacao_gastos
        despesas["controle_doencas"] = controle_doencas_gastos
        despesas["funcionarios"] = funcionarios_gastos
        despesas["infraestrutura"] = infraestrutura_gastos
        
        with open("data/despesas.json", "w") as arquivo:
            json.dump(despesas, arquivo, indent=4)

        print("\n[green] Despesas cadastradas ![/green]")
        pausar()
        return
    
    mostrar_despesas(despesas)

    print("O que deseja alterar: ")

    print("1- Alimentação")
    print("2- Controle de doenças")
    print("3- Funcionarios")
    print("4- infraestrutura")

    opcao=int(input(">"))

    if opcao == 1:
        novo_valor= float(input("Digite o novo valor: "))

        despesas["alimentacao"] = novo_valor

        with open("data/despesas.json", "w") as arquivo:
            json.dump(despesas, arquivo, indent=4) 

        print("[green]Despesa atualizada![/green]")
        pausar()

    elif opcao == 2:
        novo_valor= float(input("Digite o novo valor: "))

        despesas["controle_doencas"] = novo_valor

        with open("data/despesas.json", "w") as arquivo:
            json.dump(despesas, arquivo, indent=4) 

        print("[green]Despesa atualizada![/green]")
        pausar()

    elif opcao == 3:
        novo_valor= float(input("Digite o novo valor: "))

        despesas["funcionarios"] = novo_valor

        with open("data/despesas.json", "w") as arquivo:
            json.dump(despesas, arquivo, indent=4) 
            
        print("[green]Despesa atualizada![/green]")
        pausar()

    elif opcao == 4:
        novo_valor= float(input("Digite o novo valor: "))

        despesas["infraestrutura"] = novo_valor

        with open("data/despesas.json", "w") as arquivo:
            json.dump(despesas, arquivo, indent=4) 

        print("[green]Despesa atualizada![/green]")
        pausar()


def Visualizar_valor_de_arroba_produzido(despesas: dict, historico_arroba_por_hectare_anual: list, animais: dict ):

    ano_atual = datetime.now().year

    arroba_total= analisar_ganho_peso_anual(animais) / 15.0



   

    if arroba_total > 0:
        
        custo_total= 0
        custo_total+=despesas["alimentacao"]
        custo_total+=despesas["controle_doencas"]
        custo_total+=despesas["funcionarios"]
        custo_total+=despesas["infraestrutura"]

        valor_arroba = round(custo_total / arroba_total, 2)

        print(f"[green]Você está produzindo {valor_arroba} R$ por arroba![/green]")

    else:
        print("[yellow]Dados insuficientes para se fazer a função![/yellow]")
        
    pausar()

def remover_animais(animais: dict):
    
    identificacao= input("Digite a identificação do animal que deseja remover: ")

    if  not verificar_existe( animais, identificacao):

        print("[yellow]Identificação não encontrada no sistema![/yellow]\n")
        return
    
    animais.pop(identificacao)
    print("[green]Animal removido![/green]")


def remover_lotes(lotes: dict, animais:dict):

    nome_lote= input("Digite o nome do lote que deseja remover: ")

    if  not verificar_existe( lotes, nome_lote):

        print("[yellow]Lote não encontrado no sistema![/yellow]\n")
        return
    
    lotes.pop(nome_lote)

    animais_para_remover=[]

    for animal in animais:
        if nome_lote in animal:
          animais_para_remover.append(animal)

    for animal in animais_para_remover:
        animais.pop(animal)
        
    print("[green]Lote removido![/green]")


def mostrar_Lotes (estoque: dict, identificacoes: list):
    tabela = Table(title="[white]  LOTES  [/white]", border_style="white")

    tabela.add_column("Nome", style="yellow", justify="center")
    tabela.add_column("Espécie", style="white")
    tabela.add_column("Raça", style="white")
    tabela.add_column("Quantidade", style="white")
    tabela.add_column("Peso Médio", style="white", justify="right")
    tabela.add_column("Status", style="red")
    tabela.add_column("Preço (R$)", style="green", justify="right")
   
    for identificacao in identificacoes:

        peso_atual= estoque[identificacao]["historico_peso"][-1].get("peso")


        tabela.add_row(
            identificacao.upper(),
            estoque[identificacao]["especie"].upper(),
            estoque[identificacao]["raca"].upper(),
            str(estoque[identificacao]["quantidade"]),
            str(peso_atual),
            estoque[identificacao]["status"],
            str(estoque[identificacao]["preco"]),
           
        )
    print("\n")
    print(tabela)

    pausar()


def mostrar_Animais (estoque: dict, identificacoes: list):
    tabela = Table(title="[white] ANIMAIS  [/white]", border_style="white")

    tabela.add_column("ID", style="yellow", justify="center")
    tabela.add_column("Espécie", style="white")
    tabela.add_column("Raça", style="white")
    tabela.add_column("Peso ", style="white", justify="right")
    tabela.add_column("Status", style="red")
    tabela.add_column("Preço (R$)", style="green", justify="right")
    tabela.add_column("Lote", style="white", justify="center")

    

    for identificacao in identificacoes:

        peso_atual= estoque[identificacao]["historico_peso"][-1].get("peso")


        tabela.add_row(
            identificacao,
            estoque[identificacao]["especie"].upper(),
            estoque[identificacao]["raca"].upper(),
            str(peso_atual),
            estoque[identificacao]["status"],
            str(estoque[identificacao]["preco"]),
            str(estoque[identificacao]["lote"])
        )

    print("\n")
    print(tabela)

    pausar()

def mostrar_produtos(produtos: dict):

    tabela = Table(title="[white] PRODUTOS [/white]", border_style="white")

    tabela.add_column("Nome", style="yellow", justify="center")
    tabela.add_column("Preço (R$)", style="green", justify="right")
    tabela.add_column("Peso", style="white", justify="right")
   
    for produto in produtos:
       tabela.add_row(
            produto.upper(),
            str(produtos[produto]["valor"]),
            str(produtos[produto]["peso"])
        )


    print("\n")
    print(tabela)

    pausar()

def mostrar_despesas(despesas: dict):

    tabela = Table(title="[white] Despesas [/white]", border_style="white")

    tabela.add_column("Alimentação", style="red", justify="center")
    tabela.add_column("Controle de doenças", style="red", justify="right")
    tabela.add_column("Funcionarios", style="red", justify="right")
    tabela.add_column("Infrestrutura", style="red", justify="right")
   
    tabela.add_row(
       str(despesas["alimentacao"]), 
       str(despesas["controle_doencas"]),
       str(despesas["funcionarios"]),
       str(despesas["infraestrutura"])
    )


    print("\n")
    print(tabela)

def mostrar_relatorio_geral(animais: dict, produtos: dict, producao_leite: dict):

    tabela = Table(title="[white] RELATORIO GERAL [/white]", border_style="white")

    tabela.add_column("Animais (lactação)", style="white", justify="center")
    tabela.add_column("Animais (a venda)", style="white", justify="right")
    tabela.add_column("Animais (engorda)", style="white", justify="right")
    tabela.add_column("Animais (gestação)", style="white", justify="right")
    tabela.add_column("Leite (litros)", style="white", justify="right")
    tabela.add_column("Queijo (kg)", style="white", justify="right")

    quantidade_lactacao= 0
    quantidade_a_venda= 0
    quantidade_engorda= 0
    quantidade_gestacao= 0

    for animal in animais:

        if animais[animal]["status"] == "lactacao":
            quantidade_lactacao+=1
        
        elif animais[animal]["status"] == "a venda":
            quantidade_a_venda+=1
        
        elif animais[animal]["status"] == "engorda":
            quantidade_engorda+=1

        elif animais[animal]["status"] == "gestacao":
            quantidade_gestacao+=1

    soma_leite = 0

    for animal in producao_leite:
        for registro in producao_leite[animal]:
            soma_leite += registro["quantidade_leite"]

    soma_queijo=0

    for produto in produtos:
        if "queijo" in produto:
            soma_queijo += produtos[produto]["peso"]


    tabela.add_row(
       str(quantidade_lactacao), 
       str(quantidade_a_venda),
       str(quantidade_engorda),
       str(quantidade_gestacao),
       str(soma_leite),
       str(soma_queijo)
    )

    print("\n")
    print(tabela)
    pausar()






def mostrar_menu_adm(animais: dict, lotes: dict, login: dict, producao_leite: dict, produtos: dict, despesas: dict,historico_arroba:list):

    limpar()

    while True:

        menu= """

    1- Cadastrar animais
    2- Buscar animais
    3- Atualizar animais
    4- Remover animais
    5- Visualizar estoque
    6- Registrar produção de leite
    7- Adicionar produtos fabricados
    8- Visualizar estoque de produtos
    9- Analisar produtividade ( com @ )
    10- Visualizar relatório geral da fazenda
    11- Atualizar despesas
    12- Visualizar valor de @ produzido
    0- Deslogar
    """


        print(Panel.fit(menu, title= "MENU ADM"))

        opcao= int(input(" >  "))

        if validar_opcao(opcao, 0 , 12):
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
            
            buscar_animais(animais)

        else:
           
            buscar_lotes(lotes)

       
    elif opcao == 3:

        while True:
            print("1- Atualizar Animal ")
            print("2- Atualizar Lote")

            opcao= int(input("> "))

            if validar_opcao(opcao,1,2):
                break
            else:
                print("[yellow]Opção invalida! Digite novamente[/yellow]\n")

        if opcao == 1:

            atualizar_animais(animais)
            
        else:

            atualizar_lotes(lotes,animais)



    elif opcao == 4:
        
        while True:
            print("1- Remover Animal ")
            print("2- Remover Lote")

            opcao= int(input("> "))

            if validar_opcao(opcao,1,2):
                break
            else:
                print("[yellow]Opção invalida! Digite novamente[/yellow]\n")

        if opcao == 1:

            remover_animais(animais)

        else:

            remover_lotes(lotes,animais)

    elif opcao == 5:

        while True:
            print("1- Mostrar estoque de animais ")
            print("2- Mostrar estoque de lotes")

            opcao= int(input("> "))

            if validar_opcao(opcao,1,2):
                break
            else:
                print("[yellow]Opção invalida! Digite novamente[/yellow]\n")


        if opcao == 1:

            identificacoes = list(animais.keys())

            mostrar_Animais(animais, identificacoes)

        else:

            identificacoes = list(lotes.keys())

            mostrar_Lotes(lotes,identificacoes)

    elif opcao == 6:

        registrar_producao_leite(producao_leite,animais)

    elif opcao == 7:

        cadastrar_produtos(produtos)

    elif opcao == 8:

        mostrar_produtos(produtos)

    elif opcao == 9:

        analisar_produtividade(animais,historico_arroba)

    elif opcao == 10:

        mostrar_relatorio_geral(animais,produtos,producao_leite)
        
    elif opcao == 12:

        atualizar_despesas(despesas)

    elif opcao == 13:

        Visualizar_valor_de_arroba_produzido(despesas,historico_arroba,animais)

                        
                        
      








       