import flet as ft
from datetime import datetime
import sqlite3 as sq

# Listas para Combo Box =====================================================================================
periodo_lista = ["Diário", "Semanal", "Quinzenal", "Mensal", "Bimestral", "Trimestral", "Semestral", "Anual", "Extraordinário", "Exporárico", "Investigação Social", "Credenciamento"]
forma_envio_lista = ["Email", "DTI", "Mídia Física", "Via Malote"]
status_envio_lista = ["Finalizado", "Em Produção", "Aguardando Aprovação"]
difusao_lista = ["AR - CPA/M-7", "AC - Criminal", "AC - Público Interno", "AC - Social"]

def main(page: ft.Page):
    
    page.bgcolor = "#090113"
    
    # Informações da tela
    cabecalho = ft.Text("Controle de Fluxo de Documentos", size=28, font_family="Times New Roman", color="#fcd021", italic=True)
    
    # Função para Inserir Registro
    def inserir_registro(e):
        conn = sq.connect("doc.db")
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO documentos (periodo, documento, referencia, forma_envio, difusao, dia_do_mes, prazo, envio) 
            VALUES (?, ?, ?, ?, ?, ?, ?. ?)
        """, (
            documento.value, 
            periodo.value, 
            forma_envio.value, 
            referencia.value, 
            status_envio.value, 
            difusao.value, 
            prazo_text.value
        ))
        conn.commit()
        conn.close()

    # Função para Excluir Registro

    def excluir_registro(e):
        if documento.value:
            conn = sq.connect("doc.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM documentos WHERE documento = ?", (documento.value,))
            conn.commit()
            conn.close()
            documento.value = ""
            page.snack_bar = ft.SnackBar(ft.Text("Registro excluído com sucesso!", color="white"), bgcolor="green")
        else:
            page.snack_bar = ft.SnackBar(ft.Text("Informe a descrição do documento para excluir.", color="white"), bgcolor="red")
        page.snack_bar.open = True
        page.update()

    
    # Componentes para entrada de dados ======================================================================
    documento = ft.TextField(label="Título do Documento", width=875, border_color=ft.Colors.GREY_800, tooltip="Insira o título do documento")
    periodo = ft.Dropdown(label="Periodicidade", border_color=ft.Colors.GREY_800, width=250, options=[ft.dropdown.Option(f"{i}") for i in periodo_lista], tooltip="Informe a periodicidade de confecção do documento")
    forma_envio = ft.Dropdown(label="Forma de Envio", border_color=ft.Colors.GREY_800, width=245, options=[ft.dropdown.Option(f"{i}") for i in forma_envio_lista], tooltip="Informe a forma de envio do documento")
    referencia = ft.TextField(label="Referência", width=360, border_color=ft.Colors.GREY_800, tooltip="Informe qual o documento de referência")
    status_envio = ft.Dropdown(label="Status", border_color=ft.Colors.GREY_800, width=240, options=[ft.dropdown.Option(f"{i}") for i in status_envio_lista], tooltip="Informe qual o status atual do documento")
    dia_do_mes = ft.Dropdown(label="Dia do més", border_color=ft.Colors.GREY_800, width=110, options=[ft.dropdown.Option(f"{i}") for i in range(1, 32)], tooltip="Informe o dia do mês para entrega do documento")
    

    btn_inserir = ft.ElevatedButton("INSERIR", tooltip="Inserir novo documento", icon=ft.Icons.ADD, color="GREEN", icon_color="GREEN", width=120, on_click=inserir_registro)
    btn_editar = ft.ElevatedButton("EDITAR", tooltip="Editar documento", icon=ft.Icons.EDIT, color="#fcd021", icon_color="#fcd021", width=120, on_click=...)
    btn_excluir = ft.ElevatedButton("EXCLUIR", tooltip="Excluir documento", icon=ft.Icons.DELETE, color="RED", icon_color="RED", width=120, on_click=excluir_registro)
    btn_atualizar = ft.ElevatedButton("ATUALIZAR", tooltip="Atualizar o status do documento", icon=ft.Icons.UPDATE, color="BLUE", icon_color="BLUE", width=120, on_click=...)

    # Lógica para a contagem de Prazo
        # O programa deve verificar a data atual

    # Semanal
        # Verificar o dia da semana atual
        # Verificar o dia da semana para envio do documento
        # Verificar se o documento deve ser entregue antes do final de semana ou feriado

    # quinzenal
        # Verificar se o documento deve ser entregue antes do final de semana ou feriado
        # alterar da primeira para a segunda quinzena
        # alterar da segunda para a primeira quinzena

    # mensal
        # Verificar se o documento deve ser entregue antes do final de semana ou feriado
        # somar 30 dias à data-base
        # alterar para o mês seguinte mantendo-se o dia do mês

    # bimestral
        # Verificar se o documento deve ser entregue antes do final de semana ou feriado
        # Alterar para o bimestre seguinte mantendo-se o dia do mês

    # trimestral
        # Verificar se o documento deve ser entregue antes do final de semana ou feriado
        # Alterar para o trimestre seguinte mantendo-se o dia do mês

    # semestral
        # Verificar se o documento deve ser entregue antes do final de semana ou feriado
        # Alterar para o Semestre seguinte mantendo-se o dia do mês

    # anual
        # Verificar se o documento deve ser entregue antes do final de semana ou feriado
        # Alterar para o ano seguinte mantendo-se o dia e o mês

    # exporádico
        # Verificar se o documento deve ser entregue antes do final de semana ou feriado
        # verificar o prazo

    # Controle de visibilidade ===============================================================================
    difusao = ft.TextField(label="Difusão", border_color=ft.Colors.GREY_800, width=455, suffix=ft.IconButton(icon=ft.Icons.CONTACT_MAIL, on_click=lambda e:...), tooltip="Informe para quem o documento deve ser difundido")


    # Campo prazo preenchido através de calendário com DatePicker ============================================
    campo_data = ft.DatePicker()
    prazo_text = ft.TextField(label="Prazo", read_only=True, suffix=ft.IconButton(icon=ft.Icons.CALENDAR_MONTH, tooltip="Selecionar data", on_click=lambda e: abrir_date_picker()),width=160, border_color=ft.Colors.GREY_800,)
    page.overlay.append(campo_data)
    

    # Data selecionada e formatada
    def data_selecionada(e):
        if date_picker.value:
            prazo_text.value = date_picker.value.strftime("%d/%m/%Y")
            page.update()

    # DatePicker escondido
    date_picker = ft.DatePicker(
        on_change=data_selecionada,
        first_date=datetime(2000, 1, 1),
        last_date=datetime(2100, 12, 31)
    )
    page.overlay.append(date_picker)  # Adiciona o DatePicker à página

    def abrir_date_picker():
        date_picker.open = True
        page.update()


    # view_documents()
    page.add(cabecalho,
            documento,
            ft.Row([
                periodo, forma_envio, referencia,
            ]),
            ft.Row([
                difusao, 
                status_envio, 
                dia_do_mes,
                # prazo_text, 
            ]),
            
                btn_atualizar,
 
            ft.Row([
                btn_inserir, btn_editar, btn_excluir, 
            ])
    )

# Executa o app
ft.app(target=main)
