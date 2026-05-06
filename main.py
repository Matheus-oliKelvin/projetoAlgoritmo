produtos = [["leite", 10, 20], ["queijo", 20, 10], ["soja", 5, 10]]
animais = [["vacas", 1000, 5], ["leitoes", 300, 5], ["ovelhas", 350, 5]]

total_compra = 0

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

    print("\n1 - ver produtos")
    print("2 - ver animais")
    print("3 - comprar")
    print("4 - valor total das compras")
    print("5 - agendar retirada")
    print("6 - ver agenda de retiradas")
    print("0 - sair")
    
    opcao = input("digite uma opção: ")

    if opcao == "1":
        for produto in produtos:
            print ("Nome:", produto[0]) 
            print ("Preço:", produto[1],"$") 
            print ("Estoque:", produto[2], "em estoque") 
            print ("\n")
    
    elif opcao == "2":
        for animal in animais:
            print ("Nome:", animal[0]) 
            print ("Preço:", animal[1],"$") 
            print ("Estoque:", animal[2], "em estoque") 
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
                    else:
                        print("estoque insuficiente!")
                    break

        if not encontrado:
            print("Não encontrado")

    
    elif opcao == "5":
        
        data = input("qual a data (ex: 12.04): ").strip()
        hora = input("qual a hora (ex: 15.30): ").strip()
        print ("\n")
    

        if data in agendar_data and hora in agendar_hora:
            print("Data e hora já estão ocupadas!")
            print ("\n")
        else:
            agendar_data.append(data)
            agendar_hora.append(hora)

            print(f"Agendado para {data} às {hora}")
                
    
    elif opcao == "6":
        print("\n===== AGENDA =====")

        datas_mostradas = []

        for i in range(len(agendar_data)):
            if agendar_data[i] not in datas_mostradas:
                print(f"\n{agendar_data[i]}:")

            for j in range(len(agendar_data)):
                if agendar_data[j] == agendar_data[i]:
                    print(f" - {agendar_hora[j]}")

            datas_mostradas.append(agendar_data[i])

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    