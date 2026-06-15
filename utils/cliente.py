
from datetime import datetime
import os

from fpdf import FPDF

import requests
from utils.adm import *
from utils.geral import *



def mostrar_menu_cliente(animais:dict, lotes:dict, produtos: dict, carrinho: dict,usuarios:dict, agenda_retirada: dict):
   
    limpar()

    while True:
        menu= """
        1 - Consultar produtos
        2 - Consultar animais
        3 - Consultar lotes
        4 - Comprar produtos
        5 - Comprar animais
        6 - Comprar lotes
        7 - Ver resumo das compras
        8 - Agendar retirada
        9 - Consultar agenda de retiradas
        10  - Finalizar pagamento
        0 - Encerrar sessão

        """
      
    
        opcao = int(input(">"))

        if opcao >= 0 and opcao <= 10:
            break
        else:
            print("[yellow]Opção invalida! Digite novamente[/yellow]\n")


    if opcao == 0:
        print("Saindo...")
        pausar()
        login=[False, None]
    

    elif opcao == 1:
        mostrar_produtos(produtos)

    elif opcao == 2 :
        animais_a_venda=[]

        for animal in animais:
            if animal["status"] == "a venda":
                animais_a_venda.append(animal)


        mostrar_Animais(animais,animais_a_venda)

    elif opcao == 3:
        lotes_a_venda=[]

        for lote in lotes:
            if lote["status"] == "a venda":
                lotes_a_venda.append(lote)


        mostrar_Lotes(lotes,lotes_a_venda)


    elif opcao == 4:
        total_compra = comprar_produto(produtos,carrinho,total_compra)
    
    elif opcao == 5:
        total_compra = comprar_animal(animais,carrinho,total_compra)

    elif opcao == 6:
        total_compra = comprar_lote(lotes,carrinho,total_compra)

    elif opcao == 7:
        ver_resumo_compras(carrinho,total_compra)

    elif opcao == 8:
        agendar_retirada(agenda_retirada,carrinho,total_compra,usuarios)
    
    elif opcao == 9:
        consultar_agenda_retiradas(agenda_retirada)

    elif opcao == 10:
        finalizar_pagamento(total_compra)
    


def comprar_produto(produtos:dict, carrinho:list,total_compra: float):
    compra = input("Qual produto deseja comprar: ").lower()


    for produto in produtos:
        if compra == produto:
            quantidade = int(input(f"Digite quantos kilos de {compra} você deseja comprar: "))

            if produto["peso"] >= quantidade:
                produto["peso"] -= quantidade
                valor = produto["valor"] * quantidade
                total_compra += valor

                carrinho.append({
                    "item": compra,
                    "tipo": "produto",
                    "quantidade": quantidade,
                    "valor": valor
                })

                print( f"o valor da compra foi de: R$ {valor}")
            else:
                print("[red] estoque insuficiente! [/red]")
            break
    
    pausar()
    return total_compra


def comprar_animal(animais:dict, carrinho: list,total_compra:float):
    compra = input("Qual especie de animal deseja comprar: ").lower()
    identificacoes = []

    total_compra= 0
    
    for animal in animais:
        if animal["especie"] == compra and animal["status"] == "a venda":
            identificacoes.append(animal)

    if len(identificacoes) > 0:
        print(f"Foram encontrados {len(identificacoes)} animais desse tipo: ")

        mostrar_Animais(animais,identificacoes)


        animal_comprado = int(input("Digite a identificação do animal que deseja comprar "))
        animais[animal_comprado]["status"] = "vendido"

        valor = animais[animal_comprado]["preco"]
        total_compra += valor

        carrinho.append({
            "item": compra,
            "tipo": "animal",
            "quantidade": 1,
            "valor": valor
        })

        print("[green]o valor da compra foi de: R$ {valor}[/green]")
    else:
        print("[red]Animal não encontrado para venda.[/red]")

    pausar()
    return total_compra


def comprar_lote(lotes:dict, carrinho:list, total_compra:float):
    compra = input("Qual lote deseja comprar: ").lower()

    for lote in lotes:
        if compra == lote:
            valor = lote["preco"]
            total_compra += valor

            carrinho.append({
                "item": compra,
                "tipo": "lote",
                "quantidade": 1,
                "valor": valor
            })

            print(f"[green]o valor da compra foi de: R$ {valor}[/green]")
            break
    
    pausar()
    return total_compra


def ver_resumo_compras(carrinho:list, total_compra):
    print( f"o valor das compras estão em: R${total_compra}")

   
    tabela = Table(title="[white] CARRINHO [/white]", border_style="white")

    tabela.add_column("Item", style="white", justify="center")
    tabela.add_column("Tipo de compra", style="white", justify="right")
    tabela.add_column("Quantidade", style="white", justify="right")
    tabela.add_column("Preço (R$)", style="green", justify="right")

   
   
    for compra in carrinho:
       
       tabela.add_row(
            compra["item"],
            compra["tipo"],
            compra["quantidade"],
            str(compra["valor"])
        )


    pausar()
    

