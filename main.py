produtos = [["leite", 10, 20], ["queijo", 20, 10], ["manteiga", 5, 10]]
animais = [["vacas", 1000, 5], ["leitoes", 300, 5], ["ovelhas", 350, 5]]

total_compra = []

usuarios= [["a", "a", "cliente" ]]
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

while login[0] and login[1] == "cliente":
    
    
    
    print ("1 - ver produtos")
    print ("2 - ver animais")
    print ("3 - comprar")
    print ("4 - agendar retirada")
    print ("5 - ver total da compra")
    print ("#########")
    print ("0 - sair")

    opcao = input ("diga uma opção valida: ")

    if opcao == "1":
        for produtos in produtos:
            print ("Nome:", produtos[0])
            print ("Preço:", produtos[1],"$")
            print ("Estoque:", produtos[2], "em estoque")
            print ("\n")    
    
    elif opcao == "2":
        for animais in animais:
            print ("Nome:", animais[0])
            print ("Preço:", animais[1],"$")
            print ("Estoque:", animais[2], "em estoque")
            print ("\n")  
    
    elif opcao == "3":
        compra = input ("o que deseja comprar: ").lower().strip()
        encontrado = False

        for produto in produtos:
            if compra == produto [0].lower():
            
                encontrado = True

                quantidade = int (input ("diga a quantidade do produto escolhido deseja comprar: "))

            if produto [2] >= quantidade:
                produto [2] -= quantidade
                
            valor = produto[1] * quantidade
            total_compra += valor
            print (f"compra realizada no valor de {total_compra}")
            
            else:
                print ("estoque insuficiente!")
    
        