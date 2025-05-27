import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Verificador de Prazo"
    page.padding = 20
    # page.bgcolor = "#f8f9fa"

    resultado = ft.Text(value="", size=20)

    campo_data_entrega = ft.TextField(
        label="Data de entrega (dd/mm/yyyy)",
        hint_text="Ex: 30/05/2025",
        width=250
    )

    def verificar_prazo(e):
        try:
            data_entrega = datetime.strptime(campo_data_entrega.value, "%d/%m/%Y")
            data_hoje = datetime.now()
            dias_restantes = (data_entrega - data_hoje).days - 1

            if dias_restantes > 0:
                resultado.value = f"⏳ Faltam {dias_restantes} dias para o prazo."
                resultado.color = "green"
            elif dias_restantes == 0:
                resultado.value = "⚠️ O prazo é hoje!"
                resultado.color = "orange"
            else:
                resultado.value = f"❌ Prazo vencido há {-dias_restantes} dias."
                resultado.color = "red"
        except ValueError:
            resultado.value = "⚠️ Data inválida. Use o formato dd/mm/yyyy."
            resultado.color = "red"
        page.update()

    botao_verificar = ft.ElevatedButton(
        "Verificar Prazo", icon=ft.Icons.SCHEDULE, on_click=verificar_prazo
    )

    page.add(
        ft.Text("Verificador de Dias para o Prazo", size=24, weight="bold"),
        campo_data_entrega,
        botao_verificar,
        resultado
    )

ft.app(target=main)
