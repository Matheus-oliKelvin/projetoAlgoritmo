from colorama import Fore, Style, init
from tabulate import tabulate
from datetime import datetime
import os

try:
    from fpdf import FPDF
except ModuleNotFoundError:
    FPDF = None

try:
    import requests
except ModuleNotFoundError:
    requests = None


init(autoreset=True)


def mostrar_menu_cliente():
    print(Fore.CYAN + "=====MENU CLIENTE======\n")

    print("1 - Consultar produtos")
    print("2 - Consultar animais")
    print("3 - Consultar lotes")
    print("4 - Comprar produtos")
    print("5 - Comprar animais")
    print("6 - Comprar lotes")
    print("7 - Ver resumo das compras")
    print("8 - Agendar retirada")
    print("9 - Consultar agenda de retiradas")
    print("10  - Finalizar pagamento")
    print("0 - Encerrar sessão")

    while True:
        opcao = int(input("digite uma opção: "))

        if opcao >= 0 and opcao <= 10:
            return opcao

        print(Fore.RED + "Opção invalida! Digite novamente\n")


def consultar_produtos(produtos):
    tabela = []

    for produto in produtos:
        tabela.append([produto[0], f"{produto[1]} kg", f"R$ {produto[2]}"])

    if len(tabela) == 0:
        print(Fore.YELLOW + "Não existem produtos cadastrados.")
    else:
        print(tabulate(tabela, headers=["Produto", "Estoque", "Valor"], tablefmt="fancy_grid"))


def consultar_animais(animais):
    tabela = []

    for animal in animais:
        if animal[2] == "a venda":
            tabela.append([animal[0], animal[3], f"R$ {animal[4]}"])

    if len(tabela) == 0:
        print(Fore.YELLOW + "Não existem animais à venda.")
    else:
        print(tabulate(tabela, headers=["Animal", "Raça", "Preço"], tablefmt="fancy_grid"))


def consultar_lotes(lotes):
    tabela = []

    for lote in lotes:
        tabela.append([lote[0], lote[1], lote[2], lote[3], lote[4], f"R$ {lote[5]}"])

    if len(tabela) == 0:
        print(Fore.YELLOW + "Não existem lotes cadastrados.")
    else:
        print(tabulate(
            tabela,
            headers=["Lote", "Animal", "Raça", "Status", "Quantidade", "Valor"],
            tablefmt="fancy_grid"
        ))


def comprar_produto(produtos, carrinho, total_compra):
    compra = input("Qual produto deseja comprar: ").lower()

    for produto in produtos:
        if compra == produto[0]:
            quantidade = int(input(f"Digite quantos kilos de {compra} você deseja comprar: "))

            if produto[1] >= quantidade:
                produto[1] -= quantidade
                valor = produto[2] * quantidade
                total_compra += valor

                carrinho.append({
                    "item": compra,
                    "tipo": "produto",
                    "quantidade": quantidade,
                    "valor": valor
                })

                print(Fore.GREEN + f"o valor da compra foi de: R$ {valor}")
            else:
                print(Fore.RED + "estoque insuficiente!")
            break

    return total_compra


def comprar_animal(animais, carrinho, total_compra):
    compra = input("Qual animal deseja comprar: ").lower()
    identificacoes = []

    for animal in animais:
        if animal[0] == compra and animal[2] == "a venda":
            identificacoes.append(animal[1])

    if len(identificacoes) > 0:
        print(f"Foram encontrados {len(identificacoes)} animais desse tipo: ")

        index = -1
        for animal in animais:
            index += 1

            if animal[1] in identificacoes:
                print(tabulate(
                    [[index, animal[0], animal[2], animal[3], f"R$ {animal[4]}"]],
                    headers=["Nº", "Animal", "Status", "Raça", "Preço"],
                    tablefmt="fancy_grid"
                ))

        animal_comprado = int(input("Digite o numero do animal que deseja comprar "))
        animais[animal_comprado][2] = "vendido"

        valor = animais[animal_comprado][4]
        total_compra += valor

        carrinho.append({
            "item": compra,
            "tipo": "animal",
            "quantidade": 1,
            "valor": valor
        })

        print(Fore.GREEN + f"o valor da compra foi de: R$ {valor}")
    else:
        print(Fore.RED + "Animal não encontrado para venda.")

    return total_compra