def gerar_recibo_pdf(usuario, carrinho, total_compra, data, hora):
    

    email_cliente = "não informado"

    if len(usuario) >= 3:
        email_cliente = usuario["usuario"]

    os.makedirs("recibos", exist_ok=True)
    data_arquivo = datetime.now().strftime("%Y%m%d_%H%M%S")
    caminho_pdf = os.path.join("recibos", f"recibo_carga_{data_arquivo}.pdf")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "RECIBO / TICKET DE CARGA", ln=True, align="C")
    pdf.ln(5)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "DADOS DO CLIENTE", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"E-mail: {email_cliente}", ln=True)
    pdf.cell(0, 8, "Tipo de usuario: cliente", ln=True)
    pdf.ln(4)

    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, "ITENS COMPRADOS", ln=True)

    pdf.set_font("Arial", "B", 10)
    pdf.cell(60, 8, "Item", border=1)
    pdf.cell(40, 8, "Tipo", border=1)
    pdf.cell(35, 8, "Quantidade", border=1)
    pdf.cell(45, 8, "Valor", border=1, ln=True)

    pdf.set_font("Arial", "", 10)

    if len(carrinho) == 0:
        pdf.cell(180, 8, "Nenhum item comprado.", border=1, ln=True)
    else:
        for compra in carrinho:
            pdf.cell(60, 8, str(compra["item"]), border=1)
            pdf.cell(40, 8, str(compra["tipo"]), border=1)
            pdf.cell(35, 8, str(compra["quantidade"]), border=1)
            pdf.cell(45, 8, f"R$ {compra['valor']}", border=1, ln=True)

    pdf.ln(6)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 8, f"Total da compra: R$ {total_compra}", ln=True)
    pdf.set_font("Arial", "", 11)
    pdf.cell(0, 8, f"Data da retirada: {data}", ln=True)
    pdf.cell(0, 8, f"Hora da retirada: {hora}", ln=True)

    pdf.output(caminho_pdf)
    return caminho_pdf


def gerar_recibo_carga(usuario, carrinho, total_compra, data, hora):
    email_cliente = "não informado"

    if len(usuario) >= 3:
        email_cliente = usuario["usuario"]

    print("\n[green]========== RECIBO / TICKET DE CARGA ==========[/green]")
    print("DADOS DO CLIENTE")
    print(f"E-mail: {email_cliente}")
    print("Tipo de usuário: cliente")

    print("\nITENS COMPRADOS")

    if len(carrinho) == 0:
        print( "[yellow]Nenhum item comprado.[/yellow]")
    else:
        tabela = []

        for compra in carrinho:
            tabela.append([compra["item"], compra["tipo"], compra["quantidade"], f"R$ {compra['valor']}"])

        ver_resumo_compras(carrinho,total_compra)

    print("---------------------------------------------")
    print(f"[green]Total da compra: R$ {total_compra}[/green]")
    print(f"Data da retirada: {data}")
    print(f"Hora da retirada: {hora}")
    print( "==============================================\n")

    caminho_pdf = gerar_recibo_pdf(cliente, carrinho, total_compra, data, hora)

    if caminho_pdf is not None:
        print(f"[green]Recibo em PDF gerado: {caminho_pdf}[/green]")


def converter_data_para_api(data):
    dia = int(data[0] + data[1])
    mes = int(data[3] + data[4])
    ano_atual = datetime.now().year
    return f"{ano_atual}-{mes:02d}-{dia:02d}"


def buscar_coordenadas_cidade(cidade):
    if requests is None:
        print("[red]Pacote requests não instalado. Instale com: pip install requests[/red]")
        return None

    resposta = requests.get(
        "https://geocoding-api.open-meteo.com/v1/search",
        params={
            "name": cidade,
            "count": 1,
            "language": "pt",
            "format": "json"
        },
        timeout=10
    )
    resposta.raise_for_status()

    dados = resposta.json()

    if "results" not in dados or len(dados["results"]) == 0:
        return None

    cidade_encontrada = dados["results"][0]

    return {
        "nome": cidade_encontrada["name"],
        "latitude": cidade_encontrada["latitude"],
        "longitude": cidade_encontrada["longitude"]
    }


