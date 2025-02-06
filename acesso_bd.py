import sqlite3

class Trafico:
    def __init__(self, btl, cia, rua, numero: int, bairro, municipio, data, quantidade: float, tipo_entorpecente, traficante, nome, rg, vulgo, comparsa, viatura, militar, talao):
        self.btl = btl
        self.cia = cia
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.municipio = municipio
        self.data = data
        self.quantidade = quantidade
        self.tipo_entorpecente = tipo_entorpecente
        self.traficante = traficante
        self.nome = nome  
        self.rg = rg
        self.vulgo = vulgo
        self.comparsa = comparsa
        self.viatura = viatura
        self.militar = militar
        self.talao = talao

    @staticmethod
    def bd_trafico_entorpecentes():
        """Cria as tabelas no banco de dados SQLite"""
        conexao = sqlite3.connect("bd_trafico.sqlite3")
        cursor = conexao.cursor()

        # Criando a tabela de ocorrências
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS ocorrencia (
                sequencia INTEGER PRIMARY KEY AUTOINCREMENT,
                btl TEXT,
                cia TEXT,
                rua TEXT,
                numero TEXT,
                bairro TEXT,
                municipio TEXT,
                coord_lat REAL,
                coord_long REAL,   
                data TEXT,
                quantidade REAL DEFAULT 0,
                tipo_entorpecente TEXT,
                talao TEXT
            )
        ''')

        # Criando a tabela de traficantes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS traficante (
                sequencia INTEGER PRIMARY KEY AUTOINCREMENT,
                traficante TEXT,
                nome TEXT,
                rg TEXT
            )
        ''')

        # Criando a tabela da equipe policial
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS equipe_policial (
                sequencia INTEGER PRIMARY KEY AUTOINCREMENT,
                re TEXT,
                nome TEXT,
                viatura TEXT
            )
        ''')

        # Criando a tabela de comparsas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS comparsa (
                sequencia INTEGER PRIMARY KEY AUTOINCREMENT,
                comparsa TEXT,
                nome TEXT,
                rg TEXT,
                vulgo TEXT
            )
        ''')

        conexao.commit()
        conexao.close()

# Executando a criação do banco de dados
Trafico.bd_trafico_entorpecentes()