def comprar_lote(lotes, carrinho, total_compra):
    compra = input("Qual lote deseja comprar: ").lower()

    for lote in lotes:
        if compra == lote[0]:
            valor = lote[5]
            total_compra += valor

            carrinho.append({
                "item": compra,
                "tipo": "lote",
                "quantidade": 1,
                "valor": valor
            })

            print(Fore.GREEN + f"o valor da compra foi de: R$ {valor}")
            break

    return total_compra


def ver_resumo_compras(carrinho, total_compra):
    print(Fore.CYAN + f"o valor das compras estão em: R${total_compra}")

    tabela = []

    for compra in carrinho:
        tabela.append([compra["item"], compra["tipo"], compra["quantidade"], f"R$ {compra['valor']}"])

    if len(tabela) == 0:
        print(Fore.YELLOW + "Carrinho vazio.")
    else:
        print(tabulate(tabela, headers=["Item", "Tipo", "Quantidade", "Valor"], tablefmt="fancy_grid"))
    

def gerar_recibo_pdf(cliente, carrinho, total_compra, data, hora):
    if FPDF is None:
        print(Fore.RED + "Pacote fpdf não instalado. Instale com: pip install fpdf")
        return None

    email_cliente = "não informado"

    if len(cliente) >= 3:
        email_cliente = cliente[2]

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


def gerar_recibo_carga(cliente, carrinho, total_compra, data, hora):
    email_cliente = "não informado"

    if len(cliente) >= 3:
        email_cliente = cliente[2]

    print(Fore.GREEN + "\n========== RECIBO / TICKET DE CARGA ==========")
    print(Fore.CYAN + "DADOS DO CLIENTE")
    print(f"E-mail: {email_cliente}")
    print("Tipo de usuário: cliente")

    print(Fore.CYAN + "\nITENS COMPRADOS")

    if len(carrinho) == 0:
        print(Fore.YELLOW + "Nenhum item comprado.")
    else:
        tabela = []

        for compra in carrinho:
            tabela.append([compra["item"], compra["tipo"], compra["quantidade"], f"R$ {compra['valor']}"])

        print(tabulate(tabela, headers=["Item", "Tipo", "Quantidade", "Valor"], tablefmt="fancy_grid"))

    print("---------------------------------------------")
    print(Fore.GREEN + f"Total da compra: R$ {total_compra}")
    print(f"Data da retirada: {data}")
    print(f"Hora da retirada: {hora}")
    print(Fore.GREEN + "==============================================\n")

    caminho_pdf = gerar_recibo_pdf(cliente, carrinho, total_compra, data, hora)

    if caminho_pdf is not None:
        print(Fore.GREEN + f"Recibo em PDF gerado: {caminho_pdf}")


def converter_data_para_api(data):
    dia = int(data[0] + data[1])
    mes = int(data[3] + data[4])
    ano_atual = datetime.now().year
    return f"{ano_atual}-{mes:02d}-{dia:02d}"


def buscar_coordenadas_cidade(cidade):
    if requests is None:
        print(Fore.RED + "Pacote requests não instalado. Instale com: pip install requests")
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
        print(Fore.RED + "Cidade não encontrada para consultar a previsão do tempo.")
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
        print(Fore.RED + "Não foi possível encontrar previsão para essa data.")
        return None

    print(Fore.CYAN + f"Previsão para {local['nome']} em {data}:")
    print(f"Chuva prevista: {chuva_mm if chuva_mm is not None else 0} mm")
    print(f"Chance máxima de chuva: {chance_chuva if chance_chuva is not None else 0}%")

    return (chuva_mm is not None and chuva_mm > 0) or (chance_chuva is not None and chance_chuva >= 50)


