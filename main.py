
usuarios= []
login=[False, None]

while not login[0]:

    while True:
        print("\n Selecione a opção desejada: ")
        print("1- Login") 
        print("2- Cadastra-se como cliente ")
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
            if email == usuario[0] and senha == usuario[1] and tipo == usuario[2]: #!perguntar se verifica o tipo
                print("Seja bem-vindo(a) !")
                login=[True,tipo]
                encontrou=True
                break

        if not encontrou:
            print("E-mail ou senha incorretos ")


    elif opcao == 2:

        while True: 
            email= input("Digite seu e-mail: ")
            if "@" in email:
                break
            else:
                print("E-mail invalido, digite novamente: ")

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

while login[0] and login[1] == "cliente":
    print ("1 - ver produtos")
    print (" 2 - ver animais")
    print ("3 - comprar")
    print ("4 - agendar retirada")
    print ("#########")
    print ("0 - sair")