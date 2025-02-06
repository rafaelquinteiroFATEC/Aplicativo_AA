import flet as ft

def main(page: ft.Page):
    page.bgcolor = "#040809"
    cabecalho = ft.Text("Registro de Ocorrências de Tráfico de Entorpecentes", italic=True, size= 20, color=ft.colors.BLUE_600)

    """data, quantidade: float, tipo_entorpecente, traficante, nome, rg, vulgo, comparsa, viatura, militar, talao):
        self.btl = btl"""

# Botões de Ação --------------------------------------------------------
    botao_inserir = ft.FilledTonalButton(text="Inserir", icon=ft.icons.ADD, icon_color=ft.colors.GREEN_600)
    botao_editar = ft.FilledTonalButton(text="Editar", icon=ft.icons.EDIT, icon_color=ft.colors.YELLOW_400)
    botao_deletar = ft.FilledTonalButton(text="Deletar", icon=ft.icons.DELETE, icon_color=ft.colors.RED_400)
# -----------------------------------------------------------------------

# Caixa de Seleção para os dados
    btl = ft.Dropdown(
        label="Batalhão",
        border_color=ft.colors.GREY_900,
        width= 120,
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
        border_color=ft.colors.GREY_900,
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
        border_color=ft.colors.GREY_900,
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
        border_color=ft.colors.GREY_900,
        width=300,
        options=[
            ft.dropdown.Option("Haroldo Veloso")
        ]
    )

    municipio = ft.Dropdown(
        label="Município",
        border_color=ft.colors.GREY_900,
        width= 150,
        options=[
            ft.dropdown.Option("Guarulhos"),
            ft.dropdown.Option("Arujá"),
            ft.dropdown.Option("Santa Isabel"),
        ]
    )

# Caixas de Texto para entrada de dados
    rua = ft.TextField(label="Rua/Avenida", width=350, border_color=ft.colors.GREY_900,)
    numero = ft.TextField(label="nº", width=50, border_color=ft.colors.GREY_900,)

    container_dados_basicos = ft.Container(
        expand=True,
        border=ft.border.all(1, ft.colors.GREY_700),
        padding=20,
        margin=5,
        border_radius= 10,
        content=ft.Column([
            ft.Text("Dados Básicos", color=ft.colors.GREY_400, size=15),
            ft.Divider(color=ft.colors.GREY_700),
            ft.Row([
                btl, cia, tipo_de_via ,rua, numero, bairro, municipio,
            ]),
            ft.Row([
                botao_inserir, botao_editar, botao_deletar
            ]),
        ]),
    )

    




    page.add(cabecalho, container_dados_basicos)

ft.app(target=main)

