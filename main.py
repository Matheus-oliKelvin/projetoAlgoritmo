produtos = [
    ["leite", 10, 20],
    ["queijo", 20, 10],
    ["soja", 5, 10],
    ["milho", 8, 30],
    ["ovos", 12, 40],
    ["mel", 25, 15]
]

animais = [
    ["vaca", 1000, 5, "nelore"],
    ["leitão", 300, 5, "piau"],
    ["ovelha", 350, 5, "dorper"],
    ["galinha", 50, 20, "caipira"],
    ["cabra", 280, 8, "saanen"],
    ["boi", 1800, 4, "angus"]
]

lotes = [
    [1, "vaca nelore", 20, 2000, "a venda"],
    [2, "galinha caipira", 30, 1200, "a venda"],
    [3, "ovelha dorper", 10, 3000, "a venda"],
    [4, "boi angus", 5, 8000, "em gestacao"]
]
total_compra = 0
carrinho = []

usuarios = [["a", "a", "cliente"]]
login = [False, None]

agendar_data = ["10.04"]
agendar_hora = ["12.22"]


while not login[0]:

    while True:
        print("\n Selecione a opção desejada: ")
        print("1- Login") 
        print("2- Cadastra-se")
        print("0- Sair")

        opcao = int(input(" digite a opção : "))

        if opcao >= 1 and opcao <= 3:
            break
        else:
            print("Opção invalida! Digite novamente\n")

    if opcao == 0:
        print("Saindo...")
        break

    elif opcao == 1:
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")
        tipo = input("Deseja entrar como admin ou cliente?: ").lower()

        encontrou = False

        for usuario in usuarios:
            if email == usuario[0] and senha == usuario[1] and tipo == usuario[2]:
                print("Seja bem-vindo(a) !")
                login = [True, tipo]
                encontrou = True
                break

        if not encontrou:
            print("E-mail ou senha incorretos ")

    elif opcao == 2:

        while True:
            email = input("Digite seu e-mail: ")

            for usuario in usuarios:
                if usuario[0] == email:
                    print("Esse e-mail já está cadastrado!Digite novamente")
                    verificador = False
                    break
                else:
                    verificador = True

            if "@" in email:
                verificador = True
            else:
                print("email inválido, falta o @:")
                verificador = False
                break

            if verificador:
                break

        while True:
            senha = input("Digite sua senha : ")
            confimarSenha = input("Digite sua senha novamente: ")

            if senha == confimarSenha:
                break
            else:
                print("As senhas não coecidem")

        while True:
            tipo = input("Você deseja se cadastrar como um CLIENTE ou ADM").lower()

            if tipo == "cliente" or tipo == "adm":
                break
            else:
                print("Nome invalido, tente novamente")

        usuarios.append([email, senha, tipo])
        print("Usuário cadastrado com sucesso!")

