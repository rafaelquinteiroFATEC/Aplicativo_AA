import sqlite3

def cria_bd():
    # Conectar ao banco de dados (se não existir, será criado)
    conexao = sqlite3.connect("bd_trafico.sqlite3")
    cursor = conexao.cursor()

    # Criar tabela "ocorrencia"
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ocorrencia (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sequencia TEXT NOT NULL,
        natureza TEXT NOT NULL,
        talao TEXT NOT NULL,
        data TEXT NOT NULL,
        logradouro TEXT NOT NULL,
        numero TEXT,
        bairro TEXT NOT NULL,
        municipio TEXT NOT NULL,
        latitude REAL,
        longitude REAL
    )
    """)

    # Criar tabela "militares"
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS militares (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_ocorrencia INTEGER,
        posto_grad TEXT NOT NULL,
        RE TEXT NOT NULL,
        nome_militar TEXT NOT NULL,
        btl TEXT NOT NULL,
        cia TEXT NOT NULL,
        funcao TEXT NOT NULL,
        viatura TEXT NOT NULL,
        FOREIGN KEY (id_ocorrencia) REFERENCES ocorrencia(id) ON DELETE CASCADE
    )
    """)

    # Criar tabela "envolvidos"
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS envolvidos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_ocorrencia INTEGER,
        nome_envolvido TEXT NOT NULL,
        RG TEXT NOT NULL,
        condicao TEXT NOT NULL,
        FOREIGN KEY (id_ocorrencia) REFERENCES ocorrencia(id) ON DELETE CASCADE
    )
    """)

    # Criar tabela "entorpecentes"
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS entorpecentes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_ocorrencia INTEGER,
        tipo_entorpecente TEXT NOT NULL,
        quantidade TEXT NOT NULL,
        FOREIGN KEY (id_ocorrencia) REFERENCES ocorrencia(id) ON DELETE CASCADE
    )
    """)

    # Salvar e fechar conexão
    conexao.commit()
    conexao.close()

    print("Banco de dados criado com sucesso! 🚀")
