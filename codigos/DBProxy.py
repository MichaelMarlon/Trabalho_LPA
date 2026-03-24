import sqlite3


class DBProxy:
    def __init__(self,nome_banco):
        self.nome_banco = nome_banco
        self.conexao = sqlite3.connect(nome_banco)
        self.conexao.execute('''
                            CREATE TABLE IF NOT EXISTS dados(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            pontos INTEGER NOT NULL,
                            data TEXT NOT NULL)''')
    def salvar(self,pontos_dict:dict):
        self.conexao.execute('INSERT INTO dados (nome,pontos,data) VALUES (:nome, :pontos, :data)',pontos_dict)
        self.conexao.commit()


    def rev_top10(self) -> list:
        return self.conexao.execute('SELECT * FROM dados ORDER BY pontos DESC LIMIT 10').fetchall()


    def fechar(self):
        self.conexao.close()
