def agendar_retirada(agenda_retiradas, carrinho, total_compra, cliente):
    data = input("qual a data (ex: 12/04): ").lower()
    hora = input("qual a hora (ex: 15:30):").lower()
    cidade = input("qual a cidade da retirada: ").strip()

    if len(data) != 5 or data[2] != "/":
        print(Fore.RED + "Formato de data inválido!")
    elif len(hora) != 5 or hora[2] != ":":
        print(Fore.RED + "Formato de hora inválido!")
    else:
        dia = int(data[0] + data[1])
        mes = int(data[3] + data[4])
        horas = int(hora[0] + hora[1])
        minutos = int(hora[3] + hora[4])

        if dia < 1 or dia > 31 or mes < 1 or mes > 12:
            print(Fore.RED + "Data inválida!")
        elif horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
            print(Fore.RED + "Hora inválida!")
        elif data in agenda_retiradas and hora in agenda_retiradas[data]:
            print(Fore.RED + "Data e hora já estão ocupadas!")
        else:
            try:
                tem_chuva = verificar_chuva_na_data(cidade, data)
            except requests.RequestException:
                print(Fore.RED + "Não foi possível consultar o clima em tempo real.")
                return

            if tem_chuva is None:
                print(Fore.RED + "Retirada não agendada porque o clima não pôde ser verificado.")
                return

            if tem_chuva:
                print(Fore.RED + "Retirada não agendada: existe previsão de chuva para esse dia.")
                return

            if data not in agenda_retiradas:
                agenda_retiradas[data] = []

            agenda_retiradas[data].append(hora)

            print(Fore.GREEN + f"Agendado para {dia}/{mes} às {horas}:{minutos}")
            gerar_recibo_carga(cliente, carrinho, total_compra, data, hora)


def consultar_agenda_retiradas(agenda_retiradas):
    print(Fore.CYAN + "\n===== AGENDA DE RETIRADAS =====")

    tabela = []

    for data, horarios in agenda_retiradas.items():
        for hora in horarios:
            tabela.append([data, hora])

    if len(tabela) == 0:
        print(Fore.YELLOW + "Nenhuma retirada agendada.")
    else:
        print(tabulate(tabela, headers=["Data", "Hora"], tablefmt="fancy_grid"))


def finalizar_pagamento(total_compra):
    print(Fore.CYAN + "===== FORMAS DE PAGAMENTO =====")
    print("1 - PIX (DESCONTO DE 5%)")
    print("2 - CARTÃO (JUROS DE 5%)")
    print("3 - BOLETO (JUROS DE 1%)")

    opcao_pagamento = input("Qual a forma de pagamento: ")

    if opcao_pagamento == "1":
        desconto = total_compra * 0.05
        total_pix = total_compra - desconto

        print("PIX: 183.238.244-36")
        print(f"O desconto foi de R$ {desconto}")
        print(Fore.GREEN + f"Valor final: R$ {total_pix}")

    elif opcao_pagamento == "2":
        cartao = input("Número do cartão: ")
        cvc = input("CVC: ")
        validade = input("Validade (MM/AA): ")

        juros = total_compra * 0.05
        total_cartao = total_compra + juros

        if len(cartao) != 16:
            print(Fore.RED + "Cartão inválido!")
        elif len(cvc) != 3:
            print(Fore.RED + "CVC inválido!")
        elif len(validade) != 5:
            print(Fore.RED + "Formato da validade inválido!")
        else:
            print(Fore.GREEN + "Pagamento aprovado!")
            print(f"Juros cobrados: R$ {juros}")
            print(Fore.GREEN + f"Valor final: R$ {total_cartao}")

    elif opcao_pagamento == "3":
        juros = total_compra * 0.01
        total_boleto = total_compra + juros

        print(Fore.GREEN + "Boleto gerado com sucesso!")
        print(f"Juros cobrados: R$ {juros}")
        print(Fore.GREEN + f"Valor final: R$ {total_boleto}")

    else:
        print(Fore.RED + "Opção inválida!")
