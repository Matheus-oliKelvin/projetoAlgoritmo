import json,os, pwinput
from rich import print
from rich.panel import Panel

def validar_opcao( opcao: int, minimo: int, maximo: int,):

    if opcao >= minimo and opcao <= maximo:
        return True
    
    return False

def validar_email(email: str):
    if "@" not in email or ".com" not in email:
        return False
    return True

def verificar_existe(dicionario: dict, identificacao: str):
    
    if dicionario.get(identificacao) is None:
        return False
    
    return True

def buscar_por_identificacao (dicionario: dict, identificacao: str):

    return dicionario.get(identificacao) 
      
    


def limpar():
    
    os.system("cls")

def pausar():
    
    input("\nPressione [Enter] para continuar... ")
   

def carregar_dados(nome_arquivo: str):

    if not os.path.exists(f"data/{nome_arquivo}.json"):
        return {}
    
    with open(f"data/{nome_arquivo}.json", "r") as arquivo:
            return json.load(arquivo)
    

def sair():
    print(" [red] Saindo... [/red]")
    exit()

def deslogar(login: dict):

    login["logado"]= False
    login["usuario"]= None
    login["tipo_usuario"] = None


def logar(usuarios: dict, login: dict):

    email= input("Digite seu e-mail: ").lower().strip()
    senha= pwinput.pwinput("Digite sua senha: ").strip()

    if email in usuarios:

        if usuarios[email]["senha"] == senha:

            login ["logado"] = True
            login ["usuario"] = email
            login ["tipo_usuario"] = usuarios[email]["tipo_usuario"]

            print("[green] Seja bem-vindo(a) ![/green]")
            print("---------------------------------------------")

        else:
            print(" [red] Senha incorreta! [/red]\n")

            pausar()

    else:
        print("[red] Usuario não existe! [/red] \n")

        pausar()


def cadastrar_usuario(usuarios: dict):

    while True:

        email= input("Digite seu e-mail: ").lower().strip()

        if verificar_existe(usuarios, email):
            print("[yellow]Email já cadastrado! Digite novamente [/yellow]\n ")

        elif  not validar_email(email):
            print("[yellow]Email inválido! Digite novamente[/yellow]\n ")

        else:
            break

    while True:
        senha= pwinput.pwinput("Digite sua senha : ").strip()
        confimar_senha= pwinput.pwinput("Digite sua senha novamente: ").strip()

        if senha == confimar_senha:
            break
        else:
            print("[yellow] As senhas não coincidem! Digite novamente [/yellow]\n")

    while True:
        tipo_usuario= input("Você deseja se cadastrar como um (cliente) ou (adm): ").lower().strip()

        if tipo_usuario == "cliente" or tipo_usuario =="adm":
            break
        else:
            print("[yellow] Nome invalido, tente novamente [/yellow]\n")

    usuarios[email] = {
        "senha": senha,
        "tipo_usuario": tipo_usuario
    } 
    
    with open("data/usuarios.json", "w") as arquivo:

        json.dump(usuarios, arquivo, indent=4)


    print("[green] Usuário cadastrado com sucesso! [/green] \n")

    pausar()
    

def mostrar_menu_login(usuarios: dict, login: dict) :

    limpar()

    while True:

        menu=  """

    1- Login
    2- Cadastra-se
    0- Sair

        """

        print(Panel.fit(menu, title= "MENU"))

        opcao= int(input(" >  "))

        if validar_opcao(opcao, 0 , 2):
            break
        else:
            print(" [yellow] Opção invalida! Digite novamente [/yellow] \n")

    if opcao == 0:
        sair()

    elif opcao == 1:
        logar(usuarios, login)

    else:
        cadastrar_usuario(usuarios)
    