
import defs.adm, defs.cliente, defs.geral

total_compra = 0
carrinho = []

agendar_data = []
agendar_hora = []

usuarios= []

login=[False, None]

animais=[]

produtos=[]

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
                    login=[True,tipo]
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

        print("=====MENU CLIENTE======\n")
        
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
            
            if opcao >=0 and opcao<=10:
                break
            else:
                print("Opção invalida! Digite novamente\n")


        if opcao == 0:
            print("Saindo...")
            
            login=[False, None]
   

    

        elif opcao == 1:
            for produto in produtos:

                print ("Nome:", produto[0]) 
                print ("Quantidade:", produto[1],"kg em estoque") 
                print ("Valor:", produto[2], "$\n") 

        

        elif opcao == 2:
            for animal in animais:

                if animal[2] == "a venda":

                    print ("Animal: ", animal[0]) 
                    print ("Raça: ", animal[3])
                    print("Preço: ", animal[4],"\n")


        elif opcao == 3:

            for lote in lotes:

                print ("Nome do lote: ", lote[0]) 
                print("Animais do lote: ", lote[1])
                print("Raça dos animais: ", lote[2])
                print("Status dos animais: ", lote[3])
                print ("Quantidade:", lote[4],"animais") 
                print ("Valor:",  lote[5], "$\n") 
            


        elif opcao == 4:
            compra = input("Qual produto deseja comprar: ").lower()
            
            encontrado = False

            for produto in produtos:
                
                if compra == produto[0]:

                    encontrado = True

                    quantidade = int(input(f"Digite quantos kilos de {compra} você  deseja comprar: "))

                    if produto[1] >= quantidade:
                        produto[1] -= quantidade
                        valor = produto[2] * quantidade
                        total_compra += valor
                        print(f"o valor da compra foi de: R$ {valor}")

                        carrinho.append ([compra, quantidade])
                        
                    else:
                        print("estoque insuficiente!")
                    break


        elif opcao == 5:
            compra = input("Qual animal deseja comprar: ").lower()

            encontrado= False

            identificacoes = []

            for animal in animais:

                if animal[0] == compra and animal[2] == "a venda":
                    encontrado = True

                    identificacoes.append(animal[1])


            if encontrado:
                print(f"Foram encontrados {len(identificacoes)} animais desse tipo: ")

                index = -1
                for animal in animais:

                    index+=1

                    if animal[1] in identificacoes:     

                        print("----------------------------")
                        print(f"{index} - {animal[0]} ")
                        print(f"Status: {animal[2]}")
                        print(f"Raça: {animal[3]} ")
                        print(f"Preço:  {animal[4]} $")
                        print("----------------------------")

                animal_comprado= int(input("Digite o numero do animal que deseja comprar "))

                animais[animal_comprado] [2] = "vendido"

                valor = animais[animal_comprado] [4]
                total_compra += valor

                carrinho.append([compra, 1])

                print(f"o valor da compra foi de: R$ {valor}")


        elif opcao == 6:
            compra = input("Qual lote deseja comprar: ").lower()
            
            encontrado = False

            for lote in lotes:
                
                if compra == lote[0]:

                    encontrado = True

                    valor = lote[5]

                    total_compra += valor

                    print(f"o valor da compra foi de: R$ {valor}")

                    carrinho.append ([compra, 1])
                        
                    break
        
        elif opcao == 7:
            print (f"o valor das compras estão em: R${total_compra}")

            for compra in carrinho:
                print(f"compras: {compra[0]} - {compra[1]}\n")
        
        
        
        elif opcao == 8:

            data = input("qual a data (ex: 12/04): ").lower()
            hora = input("qual a hora (ex: 15:30):").lower()

                    
            if len(data) != 5 or data[2] != "/":
                print("Formato de data inválido!")

            elif len(hora) != 5 or hora[2] != ":":
                print("Formato de hora inválido!")

            else:

                dia = int(data[0] + data[1])

                mes = int(data[3] + data[4])

                horas = int(hora[0] + hora[1])

                minutos = int(hora[3] + hora[4])

                if dia < 1 or dia > 31 or mes < 1 or mes > 12:
                    print("Data inválida!")

                elif horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
                    print("Hora inválida!")

                elif data in agendar_data and hora in agendar_hora:
                    print("Data e hora já estão ocupadas!")

                else:

                    agendar_data.append(data)
                    agendar_hora.append(hora)

                    print(f"Agendado para {dia}/{mes} às {horas}:{minutos}")
            
                    
        
        elif opcao == 9:
            print("\n===== AGENDA DE RETIRADAS =====")

            datas_mostradas = []

            for i in range(len(agendar_data)):
                if agendar_data[i] not in datas_mostradas:
                    print(f"\n{agendar_data[i]}:")

                for j in range(len(agendar_data)):
                    if agendar_data[j] == agendar_data[i]:
                        print(f" - {agendar_hora[j]}")

                datas_mostradas.append(agendar_data[i])


        elif opcao == 10:

            print("===== FORMAS DE PAGAMENTO =====")

            print("1 - PIX (DESCONTO DE 5%)")
            print("2 - CARTÃO (JUROS DE 5%)")
            print("3 - BOLETO (JUROS DE 1%)")

            opcao_pagamento = input("Qual a forma de pagamento: ")

            if opcao_pagamento == "1":

                desconto = total_compra * 0.05

                total_pix = total_compra - desconto

                print("PIX: 183.238.244-36")

                print(f"O desconto foi de R$ {desconto}")

                print(f"Valor final: R$ {total_pix}")

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

                    print(f"Pagamento aprovado!")

                    print(f"Juros cobrados: R$ {juros}")

                    print(f"Valor final: R$ {total_cartao}")

            elif opcao_pagamento == "3":

                juros = total_compra * 0.01

                total_boleto = total_compra + juros

                print("Boleto gerado com sucesso!")

                print(f"Juros cobrados: R$ {juros}")

                print(f"Valor final: R$ {total_boleto}")

            else:

                print("Opção inválida!")
                

                    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
