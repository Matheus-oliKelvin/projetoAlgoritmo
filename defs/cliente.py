from colorama import Fore, Style, init
from tabulate import tabulate


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


def agendar_retirada(agenda_retiradas, carrinho, total_compra, cliente):
    data = input("qual a data (ex: 12/04): ").lower()
    hora = input("qual a hora (ex: 15:30):").lower()

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
