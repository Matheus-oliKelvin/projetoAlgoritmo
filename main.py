
import defs.adm, defs.cliente, defs.geral

total_compra = 0
carrinho = []

agenda_retiradas = {}

usuarios= []

login=[False, None]

animais=[]

produtos=[["leite", 5, 10]]

producao_leite = []

lotes=[]


while True:

    if not login[0]:

        while True:
            print("Selecione a opção desejada: ")
            print("1- Login") 
            print("2- Cadastra-se")
            print("0- Sair")

            opcao= int(input("Digite a opção : "))

            if opcao >=0 and opcao<=2:
                break
            else:
                print("Opção invalida! Digite novamente\n")

        if opcao == 0:
            print("Saindo...")
            break


        elif opcao == 1:
            email= input("Digite seu e-mail: ")
            senha= input("Digite sua senha: ")
            tipo= input("Deseja entrar como (cliente) ou (adm)?: ").lower()

            encontrou = False

            for usuario in usuarios:
                if email == usuario[0] and senha == usuario[1] and tipo == usuario[2]:
                    print("Seja bem-vindo(a) !")
                    print("---------------------------------------------")
                    login=[True,tipo,email]
                    encontrou=True
                    break

            if not encontrou:
                print("Credenciais incorretas!\n ")

        elif opcao == 2:

            while True: 
                email_existe= False
                email_invalido=False

                email= input("Digite seu e-mail: ")
                
                for usuario in usuarios:
                    if usuario[0] == email:
                        print("Esse e-mail já está cadastrado!Digite novamente\n ")
                        email_existe= True
                        break
                    
                if "@" not in email or ".com" not in email:
                    print("email inválido! Digite novamente\n ")
                    email_invalido= True
                
                if  not email_invalido and not email_existe :
                    break

            while True:
                senha= input("Digite sua senha : ")
                confimar_senha= input("Digite sua senha novamente: ")

                if senha == confimar_senha:
                    break
                else:
                    print("As senhas não coincidem! Digite novamente\n")

            while True:
                tipo= input("Você deseja se cadastrar como um (cliente) ou (adm): ").lower()

                if tipo == "cliente" or tipo =="adm":
                    break
                else:
                    print("Nome invalido, tente novamente\n")

            
            usuarios.append([email, senha, tipo]) 
            print("Usuário cadastrado com sucesso! \n")


    elif login[0] and login[1] == "adm":
        
        while True:

            print("=====MENU ADM======\n")

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
            
            opcao= int(input(" digite a opção : "))

            if opcao >=0 and opcao<=9:
                break
            else:
                print("Opção invalida! Digite novamente\n")
                
        if opcao == 0:
            print("Saindo...")
            login=[False, None]
            
        elif opcao == 1:
            
            while True:
                print("0- Cadastrar animal único")
                print("1- Cadastrar por Lote")

                opcao= int(input("Digite a opção desejada: "))

                if opcao >=0 and opcao<=1:
                    break
                else:
                    print("Opção invalida! Digite novamente\n")

            if opcao == 0:
                tipo_animal= input("Qual o tipo do animal: ").lower()
                raca_animal= input("Qual a raça do animal: ").lower()

                while True:
                    identificacao = input("Digite a identificação desse animal: ").lower()

                    ja_existe= False

                    for animal in animais:

                        if identificacao == animal[1]:
                            print("Essa identificação já está cadastrada!Digite novamente\n")
                            ja_existe= True
                            break

                    if not ja_existe:
                        break

                while True:
                    status= input("Qual o status desse animal: ").lower()

                    if status not in ["a venda", "lactacao", "engorda", "gestacao", "postura"]:
                        print("Status inválido! Digite novamente\n")
                    else:
                        break
                
                if status == "a venda":
                    preco= float(input("Digite o preço desse animal: "))
                else:
                    preco= None

                print("\nAnimal cadastrado!")

                animais.append([tipo_animal, identificacao, status, raca_animal, preco])

            else:

                while True:
                    nome_lote=input("Digite o nome desse lote: ")

                    ja_existe = False

                    for lote in lotes:
                        if nome_lote == lote[0]:
                            print("O nome desse lote já está cadastrado! Digite novamente\n")
                            ja_existe = True
                            break
                    
                    if not ja_existe:
                        break

                tipo_lote = input(f"Digite o tipo de animais do lote { nome_lote}: ")

                raca_lote=input(f"Digite a raça dos animais do lote { nome_lote}: ")

                while True:
                    status_lote= input(f"Digite o status dos animais do lote { nome_lote}: ").lower()

                    if status_lote not in ["a venda", "lactacao", "engorda", "gestacao", "postura"]:
                        print("Status inválido! Digite novamente\n")
                    else:
                        break

                quantidade_lote = int(input(f"Digite a quantidade de animais do lote { nome_lote}:"))

                preco_lote = float(input(f"Digite o preço do lote { nome_lote}: "))

                lotes.append([nome_lote,tipo_lote,raca_lote ,status_lote,quantidade_lote,preco_lote])
                print("\nLote cadastrado!")


        elif opcao == 2:
            identificacao_animal= input("Digite a identificação do animal que deseja buscar: ").lower()

            encontrado = False

            for animal in animais:
                if  identificacao_animal == animal[1]:
                    print(animal[0], "encontrado! Status: ", animal[2])
                    
                    if animal[2] == "a venda":
                        print("Preço:", animal[4], "$")

                    encontrado=True
                    break

            if not encontrado:
                print("\nAnimal não encontrado no sistema!")


        elif opcao == 3:
            identificacao_animal= input("Digite a identificação do animal que deseja alterar: ").lower()

            encontrado = False

            index= -1

            for animal in animais:
                index +=1

                if  identificacao_animal == animal[1]:
                    encontrado=True
                    status_atual= animal[2]
                    break
            
            if  encontrado:
                print("Status atual: ", status_atual)

                while True:
                    status_atualizado= input("Digite o novo status:").lower()

                    if status_atualizado not in ["a venda", "lactacao", "engorda", "gestacao", "postura"]:
                        print("Status inválido! Digite novamente\n")
                    else:
                        break

                animais[index][2] = status_atualizado
                print("\nStatus atualizado!")

            else:
                print("\nAnimal não encontrado no sistema!")

            
        elif opcao == 4:
            identificacao_animal= input("Digite a identificação do animal que deseja remover: ").lower()

            encontrado = False

            index= -1

            for animal in animais:
                index +=1
                if  identificacao_animal == animal[1]:
                    encontrado=True
                    break

            if encontrado:
                animais.pop(index)

                print("\nAnimal removido do sistema!")

            else:
                print("\nAnimal não encontrado no sistema!") 

        elif opcao == 5:
            print("Como você deseja visualizar o estoque dos animais: ")
            print(" 1 - Visualizar todos os animais")
            print(" 2 - Visualizar por status")
            print(" 3 - Visualizar por lote")
            print(" 4 - Visualizar por tipo de animal")

            opcao = int(input("Digite a opção desejada: "))

            if opcao == 1:

                contador = 0

                for animal in animais:

                    contador+=1

                    print("----------------------------")
                    print(f"{animal[0]} - {animal[1]}")
                    print(f"Status: {animal[2]}")
                    print(f"Raça: {animal[3]} ")
                    
                    if animal[2] == "a venda":
                        print(f"Preço:  {animal[4]} $")

                    print("----------------------------")

                
                if contador == 0:
                    print("\nNão existe animais cadastrados no sistema!") 

            elif opcao == 2:
                status=input("Deseja ver o estoque de animais em que status?: ").lower()

                contador = 0

            for animal in animais:
                
                if animal[2] == status:

                    contador+=1

                    print("----------------------------")
                    print(f"{animal[0]} - {animal[1]}")
                    print(f"Status: {animal[2]}")
                    print(f"Raça: {animal[3]} ")
                    if animal[2] == "a venda":
                        print(f"Preço:  {animal[4]} $")

                    print("----------------------------")

            if contador == 0:
                print("\nNão existe animais com esse status no sistema!") 

            elif opcao == 3:

                contador = 0

                for lote in lotes:

                    contador +=1

                    print("----------------------------")
                    print(f"Lote {lote[0]}")
                    print(f"{lote[4]} {lote[1]}")
                    print(f"Raça: {lote[2]} ")
                    print(f"Status: {lote[3]}")
                    print(f"Preço: {lote[5]} $")
                    print("----------------------------")

                if contador == 0:
                    print("\nNão existe lotes no sistema!") 

            elif opcao == 4:
                tipo_animal=input("Deseja ver o estoque de qual tipo de animal: ").lower()

                contador = 0

            for animal in animais:
                
                if animal[0] == tipo_animal:

                    contador+=1

                    print("----------------------------")
                    print(f"{animal[0]} - {animal[1]}")
                    print(f"Status: {animal[2]}")
                    print(f"Raça: {animal[3]} ")
                    if animal[2] == "a venda":
                        print(f"Preço:  {animal[4]} $")

                    print("----------------------------")

            if contador == 0:
                print("\nNão existe animais com esse tipo no sistema!") 

            else:
                print("\nOpção inválida !")       

            
            
        
                
    
        elif opcao == 6:
            verificador = 0 

            for animal in animais:

                ja_registrado = False

                for leite in producao_leite:

                    if animal[1] == leite[0]:
                        ja_registrado = True
                        break

                if animal[2] == "lactacao" and not ja_registrado:

                    leite_produzido = int(input(f"Digite a produção de leite diária do animal {animal[1]}: "))

                    producao_leite.append([animal[1], leite_produzido])
                    print(f"\nProdução de leite do animal {animal[1]} registrada!")

                else:
                    verificador += 1

            if verificador >= len(animais):
                print("\nNão existe animais disponíveis para a registração")

        elif opcao == 7:

            while True:
                nome_produto = input("Digite o nome do produto: ").lower()
                peso_produto = float(input("Digite o peso do produto: "))
                valor_produto = float(input("Digite o valor de venda (por kg) do produto: "))

                produtos.append([nome_produto, peso_produto, valor_produto])

                print("Produto cadastrado!\n")

                continuar= int(input("Deseja adicionar outro produto? (1-sim) (0-não) :"))

                if continuar == 0:
                    break
            

        elif opcao == 8:
            print("Como você deseja visualizar o estoque dos produtos: ")
            print(" 1 - Visualizar todos os produtos")
            print(" 2 - Visualizar por tipo de produto")
            
            opcao = int(input("Digite a opção desejada: "))

            if opcao == 1:
                for produto in produtos:
                    print("----------------------------")
                    print(f"{produto[0]} ")
                    print(f"peso: {produto[1]}")
                    print(f"valor de venda ( por kg): {produto[2]} ")
                    print("----------------------------")

            elif opcao == 2:
                nome_produto=input("Qual o tipo de produto que você deseja ver o estoque?: ").lower()

                contador =0

            for produto in produtos:
                
                if produto[0] == nome_produto:

                    contador+=1

                    print("----------------------------")
                    print(f" {contador}. {produto[0]} ")
                    print(f"peso: {produto[1]}")
                    print(f"valor de venda ( por kg): {produto[2]} ")
                    print("----------------------------")

            if contador == 0:
                print("\nNão existe produtos desse tipo no estoque!")

            else:
                print("\nOpção inválida !")  

        elif opcao == 9:
            hectares = float(input("Você tem quantos hectares na sua fazenda?: "))
            quantidade_animais= int(input("Você tem quantos animais na sua fazenda?: "))
            peso_inicial = float(input("No começo do ano qual era o peso médio dos seus animais?: (em kg) "))
            peso_final = float(input("No final do ano qual era o peso médio dos seus animais?: (em kg) "))

            ganho_por_animal= peso_final - peso_inicial

            ganho_peso_total = quantidade_animais * ganho_por_animal

            arroba_total = ganho_peso_total / 15.0

            arroba_por_hectare_anual = round(arroba_total/ hectares, 2)

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

            if ganho_por_animal > 0:
                opcao = int(input("Deseja ver o valor de @ produzido ? (1-sim) (0-não) : ")) 

                if opcao == 1 :
                    alimentacao_gastos = float(input("Quanto você gasta com alimentação?: "))
                    controle_doencas_gastos = float(input("Quanto você gasta com para evitar e tratar doenças?: "))
                    funcionarios_gastos = float(input("Quanto você gasta com os funcionários da sua fazenda?: "))
                    infraestrutura_gastos = float(input("Quanto você gasta com a infraestrutura da sua fazenda?: "))

                    custos = alimentacao_gastos + controle_doencas_gastos + funcionarios_gastos + infraestrutura_gastos

                    valor_arroba = round(custos / arroba_total, 2)

                    print(f"Você está produzindo {valor_arroba} R$ por arroba!")

                

        

    elif login[0] and login[1] == "cliente":

        opcao = defs.cliente.mostrar_menu_cliente()

        if opcao == 0:
            print("Saindo...")
            login=[False, None]

        elif opcao == 1:
            defs.cliente.consultar_produtos(produtos)

        elif opcao == 2:
            defs.cliente.consultar_animais(animais)

        elif opcao == 3:
            defs.cliente.consultar_lotes(lotes)

        elif opcao == 4:
            total_compra = defs.cliente.comprar_produto(produtos, carrinho, total_compra)

        elif opcao == 5:
            total_compra = defs.cliente.comprar_animal(animais, carrinho, total_compra)

        elif opcao == 6:
            total_compra = defs.cliente.comprar_lote(lotes, carrinho, total_compra)
        
        elif opcao == 7:
            defs.cliente.ver_resumo_compras(carrinho, total_compra)
        
        elif opcao == 8:
            defs.cliente.agendar_retirada(agenda_retiradas, carrinho, total_compra, login)
        
        elif opcao == 9:
            defs.cliente.consultar_agenda_retiradas(agenda_retiradas)

        elif opcao == 10:
            defs.cliente.finalizar_pagamento(total_compra)
