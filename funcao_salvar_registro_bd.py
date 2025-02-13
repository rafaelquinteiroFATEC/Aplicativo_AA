import flet as ft
import sqlite3

# Criando banco de dados e tabela
conn = sqlite3.connect("teste.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS militares (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    posto_grad TEXT,
    re TEXT,
    nome_militar TEXT,
    btl TEXT,
    cia TEXT,
    funcao TEXT,
    viatura TEXT
)
""")
conn.commit()
conn.close()


def main(page: ft.Page):
    # Dicionário para armazenar os dados antes de salvar no banco
    dados = {"posto_grad": [], "re": [], "nome_militar": [], "btl": [], "cia": [], "funcao": [], "viatura": []}

    # Campos de entrada do usuário
    btl = ft.Dropdown(
        label="Batalhão",
        border_color=ft.colors.GREY_800,
        width=130,
        options=[ft.dropdown.Option("31º BPM/M"), ft.dropdown.Option("15º BPM/M"), ft.dropdown.Option("26º BPM/M")]
    )

    cia = ft.Dropdown(
        label="Cia",
        border_color=ft.colors.GREY_800,
        width=80,
        options=[ft.dropdown.Option(str(i)) for i in range(1, 6)]
    )

    posto_grad = ft.Dropdown(
        label="Posto/Grad",
        border_color=ft.colors.GREY_800,
        width=150,
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

    funcao = ft.Dropdown(
        label="Função",
        border_color=ft.colors.GREY_800,
        width=150,
        options=[
            ft.dropdown.Option("encarregado"),
            ft.dropdown.Option("motorista"),
            ft.dropdown.Option("auxiliar"),
        ]
    )

    viatura = ft.TextField(label="Viatura", width=100, border_color=ft.colors.GREY_800, prefix_text="M-")
    re = ft.TextField(label="RE", width=100, border_color=ft.colors.GREY_800)
    nome_militar = ft.TextField(label="Nome do Militar", width=350, border_color=ft.colors.GREY_800)

    # Campo para exibir os dados cadastrados
    output_text = ft.Text()

    # Função para confirmar os dados no dicionário
    def confirmar_dados(e):
        if posto_grad.value and re.value and nome_militar.value and btl.value and cia.value and funcao.value and viatura.value:
            dados["posto_grad"].append(posto_grad.value)
            dados["re"].append(re.value)
            dados["nome_militar"].append(nome_militar.value)
            dados["btl"].append(btl.value)
            dados["cia"].append(cia.value)
            dados["funcao"].append(funcao.value)
            dados["viatura"].append(viatura.value)

            # Atualizando a exibição dos dados armazenados
            output_text.value = str(dados)
            page.update()

            # Limpando os campos após a confirmação
            posto_grad.value = None
            re.value = ""
            nome_militar.value = ""
            btl.value = None
            cia.value = None
            funcao.value = None
            viatura.value = ""

            page.update()
        else:
            output_text.value = "⚠️ Preencha todos os campos antes de confirmar!"
            page.update()

    # Função para enviar os dados do dicionário para o banco de dados
    def enviar_para_banco(e):
        conn = sqlite3.connect("teste.db")
        cursor = conn.cursor()

        for i in range(len(dados["posto_grad"])):  # Percorre todas as entradas do dicionário
            cursor.execute("""
                INSERT INTO militares (posto_grad, re, nome_militar, btl, cia, funcao, viatura)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                dados["posto_grad"][i],
                dados["re"][i],
                dados["nome_militar"][i],
                dados["btl"][i],
                dados["cia"][i],
                dados["funcao"][i],
                dados["viatura"][i]
            ))

        conn.commit()
        conn.close()

        # Limpa os dados do dicionário após enviar
        for key in dados.keys():
            dados[key].clear()

        output_text.value = "✅ Dados enviados para o banco com sucesso!"
        page.update()

    # Botões
    confirmar_btn = ft.ElevatedButton(text="Confirmar", on_click=confirmar_dados)
    enviar_btn = ft.ElevatedButton(text="Enviar para o Banco", on_click=enviar_para_banco)

    # Adicionando elementos à interface
    page.add(posto_grad, re, nome_militar, btl, cia, funcao, viatura, confirmar_btn, enviar_btn, output_text)

ft.app(target=main)
