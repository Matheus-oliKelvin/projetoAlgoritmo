
import utils.adm, utils.cliente, utils.geral




login = {
    "logado": False,
    "usuario": None,
    "tipo_usuario": None
}

usuarios= utils.geral.carregar_dados("usuarios")
animais=utils.geral.carregar_dados("animais")
lotes=utils.geral.carregar_dados("lotes")
produtos=utils.geral.carregar_dados("produtos")
producao_leite=utils.geral.carregar_dados("producao_leite")
despesas=utils.geral.carregar_dados("despesas")
historico_arroba= utils.geral.carregar_dados("historico_arroba")


carinho=[]
total_compra=0
agenda_retiradas = {}


while True:
    if not login ["logado"]:

        utils.geral.mostrar_menu_login(usuarios, login)
        

    elif login["tipo_usuario"] == "adm":
        
        utils.adm.mostrar_menu_adm(animais,lotes,login,producao_leite,produtos,despesas,historico_arroba)
        

    

        

    elif login["tipo_usuario"] == "cliente":

        utils.cliente.mostrar_menu_cliente(animais,lotes,produtos,total_compra,usuarios,agenda_retiradas)

      