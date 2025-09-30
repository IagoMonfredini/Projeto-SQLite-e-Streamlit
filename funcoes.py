import sqlite3

conexao = sqlite3.connect("biblioteca.db")


cursor = conexao.cursor()


def cadastar_livro():
        try:
            titulo = input("Digite o título do livro: ")
            autor = input("Digite o autor do livro: ")
            ano = input("Digite o ano de publicação: ")
            disponivel = "sim"
            cursor.execute('''
            INSERT INTO livros (titulo, autor, ano, disponivel)
            VALUES (?, ?, ?, ?)
            ''', (titulo, autor, ano, disponivel))
            conexao.commit()
            print("Livro cadastrado com sucesso!")
        except Exception as erro:
            print(f"Erro ao cadastrar: {erro}")