while login[0] and login[1] == "cliente":
    print ("=====MENU CLIENTE======\n")
    
    print("1 - Consultar produtos")
    print("2 - Consultar animais")
    print("3 - Realizar compra")
    print("4 - Ver resumo das compras")
    print("5 - Agendar retirada")
    print("6 - Consultar agenda")
    print("7 - comprar lotes")
    print("8 - Finalizar pagamento")
    print("0 - Encerrar sessão")
    
    opcao = input("digite uma opção: ")

    if opcao == "1":
        for produto in produtos:
            print ("Nome:", produto[0]) 
            print ("Preço:", produto[1],"$") 
            print ("Estoque:", produto[2], "em estoque") 
            print ("\n")
    
    elif opcao == "2":
        for animal in animais:
            print ("Animal:", animal[0]) 
            print ("Preço:", animal[1],"$") 
            print ("Estoque:", animal[2], "em estoque") 
            print ("Raça:", animal[3])
            print ("\n")
    
    elif opcao == "3":
        compra = input("O que deseja comprar: ").lower().strip()
        
        encontrado = False

        for produto in produtos:
            if compra == produto[0]:
                encontrado = True
                quantidade = int(input("diga a quantidade que deseja comprar: "))

                if produto[2] >= quantidade:
                    produto[2] -= quantidade
                    valor = produto[1] * quantidade
                    total_compra += valor
                    print(f"o valor da compra foi de: R$ {valor}")

                    carrinho.append ([compra, quantidade])
                    
                
                else:
                    print("estoque insuficiente!")
                break

        if not encontrado:
            for animal in animais:
                if compra == animal[0]:
                    encontrado = True
                    quantidade = int(input("diga a quantidade que deseja comprar: "))

                    if animal[2] >= quantidade:
                        animal[2] -= quantidade
                        valor = animal[1] * quantidade
                        total_compra += valor
                        print(f"o valor da compra foi de: R$ {valor}")
                        carrinho.append([compra, quantidade])
                    else:
                        print("estoque insuficiente!")
                    break

        if not encontrado:
            print("Não encontrado")

    
    elif opcao == "4":
        print (f"o valor das compras est?o em: R${total_compra}")

        if len(carrinho) == 0:
            print("nenhuma compra realizada")
        else:
            for carrin in carrinho:
                print(f"compras: {carrin[0]} - {carrin[1]}\n")

    elif opcao == "5":

        data = input("qual a data (ex: 12.04): ").strip()
        hora = input("qual a hora (ex: 15:30): ").strip()

        print("\n")

        dia = int(data[0:2])
        mes = int(data[3:5])

        horas = int(hora[0:2])
        minutos = int(hora[3:5])

        if dia < 1 or dia > 31 or mes < 1 or mes > 12:
            print("data invalida")

        elif horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
            print("hora invalida")

        elif data in agendar_data and hora in agendar_hora:
            print("Data e hora já estão ocupadas!")

        else:
            agendar_data.append(data)
            agendar_hora.append(hora)

            print(f"Agendado para {data} às {hora}")
                
    
    elif opcao == "6":
        print("\n===== AGENDA DE RETIRADAS =====")

        datas_mostradas = []

        for i in range(len(agendar_data)):
            if agendar_data[i] not in datas_mostradas:
                print(f"{agendar_data[i]}:")

            for j in range(len(agendar_data)):
                if agendar_data[j] == agendar_data[i]:
                    print(f" - {agendar_hora[j]}")

            datas_mostradas.append(agendar_data[i])

    elif opcao == "7":
        for lote in lotes:
            print("identificacao:", lote[0])
            print("lote:", lote[1])
            print("quantidade:", lote[2])
            print("valor:", lote[3])
            print("status:", lote[4])
            print()

        identificacao = int(input("qual o lote que deseja comprar diga a numeraçao? "))

        for lote in lotes:
            if identificacao == lote[0]:
                if lote[4] == "a venda":
                    total_compra += lote[3]
                    lote[4] = "vendido"
                    carrinho.append([lote[1], lote[2]])
                    print("lote comprado com sucesso!")
                else:
                    print("esse lote nao esta disponivel")

    elif opcao == "8":
        print ("=====FORMAS DE PAGAMENTO=====")
        print ("1 - PIX (DESCONTO DE 5%)")
        print ("2 - CARTÃO (JUROS DE 5%)")

        opcao_pagamento = (input ("qual a forma de pagamento: "))

        if opcao_pagamento == "1":
            desconto = total_compra * 0.05
            desconto_total_pix = total_compra - desconto
            print ("PIX: 183.238.244-36")
            print (f"O DESCONTO FOI DE {desconto} E SUAS COMPRAS FICARAM EM: R${desconto_total_pix}")
            
        elif opcao_pagamento == "2":
            cartao = input("numero do cartão: ").replace(" ", "")
            cvc = input("CVC: ")
            validade = input("validade (MM/AA): ")
        
            desconto2 = total_compra * 0.05
            desconto_total_cartao = total_compra + desconto2

            if len(cartao) != 16 or not cartao.isdigit():
                print("cartão invalido")

            elif len(cvc) != 3:
                print("CVC invalido")

            if len(validade) != 5 or validade[2] != "/":
                print("formato inválido!")
            else:
                dia = int(validade[0:2])
                mes = int(validade[3:5])

                if dia < 1 or dia > 31:
                    print ("dia invalido!")
                
                if mes < 1 or mes > 12:
                    print("mês inválido!")
                
                

                else:
                    print ("\n")
                    print(f"Pagamento aprovado! No valor de {desconto_total_cartao} e o juros cobrado foi de {desconto2}" )
                    break

        elif opcao == "0":
            print ("saindo...")
            break
