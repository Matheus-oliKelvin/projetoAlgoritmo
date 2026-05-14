
usuarios= [["1","1","adm"]]
login=[False, None]
animais=[]
produtos=[]
producao_leite = []
estoque_raca=[]


while not  login[0]:

    while True:
        print("Selecione a opção desejada: ")
        print("1- Login") 
        print("2- Cadastra-se  ")
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

       
        encontrou= False

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


while login[0] and login[1] == "adm":
    
    while True:
        print("\n Bem vindo Admin! Selecione a opção desejada: ")
        print("1- Cadastrar animais ") 
        print("2- Buscar animais ") 
        print("3- Atualizar animais ") 
        print("4- Remover animais")
        print("5- Visualizar estoque de animais")
        print("6- Registrar produção de leite")
        print("7- Adicionar produtos fabricados")
        print("8- Visualizar estoque de produtos")
        print("9- ###########")
        print("0- Sair")
        
        opcao= int(input(" digite a opção : "))

        if opcao >=0 and opcao<=9:
            break
        else:
            print("Opção invalida! Digite novamente\n")
             
    if opcao == 0:
        print("Saindo...")
        break
        

    elif opcao == 1:
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
        
        print("\nAnimal cadastrado!")
        animais.append([tipo_animal, identificacao, status, raca_animal])
 

    elif opcao == 2:
        identificacao_animal= input("Digite a identificação do animal que deseja buscar: ").lower()

        encontrado = False

        for animal in animais:
            if  identificacao_animal == animal[1]:
                print(animal[0], "encontrado! Status: ", animal[2])
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
            for animal in animais:
                print("----------------------------")
                print(f"{animal[0]} - {animal[1]}")
                print(f"status: {animal[2]}")
                print(f"raça: {animal[3]} ")
                print("----------------------------")
      
            
 
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
           nome_produto = input("Digite o nome do produto: ")
           peso_produto = float(input("Digite o peso do produto: "))
           valor_produto = float(input("Digite o valor de venda (por kg) do produto: "))

           produtos.append([nome_produto, peso_produto, valor_produto])

           print("Produto cadastrado!\n")

           continuar= int(input("Deseja adicionar outro produto? (1-sim) (0-não) :"))

           if continuar == 0:
               break



        



