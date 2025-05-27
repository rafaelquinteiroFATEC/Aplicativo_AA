import flet as ft
from datetime import datetime
import sqlite3 as sq

# Listas para Combo Box
periodo_lista = ["Diário", "Semanal", "Quinzenal", "Mensal", "Bimestral", "Trimestral", "Semestral", "Anual", "Extraordinário", "Exporárico", "Investigação Social", "Credenciamento"]
forma_envio_lista = ["Email", "DTI", "Mídia Física", "Via Malote"]
status_envio_lista = ["Finalizado", "Em Produção", "Aguardando Aprovação"]
difusao_lista = ["AR - CPA/M-7", "AC - Criminal", "AC - Público Interno", "AC - Social"]

def main(page: ft.Page):
    page.bgcolor = "#090113"
    
    # Informações da tela
    cabecalho = ft.Text("Controle de Fluxo de Documentos", size=28, font_family="Times New Roman", color="#fcd021", italic=True)
    
    # Conexão com o banco de dados
    def get_db_connection():
        conn = sq.connect("doc.db")
        conn.row_factory = sq.Row
        return conn

    # Criar tabela se não existir
    def criar_tabela():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS documentos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                periodo TEXT,
                documento TEXT,
                referencia TEXT,
                forma_envio TEXT,
                difusao TEXT,
                dia_do_mes INTEGER,
                prazo TEXT,
                envio TEXT
            )
        """)
        conn.commit()
        conn.close()

    criar_tabela()

    # Função para buscar documentos
    def buscar_documentos():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT documento FROM documentos ORDER BY documento")
        documentos = cursor.fetchall()
        conn.close()
        return [doc["documento"] for doc in documentos]

    # Função para mostrar diálogo de seleção
    def mostrar_documentos_dialog(e):
        documentos = buscar_documentos()
        
        if not documentos:
            page.snack_bar = ft.SnackBar(
                ft.Text("Nenhum documento encontrado no banco de dados."),
                bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()
            return

        def selecionar_documento(e):
            documento.value = dropdown.value
            dialog.open = False
            page.update()

        dropdown = ft.Dropdown(
            options=[ft.dropdown.Option(doc) for doc in documentos],
            width=400,
            autofocus=True
        )

        dialog = ft.AlertDialog(
            title=ft.Text("Selecione um Documento"),
            content=ft.Column([dropdown], tight=True),
            actions=[
                ft.TextButton("Selecionar", on_click=selecionar_documento),
                ft.TextButton("Cancelar", on_click=lambda e: setattr(dialog, 'open', False) or page.update()),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.dialog = dialog
        dialog.open = True
        page.update()

    # Função para inserir registro
    def inserir_registro(e):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("""
                INSERT INTO documentos 
                (periodo, documento, referencia, forma_envio, difusao, dia_do_mes, prazo, envio) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                periodo.value,
                documento.value,
                referencia.value,
                forma_envio.value,
                difusao.value,
                dia_do_mes.value,
                prazo_text.value,
                status_envio.value
            ))
            conn.commit()
            page.snack_bar = ft.SnackBar(
                ft.Text("Documento inserido com sucesso!"),
                bgcolor="green"
            )
        except Exception as e:
            page.snack_bar = ft.SnackBar(
                ft.Text(f"Erro ao inserir documento: {str(e)}"),
                bgcolor="red"
            )
        finally:
            conn.close()
            page.snack_bar.open = True
            page.update()

    # Função para excluir registro
    def excluir_registro(e):
        if not documento.value:
            page.snack_bar = ft.SnackBar(
                ft.Text("Selecione um documento para excluir."),
                bgcolor="red"
            )
            page.snack_bar.open = True
            page.update()
            return

        def confirmar_exclusao(e):
            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                cursor.execute("DELETE FROM documentos WHERE documento = ?", (documento.value,))
                conn.commit()
                page.snack_bar = ft.SnackBar(
                    ft.Text("Documento excluído com sucesso!"),
                    bgcolor="green"
                )
                documento.value = ""
                page.update()
            except Exception as e:
                page.snack_bar = ft.SnackBar(
                    ft.Text(f"Erro ao excluir documento: {str(e)}"),
                    bgcolor="red"
                )
            finally:
                conn.close()
                page.snack_bar.open = True
                page.update()
                confirm_dialog.open = False
                page.update()

        confirm_dialog = ft.AlertDialog(
            title=ft.Text("Confirmar Exclusão"),
            content=ft.Text(f"Tem certeza que deseja excluir o documento '{documento.value}'?"),
            actions=[
                ft.TextButton("Sim", on_click=confirmar_exclusao),
                ft.TextButton("Não", on_click=lambda e: setattr(confirm_dialog, 'open', False) or page.update()),
            ],
        )

        page.dialog = confirm_dialog
        confirm_dialog.open = True
        page.update()

    # Componentes da interface
    documento = ft.TextField(
        label="Título do Documento",
        width=875,
        border_color=ft.Colors.GREY_800,
        suffix=ft.IconButton(
            icon=ft.Icons.SEARCH,
            on_click=mostrar_documentos_dialog,
            tooltip="Buscar documentos existentes"
        )
    )

    periodo = ft.Dropdown(
        label="Periodicidade",
        border_color=ft.Colors.GREY_800,
        width=250,
        options=[ft.dropdown.Option(i) for i in periodo_lista]
    )

    forma_envio = ft.Dropdown(
        label="Forma de Envio",
        border_color=ft.Colors.GREY_800,
        width=245,
        options=[ft.dropdown.Option(i) for i in forma_envio_lista]
    )

    referencia = ft.TextField(
        label="Referência",
        width=360,
        border_color=ft.Colors.GREY_800
    )

    status_envio = ft.Dropdown(
        label="Status",
        border_color=ft.Colors.GREY_800,
        width=240,
        options=[ft.dropdown.Option(i) for i in status_envio_lista]
    )

    dia_do_mes = ft.Dropdown(
        label="Dia do mês",
        border_color=ft.Colors.GREY_800,
        width=110,
        options=[ft.dropdown.Option(str(i)) for i in range(1, 32)]
    )

    difusao = ft.TextField(
        label="Difusão",
        border_color=ft.Colors.GREY_800,
        width=455,
        suffix=ft.IconButton(
            icon=ft.Icons.CONTACT_MAIL,
            tooltip="Selecionar destinatários"
        )
    )

    # DatePicker para o campo de prazo
    date_picker = ft.DatePicker(
        first_date=datetime(2000, 1, 1),
        last_date=datetime(2100, 12, 31)
    )

    def update_prazo(e):
        prazo_text.value = date_picker.value.strftime("%d/%m/%Y")
        page.update()

    date_picker.on_change = update_prazo
    page.overlay.append(date_picker)

    prazo_text = ft.TextField(
        label="Prazo",
        read_only=True,
        width=160,
        border_color=ft.Colors.GREY_800,
        suffix=ft.IconButton(
            icon=ft.Icons.CALENDAR_MONTH,
            on_click=lambda _: date_picker.pick_date(),
            tooltip="Selecionar data"
        )
    )

    # Botões
    btn_inserir = ft.ElevatedButton(
        "INSERIR",
        icon=ft.Icons.ADD,
        color="green",
        width=120,
        on_click=inserir_registro
    )

    btn_excluir = ft.ElevatedButton(
        "EXCLUIR",
        icon=ft.Icons.DELETE,
        color="red",
        width=120,
        on_click=excluir_registro
    )

    # Layout da página
    page.add(
        cabecalho,
        documento,
        ft.Row([periodo, forma_envio, referencia]),
        ft.Row([difusao, status_envio, dia_do_mes]),
        ft.Row([prazo_text]),
        ft.Row([btn_inserir, btn_excluir])
    )

ft.app(target=main)