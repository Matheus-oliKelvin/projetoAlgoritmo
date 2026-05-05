
usuarios= []
login=[False, None]

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
            email= input("Digite seu e-mail: ")
            
            for usuario in usuarios:
                if usuario[0] == email:
                    print("Esse e-mail já está cadastrado!Digite novamente")
                    verificador= False
                    break
                else:
                    verificador=True


            if "@" in email:
                verificador= True
            else:
                print("email inválido, falta o @:")
                verificador=False
                break


            if verificador :
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
        print("5- Registrar litros de leite ordenhado ")
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
        animais=[]

        while True:
            tipoAnimal= input("Qual o tipo do animal: ").lower()

            if tipoAnimal not in ("caprino", "ovino", "suino", "leitao", "bovino de leite"):
                print("Animal inválido! Digite novamente ")
            else:
                break


        identificador = input("Digite a identificação desse", tipoAnimal,": ").lower()


        while True:
            status= input("Qual o status desse animal:")

            if status not in ("a venda", "lactacao", "engorda"):
                print("Status inválido! Digite novamente ")
            else:
                break
        
        animais.append([tipoAnimal, identificador, status])

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


       

      
        



