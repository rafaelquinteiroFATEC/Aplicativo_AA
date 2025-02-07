import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#040809"
    cabecalho = ft.Text("Registro de Ocorrências envolvendo Entorpecentes", italic=True, size= 20, color=ft.colors.BLUE_600)

# Botões de Ação -------------------------------------------------------------------------------
    botao_inserir = ft.FilledTonalButton(text="Inserir", icon=ft.icons.ADD, icon_color=ft.colors.GREEN_600)
    botao_editar = ft.FilledTonalButton(text="Editar", icon=ft.icons.EDIT, icon_color=ft.colors.YELLOW_400)
    botao_deletar = ft.FilledTonalButton(text="Deletar", icon=ft.icons.DELETE, icon_color=ft.colors.RED_400)

    botao_inserir_militar = ft.FilledTonalButton(text="Inserir", icon=ft.icons.ADD, icon_color=ft.colors.GREEN_600)
    botao_editar_militar = ft.FilledTonalButton(text="Editar", icon=ft.icons.EDIT, icon_color=ft.colors.YELLOW_400)
    botao_deletar_militar = ft.FilledTonalButton(text="Deletar", icon=ft.icons.DELETE, icon_color=ft.colors.RED_400)

    botao_inserir_envolvido = ft.FilledTonalButton(text="Inserir", icon=ft.icons.ADD, icon_color=ft.colors.GREEN_600)
    botao_editar_envolvido = ft.FilledTonalButton(text="Editar", icon=ft.icons.EDIT, icon_color=ft.colors.YELLOW_400)
    botao_deletar_envolvido = ft.FilledTonalButton(text="Deletar", icon=ft.icons.DELETE, icon_color=ft.colors.RED_400)

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
        border_color=ft.colors.GREY_800,
        width= 510,
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
        border_color=ft.colors.GREY_800,
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
        border_color=ft.colors.GREY_800,
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
        border_color=ft.colors.GREY_800,
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
        border_color=ft.colors.GREY_800,
        width=320,
        options=[
        ft.dropdown.Option(text='Aeroporto Internacional de Guarulhos'),
        ft.dropdown.Option(text='Água Azul'),
        ft.dropdown.Option(text='Água Chata'),
        ft.dropdown.Option(text='Anita Garibaldi'),
        ft.dropdown.Option(text='Aracília'),
        ft.dropdown.Option(text='Base Aérea de São Paulo'),
        ft.dropdown.Option(text='CECAP'),
        ft.dropdown.Option(text='Chácara Camilo'),
        ft.dropdown.Option(text='Chácara das Cerejeiras'),
        ft.dropdown.Option(text='Chácara das Lavras'),
        ft.dropdown.Option(text='Chácara de Recreio Oasis'),
        ft.dropdown.Option(text='Cidade Industrial Satélite'),
        ft.dropdown.Option(text='Cidade Jardim Cumbica'),
        ft.dropdown.Option(text='Cidade Parque Alvorada'),
        ft.dropdown.Option(text='Cidade Parque Brasília'),
        ft.dropdown.Option(text='Cidade Parque São Luiz'),
        ft.dropdown.Option(text='Cidade Seródio'),
        ft.dropdown.Option(text='Cidade Soberana'),
        ft.dropdown.Option(text='Cidade Soinco'),
        ft.dropdown.Option(text='Cidade Tupinambá'),
        ft.dropdown.Option(text='Conjunto Residencial Haroldo Veloso'),
        ft.dropdown.Option(text='Conjunto Residencial Paes de Barros'),
        ft.dropdown.Option(text='Fazenda Campina'),
        ft.dropdown.Option(text='Fazenda Itaim'),
        ft.dropdown.Option(text='Inocoop'),
        ft.dropdown.Option(text='Jardim Adelina'),
        ft.dropdown.Option(text='Jardim Aeródromo'),
        ft.dropdown.Option(text='Jardim Álamo'),
        ft.dropdown.Option(text='Jardim Albertina'),
        ft.dropdown.Option(text='Jardim Angélica'),
        ft.dropdown.Option(text='Jardim Ansalca'),
        ft.dropdown.Option(text='Jardim Arapongas'),
        ft.dropdown.Option(text='Jardim Arujá'),
        ft.dropdown.Option(text='Jardim Bananal'),
        ft.dropdown.Option(text='Jardim Bela Vista'),
        ft.dropdown.Option(text='Jardim Bondança'),
        ft.dropdown.Option(text='Jardim Brasil'),
        ft.dropdown.Option(text='Jardim Campestre'),
        ft.dropdown.Option(text='Jardim Carvalho'),
        ft.dropdown.Option(text='Jardim Cristina'),
        ft.dropdown.Option(text='Jardim Cumbica'),
        ft.dropdown.Option(text='Jardim das Andorinhas'),
        ft.dropdown.Option(text='Jardim das Nações'),
        ft.dropdown.Option(text='Jardim das Oliveiras II'),
        ft.dropdown.Option(text='Jardim do Porto'),
        ft.dropdown.Option(text='Jardim do Triunfo'),
        ft.dropdown.Option(text='Jardim Dona Luiza'),
        ft.dropdown.Option(text='Jardim dos Olivas'),
        ft.dropdown.Option(text='Jardim dos Pimentas'),
        ft.dropdown.Option(text='Jardim Fátima'),
        ft.dropdown.Option(text='Jardim Ferrão'),
        ft.dropdown.Option(text='Jardim Fortaleza'),
        ft.dropdown.Option(text='Jardim Guaracy'),
        ft.dropdown.Option(text='Jardim Guilhermino'),
        ft.dropdown.Option(text='Jardim Hanna'),
        ft.dropdown.Option(text='Jardim IV Centenário'),
        ft.dropdown.Option(text='Jardim Izildinha'),
        ft.dropdown.Option(text='Jardim Jacy'),
        ft.dropdown.Option(text='Jardim Jade'),
        ft.dropdown.Option(text='Jardim Joemi'),
        ft.dropdown.Option(text='Jardim Kátia'),
        ft.dropdown.Option(text='Jardim Leblon'),
        ft.dropdown.Option(text='Jardim Lenize'),
        ft.dropdown.Option(text='Jardim Maria Alice'),
        ft.dropdown.Option(text='Jardim Maria Clara'),
        ft.dropdown.Option(text='Jardim Maria Dirce'),
        ft.dropdown.Option(text='Jardim Maria do Carmo'),
        ft.dropdown.Option(text='Jardim Monte Alegre'),
        ft.dropdown.Option(text='Jardim Monte Alto'),
        ft.dropdown.Option(text='Jardim Monte Sião'),
        ft.dropdown.Option(text='Jardim Munira'),
        ft.dropdown.Option(text='Jardim Normândia'),
        ft.dropdown.Option(text='Jardim Nossa Senhora Aparecida'),
        ft.dropdown.Option(text='Jardim Nova Cidade'),
        ft.dropdown.Option(text='Jardim Novo Portugal'),
        ft.dropdown.Option(text='Jardim Olivas'),
        ft.dropdown.Option(text='Jardim Oliveira'),
        ft.dropdown.Option(text='Jardim Ottawa'),
        ft.dropdown.Option(text='Jardim Paulista'),
        ft.dropdown.Option(text='Jardim Ponte Alta'),
        ft.dropdown.Option(text='Jardim Presidente Dutra'),
        ft.dropdown.Option(text='Jardim Ramos'),
        ft.dropdown.Option(text='Jardim Regina'),
        ft.dropdown.Option(text='Jardim Rodolpho'),
        ft.dropdown.Option(text='Jardim Sandra'),
        ft.dropdown.Option(text='Jardim Santa Helena'),
        ft.dropdown.Option(text='Jardim Santa Maria'),
        ft.dropdown.Option(text='Jardim Santa Paula'),
        ft.dropdown.Option(text='Jardim Santa Terezinha'),
        ft.dropdown.Option(text='Jardim Santo Afonso'),
        ft.dropdown.Option(text='Jardim Santo Expedito'),
        ft.dropdown.Option(text='Jardim São Geraldo'),
        ft.dropdown.Option(text='Jardim São João'),
        ft.dropdown.Option(text='Jardim São José'),
        ft.dropdown.Option(text='Jardim São Manoel'),
        ft.dropdown.Option(text='Jardim Silvestre'),
        ft.dropdown.Option(text='Jardim Vida Nova'),
        ft.dropdown.Option(text='Nova Ponte Alta'),
        ft.dropdown.Option(text='Orquidiama'),
        ft.dropdown.Option(text='Parque das Nações'),
        ft.dropdown.Option(text='Parque Industrial Cumbica'),
        ft.dropdown.Option(text='Parque Jandaia'),
        ft.dropdown.Option(text='Parque Jurema'),
        ft.dropdown.Option(text='Parque Maria Helena'),
        ft.dropdown.Option(text='Parque Piratininga'),
        ft.dropdown.Option(text='Parque Residencial Bambi'),
        ft.dropdown.Option(text='Parque Santos Dumont'),
        ft.dropdown.Option(text='Parque São Miguel'),
        ft.dropdown.Option(text='Parque Stella'),
        ft.dropdown.Option(text='Parque Uirapuru'),
        ft.dropdown.Option(text='Residencial Parque Cumbica'),
        ft.dropdown.Option(text='Rocinha'),
        ft.dropdown.Option(text='São Roque'),
        ft.dropdown.Option(text='Sítio dos Ferrões'),
        ft.dropdown.Option(text='Sítio Pau de Leite'),
        ft.dropdown.Option(text='Sítio São Francisco'),
        ft.dropdown.Option(text='Sítios Recreio Rober'),
        ft.dropdown.Option(text='Tanque Grande'),
        ft.dropdown.Option(text='Várzea do Palácio'),
        ft.dropdown.Option(text='Vila do Sapo'),
        ft.dropdown.Option(text='Vila Aimoré'),
        ft.dropdown.Option(text='Vila Alzira'),
        ft.dropdown.Option(text='Vila Any'),
        ft.dropdown.Option(text='Vila Aurora'),
        ft.dropdown.Option(text='Vila Bernardino'),
        ft.dropdown.Option(text='Vila Branca'),
        ft.dropdown.Option(text='Vila Carmela'),
        ft.dropdown.Option(text='Vila Dinamarca'),
        ft.dropdown.Option(text='Vila Girassol'),
        ft.dropdown.Option(text='Vila GPM'),
        ft.dropdown.Option(text='Vila Itai'),
        ft.dropdown.Option(text='Vila Itaim'),
        ft.dropdown.Option(text='Vila Izabel'),
        ft.dropdown.Option(text='Vila Laurita'),
        ft.dropdown.Option(text='Vila Nova Bonsucesso'),
        ft.dropdown.Option(text='Vila Nova Cumbica'),
        ft.dropdown.Option(text='Vila Paraíso'),
        ft.dropdown.Option(text='Vila Pastor'),
        ft.dropdown.Option(text='Vila Pires'),
        ft.dropdown.Option(text='Vila Rica'),
        ft.dropdown.Option(text='Vila Sadokim'),
        ft.dropdown.Option(text='Vila São Benedito'),
        ft.dropdown.Option(text='Vila São Carlos'),
        ft.dropdown.Option(text='Vila São Gabriel'),
        ft.dropdown.Option(text='Vila São João'),
        ])

    municipio = ft.Dropdown(
        label="Município",
        border_color=ft.colors.GREY_800,
        width= 140,
        options=[
            ft.dropdown.Option("Guarulhos"),
            ft.dropdown.Option("Arujá"),
            ft.dropdown.Option("Santa Isabel"),
        ]
    )

    tipo_entorpecente = ft.Dropdown(
        label="Tipo de Entorpecentes",
        border_color=ft.colors.GREY_800,
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
        border_color=ft.colors.GREY_800,
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
    rua = ft.TextField(label="Rua/Avenida", width=350, border_color=ft.colors.GREY_800,)
    numero = ft.TextField(label="nº", width=50, border_color=ft.colors.GREY_800,)
    data = ft.TextField(label="Data", width=140, border_color=ft.colors.GREY_800)
    quantidade = ft.TextField(label="Qtd (Kg)", width=100, border_color=ft.colors.GREY_800)
    viatura = ft.TextField(label="Viatura", width=150, border_color=ft.colors.GREY_800, prefix_text="M-")
    re = ft.TextField(label="RE", width=100, border_color=ft.colors.GREY_800)
    nome_militar = ft.TextField(label="Nome do Militar", width=350, border_color=ft.colors.GREY_800)
    registro_militar = ft.TextField(label="Registro", width=100, border_color=ft.colors.GREY_800)
    registro_envolvido = ft.TextField(label="Registro", width=100, border_color=ft.colors.GREY_800)
# ----------------------------------------------------------------------------------------------

    container_militares = ft.Container(
        width=660,
        border=ft.border.all(1, ft.colors.GREY_700),
        padding=20,
        margin=5,
        border_radius= 10,
        content=ft.Column([
            ft.Text("Militares", color=ft.colors.GREY_400, size=18, italic=True),
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
        width=660,
        border=ft.border.all(1, ft.colors.GREY_700),
        padding=20,
        margin=5,
        border_radius= 10,
        content=ft.Column([
            ft.Text("Envolvidos", color=ft.colors.GREY_400, size=18, italic=True),
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
                registro_envolvido
            ])
        ])
    )

    container_inseridos = ft.Container(
        width=1160,
        height=490,
        border=ft.border.all(1, ft.colors.GREY_700),
        padding=20,
        margin=5,
        border_radius= 10,
        content=ft.Column([
            ft.Text("Dados Inseridos", color=ft.colors.GREY_400, size=18, italic=True),
            ft.Divider(color=ft.colors.GREY_700),
        ])
    )

    container_dados_basicos = ft.Container(
        expand=True,
        border=ft.border.all(1, ft.colors.GREY_700),
        padding=20,
        margin=5,
        border_radius= 10,
        content=ft.Column([
            ft.Text("Dados Básicos", color=ft.colors.GREY_400, size=18, italic=True),
            ft.Divider(color=ft.colors.GREY_700),
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
                ft.Column([
                    container_militares,
                    container_envolvidos,
                ]),
                container_inseridos
            ]),

            ft.Row([
                botao_inserir, 
                botao_editar, 
                botao_deletar,
            ]),
        ]),
    )

    page.add(cabecalho, container_dados_basicos)

ft.app(target=main)
