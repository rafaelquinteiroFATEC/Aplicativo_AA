import flet as ft
from datetime import datetime, timedelta

def main(page: ft.Page):
    page.title = "Somar Dias a uma Data"
    page.padding = 20
    # page.bgcolor = "#f5f5f5"

    resultado = ft.Text(value="", color="blue", size=20)

    # Campo para a data inicial
    campo_data = ft.TextField(
        label="Data (dd/mm/yyyy)", width=200, hint_text="Ex: 26/05/2025"
    )

    # Campo para a quantidade de dias
    campo_dias = ft.TextField(
        label="Quantidade de dias (+ ou -)", width=200, hint_text="Ex: 7 ou -5"
    )

    def calcular(e):
        try:
            data_inicial = datetime.strptime(campo_data.value, "%d/%m/%Y")
            dias = int(campo_dias.value) - 1
            nova_data = data_inicial + timedelta(days=dias)
            resultado.value = f"Nova data: {nova_data.strftime('%d/%m/%Y')}"
            resultado.color = "green"
        except ValueError:
            resultado.value = "⚠️ Verifique a data ou o número de dias."
            resultado.color = "red"
        page.update()

    # Botão para executar o cálculo
    botao_calcular = ft.ElevatedButton(
        "Calcular nova data", icon=ft.Icons.DATE_RANGE, on_click=calcular
    )

    page.add(
        ft.Text("Somador de Dias em Datas", size=24, weight="bold"),
        campo_data,
        campo_dias,
        botao_calcular,
        resultado
    )

ft.app(target=main)
