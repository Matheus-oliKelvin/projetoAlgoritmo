
while True:
    while True:
        print("\n Selecione a opção desejada: ")
        print("1- login")
        print("2- Cadastra-se")
        print("3- Sair")
        opcao= int(input(" digite a opção : "))
        if opcao >=1 and opcao<=3:
            break
        else:
            print("Opção invalida! Digite novamente\n")
    if opcao == 3:
        print("Saindo...")
        break
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
        usuarios= []
        usuarios.append(email, senha, tipo)
        print("Usuário cadastrado com sucesso!")