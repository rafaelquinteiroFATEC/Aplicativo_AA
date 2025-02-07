import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#040809"
    cabecalho = ft.Text("Registro de Ocorrências envolvendo Entorpecentes", italic=True, size= 20, color=ft.Colors.BLUE_600)

    """traficante, nome, rg, vulgo, comparsa, viatura, militar, talao"""

# Botões de Ação -------------------------------------------------------------------------------
    botao_inserir = ft.FilledTonalButton(text="Inserir", icon=ft.Icons.ADD, icon_color=ft.Colors.GREEN_600)
    botao_editar = ft.FilledTonalButton(text="Editar", icon=ft.Icons.EDIT, icon_color=ft.Colors.YELLOW_400)
    botao_deletar = ft.FilledTonalButton(text="Deletar", icon=ft.Icons.DELETE, icon_color=ft.Colors.RED_400)

    botao_inserir_militar = ft.FilledTonalButton(text="Inserir", icon=ft.Icons.ADD, icon_color=ft.Colors.GREEN_600)
    botao_editar_militar = ft.FilledTonalButton(text="Editar", icon=ft.Icons.EDIT, icon_color=ft.Colors.YELLOW_400)
    botao_deletar_militar = ft.FilledTonalButton(text="Deletar", icon=ft.Icons.DELETE, icon_color=ft.Colors.RED_400)

    botao_inserir_envolvido = ft.FilledTonalButton(text="Inserir", icon=ft.Icons.ADD, icon_color=ft.Colors.GREEN_600)
    botao_editar_envolvido = ft.FilledTonalButton(text="Editar", icon=ft.Icons.EDIT, icon_color=ft.Colors.YELLOW_400)
    botao_deletar_envolvido = ft.FilledTonalButton(text="Deletar", icon=ft.Icons.DELETE, icon_color=ft.Colors.RED_400)

    nav_primeiro_militar = ft.FloatingActionButton(icon=ft.icons.FIRST_PAGE)
    nav_anterior_militar = ft.FloatingActionButton(icon=ft.icons.NAVIGATE_BEFORE)
    nav_proximo_militar = ft.FloatingActionButton(icon=ft.icons.NAVIGATE_NEXT)
    nav_ultimo_militar = ft.FloatingActionButton(icon=ft.icons.LAST_PAGE)

    nav_primeiro_envolvido = ft.FloatingActionButton(icon=ft.icons.FIRST_PAGE)
    nav_anterior_envolvido = ft.FloatingActionButton(icon=ft.icons.NAVIGATE_BEFORE)
    nav_proximo_envolvido = ft.FloatingActionButton(icon=ft.icons.NAVIGATE_NEXT)
    nav_ultimo_envolvido = ft.FloatingActionButton(icon=ft.icons.LAST_PAGE)
# ----------------------------------------------------------------------------------------------

# Caixa de Seleção para os dados ---------------------------------------------------------------
    natureza = ft.Dropdown(
        label="Natureza da Ocorrência",
        border_color=ft.Colors.GREY_900,
        width= 490,
        options=[
            ft.dropdown.Option("Tráfico de Drogas (Art. 33)"),
            ft.dropdown.Option("Associação para o Tráfico (Art. 35)"),
            ft.dropdown.Option("Porte de Drogas para Uso Pessoal (Art. 28)"),
            ft.dropdown.Option("Tráfico Internacional de Drogas (Art. 33, §1º, I)"),
            ft.dropdown.Option("Cultivo de Drogas Sem Autorização (Art. 33, §1º, II)"),
            ft.dropdown.Option("Induzir ou Auxiliar o Uso de Drogas (Art. 33, §2º)"),
            ft.dropdown.Option("Organização Criminosa Ligada ao Tráfico (Lei 12.850/2013)"),
            ft.dropdown.Option("Localização de Entorpecentes"),
        ]
    )
    
    btl = ft.Dropdown(
        label="Batalhão",
        border_color=ft.Colors.GREY_900,
        width= 130,
        options=[
            ft.dropdown.Option("31º BPM/M"),
            ft.dropdown.Option("15º BPM/M"),
            ft.dropdown.Option("26º BPM/M"),
            ft.dropdown.Option("41º BPM/I"),
            ft.dropdown.Option("35º BPM/M"),
            ft.dropdown.Option("32º BPM/M"),
            ft.dropdown.Option("2º BPM/M"),
            ft.dropdown.Option("29º BPM/M"),
        ]
    )

    cia = ft.Dropdown(
        label="Cia",
        border_color=ft.Colors.GREY_900,
        width=80,
        options=[
            ft.dropdown.Option("1"),
            ft.dropdown.Option("2"),
            ft.dropdown.Option("3"),
            ft.dropdown.Option("4"),
            ft.dropdown.Option("5"),
        ]
    )

    tipo_de_via = ft.Dropdown(
        label="Tipo de via",
        border_color=ft.Colors.GREY_900,
        width=130,
        options=[
            ft.dropdown.Option("Rua"),
            ft.dropdown.Option("Avenida"),
            ft.dropdown.Option("Estrada"),
            ft.dropdown.Option("Viela"),
            ft.dropdown.Option("Passagem"),
        ]
    )

    """Completar com a lista de bairros existentes organizada em ordem alfabética"""
    bairro = ft.Dropdown(
        label="Bairro",
        border_color=ft.Colors.GREY_900,
        width=300,
        options=[
            ft.dropdown.Option("Haroldo Veloso")
        ]
    )

    municipio = ft.Dropdown(
        label="Município",
        border_color=ft.Colors.GREY_900,
        width= 150,
        options=[
            ft.dropdown.Option("Guarulhos"),
            ft.dropdown.Option("Arujá"),
            ft.dropdown.Option("Santa Isabel"),
        ]
    )

    tipo_entorpecente = ft.Dropdown(
        label="Tipo de Entorpecentes",
        border_color=ft.Colors.GREY_900,
        width= 250,
        options=[
            ft.dropdown.Option("Maconha"),
            ft.dropdown.Option("Cocaína"),
            ft.dropdown.Option("Crack"),
            ft.dropdown.Option("Lança Perfume"),
            ft.dropdown.Option("Pasta base de Cocaína"),
            ft.dropdown.Option("LSD"),
            ft.dropdown.Option("Ecstasy"),
            ft.dropdown.Option("Skank"),
            ft.dropdown.Option("Metanfetamina"),
            ft.dropdown.Option("K9"),            
        ]
    )    
    
    posto_grad = ft.Dropdown(
        label="Posto/Grad",
        border_color=ft.Colors.GREY_900,
        width= 150,
        options=[
            ft.dropdown.Option("Cel PM"),
            ft.dropdown.Option("Ten Cel PM"),
            ft.dropdown.Option("Maj PM"),
            ft.dropdown.Option("Cap PM"),
            ft.dropdown.Option("1º Ten PM"),
            ft.dropdown.Option("2º Ten PM"),
            ft.dropdown.Option("Asp Oficial PM"),
            ft.dropdown.Option("Aluno Of PM"),
            ft.dropdown.Option("Subten PM"),
            ft.dropdown.Option("1º Sgt PM"),
            ft.dropdown.Option("2º Sgt PM"),
            ft.dropdown.Option("3º Sgt PM"),
            ft.dropdown.Option("Aluno Sgt PM"),
            ft.dropdown.Option("Cb PM"),
            ft.dropdown.Option("Sd PM"),
            ft.dropdown.Option("Sd PM 2ª Cl"),            
        ]
    )
