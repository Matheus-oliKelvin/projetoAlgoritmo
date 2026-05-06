produtos = [["leite", 10, 20], ["queijo", 20, 10], ["soja", 5, 10]]
animais = [["vacas", 1000, 5], ["leitoes", 300, 5], ["ovelhas", 350, 5]]

total_compra = 0

usuarios = [["a", "a", "cliente"]]
login = [False, None]

while not login[0]:

    print("\nSelecione a opção desejada:")
    print("1- Login")
    print("2- Cadastrar-se")
    print("0- Sair")

    opcao = input("Digite a opção: ")

    if opcao == "0":
        print("Saindo...")
        break

    elif opcao == "1":
        email = input("Digite seu e-mail: ")
        senha = input("Digite sua senha: ")
        tipo = input("admin ou cliente: ").lower()

        encontrou = False

        for usuario in usuarios:
            if email == usuario[0] and senha == usuario[1] and tipo == usuario[2]:
                print("Seja bem-vindo!")
                login = [True, tipo]
                encontrou = True
                break

        if not encontrou:
            print("Login inválido")

    elif opcao == "2":
        email = input("Email: ")
        senha = input("Senha: ")
        tipo = input("cliente ou adm: ").lower()
        usuarios.append([email, senha, tipo])
        print("Cadastrado!")

while login[0] and login[1] == "cliente":

    print("\n1 - ver produtos")
    print("2 - ver animais")
    print("3 - comprar")
    print ("4 - agendar retirada")
    print("5 - valor total das compras")
    print("0 - sair")
    
    opcao = input("digite uma opção: ")

    if opcao == "1":
        for produto in produtos:
            print(produto)

    elif opcao == "2":
        for animal in animais:
            print(animal)

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
                    print(f"o valor da compra foi de:R${valor}")
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
                        print(f"o valor da compra foi de:R${valor}")
                    else:
                        print("estoque insuficiente!")
                    break

        if not encontrado:
            print("Não encontrado")

    elif opcao == "5":
        print(f"o total da suas compras foram de: R${total_compra}" )

    elif opcao == "0":
        break
print

















``