import flet as ft
# import sys

def main(page: ft.Page):

    # Configurações da página Inicial
    page.title = "Sistema de Gerenciamento de Rotinas Administrativas"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = "#040809"

    # Carregar a imagem
    background_image = ft.Image(
        src="coruja_inicial.png",
        width=page.window.width,  # Define a largura como a largura da janela
        height=page.window.height,  # Define a altura como a altura da janela
    )
    
    # Atualiza a página quando a janela for redimensionada
    def redimencionar(e):
        background_image.width = page.window.width
        background_image.height = page.window.height
        page.update()

    # Vincular evento de redimensionamento
    page.on_resized = redimencionar

    # Exibe a interface
    page.update()
    
    ## ------------------------------------------------- ## ------------------------------------------------- ##

    
    ## ------------------------------------------------- ## ------------------------------------------------- ##

    # Função para exibir o menu de login
    def show_login(e):
        dialogo.open = True
        page.update()
    
    # Função para fechar o menu de login
    def fecha_login(e):
        dialogo.open = False
        page.update()
    
    """
    Fazer a função de validação do CPF e a confirmação do acesso através de pesquisa no banco de dados de cadastro de usuários,
    saia da tela de login e passando para a tela inicial com o nome do usuário no canto superior esquerdo.
    """

    # Função para coletar os dados inseridos, validar o CPF e senha

    def inserir_dados_login(e):
        cpf = login_cpf.value
        senha = login_senha.value 

        if len(cpf) != 11:  
            page.open(
                ft.AlertDialog(
                title=ft.Text("CPF inválido"),
                )
            )
            login_cpf.value = ""
        
    # Função para verificar a validade do CPF
        multiplicador = 10
        soma = 0
        cpf_calculado = ""

        # Primeiro dígito conferidor
        for numero in cpf:

            if multiplicador <= 10 and multiplicador > 1:
                cpf_calculado += numero
                soma = soma + (int(numero) * multiplicador)
            multiplicador -= 1

            if (int(11 - (soma % 11))) > 9:
                dig_1 = "0"
            else:
                dig_1 = str(11 - (soma % 11))        

        cpf_calculado += dig_1

        # Segundo dígito conferidor
        multiplicador = 11
        soma = 0

        for numero in cpf:
            
            if multiplicador <= 11 and multiplicador > 1:
                soma = soma + (int(numero) * multiplicador)
            multiplicador -= 1

            if (int(11 - (soma % 11))) > 9:
                dig_2 = "0"
            else:
                dig_2 = str(11 - (soma % 11))        

        cpf_calculado += dig_2

        if cpf != cpf_calculado:
            page.open(
                    ft.AlertDialog(
                    title=ft.Text("CPF inválido"),
                    )
                )
            login_cpf.value = ""
        else:
            ...
            #buscar_usuario(cpf, senha)
        
        # fecha_login(e)
    

    """
    Implementar função que faça a confirmação se o usuário deseja realmente fechar a aplicação, 
    realize Logoff automaicamente e feche a janela acionada pelo iconButton Fechar
    
    # Função para Fechar a Aplicação
    def encerrar_app(e):
        sys.exit()      
    """

    def informacoes():
        ...

    resultado_text = ft.Text()
    # Campos do menu de login
    login_cpf = ft.TextField(label="CPF", width=300)
    login_senha = ft.TextField(label="Senha",password=True, can_reveal_password=True,width=300)
    
    # Caixa de Diálogo para o menu de login
    dialogo = ft.AlertDialog(
        modal=True,
        title=ft.Text("Insira suas Credenciais"),
        content=ft.Column(
            [
                login_cpf,
                login_senha
            ],
            tight=True,
        ),
        actions=[
            ft.TextButton("Cancelar", on_click=fecha_login,),
            ft.TextButton("Entrar", on_click=inserir_dados_login),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
    )
    
    # Adiciona a barra de menu e o botão de login
    page.appbar = ft.AppBar(
        title=ft.Text("Página de Login"),
        actions=[
            ft.IconButton(icon=ft.icons.INFO, on_click=informacoes),    # Inserir Informações Gerais
            ft.IconButton(icon=ft.icons.ADMIN_PANEL_SETTINGS, on_click=..., tooltip="Acesso do Administrador"), # Implementar Rotinas Gerenciais
            ft.IconButton(icon=ft.icons.LOGIN, on_click=show_login),
            ft.IconButton(icon=ft.icons.CLOSE, icon_color="red", on_click=...),
        ],
    )
    
    page.dialog = dialogo
    page.update()

    # Rodapé
    footer = ft.Container(
        content=ft.Text(
            "Versão 1.0.0",
            style=ft.Text.theme_style,
            color=ft.colors.WHITE,
            italic=True,
        ),
        bgcolor= "#040809",
        padding=ft.padding.all(10),
        alignment=ft.alignment.bottom_right,
    )

    # Adiciona a imagem à página
    page.add(
        ft.Column(
            [
                # Container criado para garantir que a imagem de fundo ocupasse a parte que sobra após a AppBar
                ft.Container(       
                content=background_image,
                expand=True,
                ),
                footer
            ],
            expand=True,   
        )
    )
    page.update()

ft.app(target=main)