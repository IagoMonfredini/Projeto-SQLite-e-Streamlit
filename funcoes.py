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

def listar_livros():
        try:
            cursor.execute('SELECT * FROM livros')
            livros = cursor.fetchall()
            if livros:
                for livro in livros:
                    print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]} | Disponível: {livro[4]}")
            else:
                print("Nenhum livro cadastrado.")
        except Exception as erro:
            print(f"Erro ao listar livros: {erro}")
            
def atualizar_disponibilidade():
            try:
                id_livro = input("Digite o ID do livro que deseja atualizar: ")
                nova_disponibilidade = input("Digite a nova disponibilidade (sim/não): ")
                cursor.execute('''
                UPDATE livros
                SET disponivel = ?
                WHERE id = ?
                ''', (nova_disponibilidade, id_livro))
                conexao.commit()
                if cursor.rowcount > 0:
                    print("Disponibilidade atualizada com sucesso!")
                else:
                    print("Livro não encontrado.")
            except Exception as erro:
                print(f"Erro ao atualizar livro: {erro}")
                
def remover_livros():
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()
        id_removido = int(input("Digite o id do livro que deseja excluir: "))
        cursor.execute("DELETE FROM livros WHERE id = ?", (id_removido,))     
        conexao.commit()
        if cursor.rowcount > 0:
            print("Livro removido com sucesso!")
        else:
            print("Nenhum livro encontrado com o ID fornecido.")
    except Exception as erro:
        print(f"Erro ao tentar excluir Livro: {erro}")

    finally:
        if conexao:
            conexao.close()