# ----------------------------------------------------------------------------------------------

# Caixas de Texto para entrada de dados --------------------------------------------------------
    rua = ft.TextField(label="Rua/Avenida", width=350, border_color=ft.Colors.GREY_900,)
    numero = ft.TextField(label="nº", width=50, border_color=ft.Colors.GREY_900,)
    data = ft.TextField(label="Data", width=130, border_color=ft.Colors.GREY_900)
    quantidade = ft.TextField(label="Qtd (Kg)", width=100, border_color=ft.Colors.GREY_900)
    viatura = ft.TextField(label="Viatura", width=150, border_color=ft.Colors.GREY_900, prefix_text="M-")
    re = ft.TextField(label="RE", width=100, border_color=ft.Colors.GREY_900)
    nome_militar = ft.TextField(label="Nome do Militar", width=350, border_color=ft.Colors.GREY_900)
    registro_militar = ft.TextField(label="Nome do Militar", width=350, border_color=ft.Colors.GREY_900)
    registro_envolvido = ft.TextField(label="Nome do Militar", width=350, border_color=ft.Colors.GREY_900)
# ----------------------------------------------------------------------------------------------

    container_militares = ft.Container(
        expand=True,
        border=ft.border.all(1, ft.Colors.GREY_700),
        padding=20,
        margin=5,
        border_radius= 10,
        content=ft.Column([
            ft.Row([
                posto_grad,
                re,
                nome_militar
            ]),
            ft.Row([
                botao_inserir_militar,
                botao_editar_militar,
                botao_deletar_militar
            ]),
            ft.Row([
                nav_primeiro_militar,
                nav_anterior_militar,
                nav_proximo_militar,
                nav_ultimo_militar,
                registro_militar
            ])
        ])
    )

    container_envolvidos = ft.Container(
        expand=True,
        border=ft.border.all(1, ft.Colors.GREY_700),
        padding=20,
        margin=5,
        border_radius= 10,
        content=ft.Column([
            ft.Row([
                posto_grad,
                re,
                nome_militar
            ]),
            ft.Row([
                botao_inserir_envolvido,
                botao_editar_envolvido,
                botao_deletar_envolvido
            ]),
            ft.Row([
                nav_primeiro_envolvido,
                nav_anterior_envolvido,
                nav_proximo_envolvido,
                nav_ultimo_envolvido,
                registro_militar
            ])
        ])
    )

    container_dados_basicos = ft.Container(
        expand=True,
        border=ft.border.all(1, ft.Colors.GREY_700),
        padding=20,
        margin=5,
        border_radius= 10,
        content=ft.Column([
            ft.Text("Dados Básicos", color=ft.Colors.GREY_400, size=18, italic=True),
            ft.Divider(color=ft.Colors.GREY_700),
            ft.Row([
                natureza, 
                tipo_entorpecente,
                quantidade,
                data,

            ]),
            ft.Row([
                tipo_de_via,
                rua, 
                numero, 
                bairro, 
                municipio,
            ]),
            ft.Row([
                btl,
                cia,
                viatura,
            ]),
            
            ft.Row([
                botao_inserir, 
                botao_editar, 
                botao_deletar
            ]),
            ft.Row([
                container_militares,
                container_envolvidos

            ])
        ]),
    )






    page.add(cabecalho, container_dados_basicos)

ft.app(target=main)

