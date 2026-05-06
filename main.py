
usuarios= []
login=[False, None]
animais=[]
produtos=[]
producao_Leite = []

while not login[0]:

    while True:
        print("\n Selecione a opção desejada: ")
        print("1- Login") 
        print("2- Cadastra-se  ")
        print("0- Sair")

        opcao= int(input(" digite a opção : "))

        if opcao >=1 and opcao<=3:
            break
        else:
            print("Opção invalida! Digite novamente\n")


    if opcao == 0:
        print("Saindo...")
        break


    elif opcao == 1:
        email= input("Digite seu e-mail: ")
        senha= input("Digite sua senha: ")
        tipo= input("Deseja entrar como admin ou cliente?: ").lower()

       
        encontrou= False

        for usuario in usuarios:
            if email == usuario[0] and senha == usuario[1] and tipo == usuario[2]:
                print("Seja bem-vindo(a) !")
                login=[True,tipo]
                encontrou=True
                break

        if not encontrou:
            print("E-mail ou senha incorretos ")


    elif opcao == 2:

        while True: 
            email_existe= False
            email_invalido=False

            email= input("Digite seu e-mail: ")
            
            for usuario in usuarios:
                if usuario[0] == email:
                    print("Esse e-mail já está cadastrado!Digite novamente")
                    email_existe= True
                    break
                   
            if "@" not in email:
                print("email inválido, falta o @! Digite novamente")
                email_invalido= True
              
            if  not email_invalido and not email_existe :
                    break

        while True:
            senha= input("Digite sua senha : ")
            confimarSenha= input("Digite sua senha novamente: ")
            if senha == confimarSenha:
                break
            else:
                print("As senhas não coecidem")

        while True:
            tipo= input("Você deseja se cadastrar como um CLIENTE ou ADM").lower()
            if tipo == "cliente" or tipo =="adm":
                break
            else:
                print("Nome invalido, tente novamente")

        
        usuarios.append([email, senha, tipo]) 
        print("Usuário cadastrado com sucesso!")


while login[0] and login[1] == "adm":
    
    while True:
        print("\n Bem vindo Admin! Selecione a opção desejada: ")
        print("1- Cadastrar Animais ") 
        print("2- Buscar Animais ") 
        print("3- Atualizar Animais ") 
        print("4- Remover Animais")
        print("5- Registrar produção de leite")
        print("6- Adcionar produtos fabricados")
        print("7- ###########")
        print("0- Sair")
        
        opcao= int(input(" digite a opção : "))

        if opcao >=1 and opcao<=7:
            break
        else:
            print("Opção invalida! Digite novamente\n")
            
    if opcao == 0:
        print("Saindo...")
        break
        

    elif opcao == 1:
        tipoAnimal= input("Qual o tipo do animal: ").lower()
        racaAnimal= input("Qual a raça do animal: ").lower()
        identificador = input(f"Digite a identificação desse {tipoAnimal} ").lower()


        while True:
            status= input("Qual o status desse animal:")

            if status not in ("a venda", "lactacao", "engorda"):
                print("Status inválido! Digite novamente ")
            else:
                break
        
        animais.append([tipoAnimal, identificador, status, racaAnimal])


    elif opcao == 2:
        buscar = input("Digite a identificação do animal que deseja buscar: ").lower()

        encontrado = False

        for animal in animais:
            if  buscar in animal[1]:
                print(animal[0], "encontrado! Status: ", animal[2])
                encontrado=True
                break

        if not encontrado:
            print("Animal não encontrado no sistema!")


    elif opcao == 3:
        buscar= input("Digite a identificação do animal que deseja alterar: ").lower()

        encontrado = False
        status= None
        for animal in animais:
            if  buscar in animal[1]:
                encontrado=True
                status= animal
                break
        
        if  encontrado:
           print("Status atual: ", status)

           while True:
            status= input("Digite o novo status:")

            if status not in ("a venda", "lactacao", "engorda"):
                print("Status inválido! Digite novamente ")
            else:
                break

            animais[2] = status
            print("Status atualizado! ")

        else:
             print("Animal não encontrado no sistema!")

        
    elif opcao == 4:
        buscar= input("Digite a identificação do animal que deseja remover: ").lower()

        encontrado = False

        for animal in animais:
            if  buscar in animal[1]:
                encontrado=True
                break

        if encontrado:
            animais.remove(buscar)
            print("Animal removido do sistema! ")
        else:
            print("Animal não encontrado no sistema!") 


    elif opcao == 5:
        verificador = 0

        for animal in animais:
            if animal[2] == "lactacao" and animal[1] not in producao_Leite: 
                leite_produzido = ("Digite a produção de leite diária do animal:",animal[1] )


                producao_Leite.append([animal[1],leite_produzido ])
            else:
                verificador += 1
        
        if verificador >= len(animais):
            print("Não existe animais disponíveis para a registraçaõ")

    elif opcao == 6:

        while True:
           nomeProduto = input("Digite o nome do produto: ")
           pesoProduto = float(input("Digite o peso do produto: "))
           valorProduto = float(input("Digite o valor de venda (por kg) do produto: "))

           produtos.append([nomeProduto, pesoProduto, valorProduto])

           print("\nProduto cadastrado!\n")

           continuar= int(input("Deseja adicionar outro produto? (1-sim) (0-não) :"))

           if continuar == 0:
               break
 


       

      
        