def verificar_chuva_na_data(cidade, data):
    local = buscar_coordenadas_cidade(cidade)

    if local is None:
        print("[red]Cidade não encontrada para consultar a previsão do tempo.[/red]")
        return None

    data_api = converter_data_para_api(data)

    resposta = requests.get(
        "https://api.open-meteo.com/v1/forecast",
        params={
            "latitude": local["latitude"],
            "longitude": local["longitude"],
            "daily": "precipitation_sum,precipitation_probability_max",
            "timezone": "America/Sao_Paulo",
            "start_date": data_api,
            "end_date": data_api
        },
        timeout=10
    )
    resposta.raise_for_status()

    dados = resposta.json()
    previsao_diaria = dados.get("daily", {})
    chuva_mm = previsao_diaria.get("precipitation_sum", [None])[0]
    chance_chuva = previsao_diaria.get("precipitation_probability_max", [None])[0]

    if chuva_mm is None and chance_chuva is None:
        print("[red]Não foi possível encontrar previsão para essa data.[/red]")
        return None

    print( f"Previsão para {local['nome']} em {data}:")
    print(f"Chuva prevista: {chuva_mm if chuva_mm is not None else 0} mm")
    print(f"Chance máxima de chuva: {chance_chuva if chance_chuva is not None else 0}%")

    return (chuva_mm is not None and chuva_mm > 0) or (chance_chuva is not None and chance_chuva >= 50)


def agendar_retirada(agenda_retiradas, carrinho, total_compra, cliente):
    data = input("qual a data (ex: 12/04): ").lower()
    hora = input("qual a hora (ex: 15:30):").lower()
    cidade = input("qual a cidade da retirada: ").strip()

    if len(data) != 5 or data[2] != "/":
        print("[red]Formato de data inválido![/red]")
    elif len(hora) != 5 or hora[2] != ":":
        print("[red]Formato de hora inválido![/red]")
    else:
        dia = int(data[0] + data[1])
        mes = int(data[3] + data[4])
        horas = int(hora[0] + hora[1])
        minutos = int(hora[3] + hora[4])

        if dia < 1 or dia > 31 or mes < 1 or mes > 12:
            print("[red]Data inválida![/red]")
        elif horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
            print("[red]Hora inválida![/red]")
        elif data in agenda_retiradas and hora in agenda_retiradas[data]:
            print("[red]Data e hora já estão ocupadas![/red]")
        else:
    
            tem_chuva = verificar_chuva_na_data(cidade, data)
          

            if tem_chuva is None:
                print("[red]Retirada não agendada porque o clima não pôde ser verificado.[/red]")
                return

            if tem_chuva:
                print("[red]Retirada não agendada: existe previsão de chuva para esse dia.[/red]")
                return

            if data not in agenda_retiradas:
                agenda_retiradas[data] = []

            agenda_retiradas[data].append(hora)

            print(f"[green]Agendado para {dia}/{mes} às {horas}:{minutos}[/green]")
            gerar_recibo_carga(cliente, carrinho, total_compra, data, hora)

    pausar()

def consultar_agenda_retiradas(agenda_retiradas):
    tabela = Table(title="[white] AGENDA DE RETIRADAS  [/white]", border_style="white")

    tabela.add_column("Data", style="white", justify="center")
    tabela.add_column("Hora", style="white", justify="right")

    for data, horarios in agenda_retiradas.items():
        for horario in horarios:
            tabela.add_row(
                data,
                horario
            )
    
    pausar()

def finalizar_pagamento(total_compra):
    print( "===== FORMAS DE PAGAMENTO =====")
    print("1 - PIX (DESCONTO DE 5%)")
    print("2 - CARTÃO (JUROS DE 5%)")
    print("3 - BOLETO (JUROS DE 1%)")

    opcao_pagamento = input("Qual a forma de pagamento: ")

    if opcao_pagamento == "1":
        desconto = total_compra * 0.05
        total_pix = total_compra - desconto

        print("PIX: 183.238.244-36")
        print(f"O desconto foi de R$ {desconto}")
        print(f"[green]Valor final: R$ {total_pix}[/green]")

    elif opcao_pagamento == "2":
        cartao = input("Número do cartão: ")
        cvc = input("CVC: ")
        validade = input("Validade (MM/AA): ")

        juros = total_compra * 0.05
        total_cartao = total_compra + juros

        if len(cartao) != 16:
            print("Cartão inválido!")
        elif len(cvc) != 3:
            print("CVC inválido!")
        elif len(validade) != 5:
            print("Formato da validade inválido!")
        else:
            print("Pagamento aprovado!")
            print(f"Juros cobrados: R$ {juros}")
            print("Valor final: R$ {total_cartao}")

    elif opcao_pagamento == "3":
        juros = total_compra * 0.01
        total_boleto = total_compra + juros

        print("Boleto gerado com sucesso!")
        print(f"Juros cobrados: R$ {juros}")
        print("Valor final: R$ {total_boleto}")

    else:
        print("Opção inválida!")
    
    pausar()
