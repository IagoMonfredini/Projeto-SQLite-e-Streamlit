import sqlite3
import funcoes as op 

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()


cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        ano INTEGER,
        disponivel TEXT NOT NULL
    )
    ''')
conexao.commit()
print("Tabela 'livros' criada")

while True:
    print("---- Sistema Da Biblioteca ---")
    print("1.Cadastra Livro")
    print("2.Listar Livros")
    print("3.Atualizar Disponibilidade")
    print("4.Remover Livro")
    print("5.Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        op.cadastar_livro()
    elif opcao == "2":  
        op.listar_livros()
    elif opcao == "3":    
        op.atualizar_disponibilidade()
    elif opcao == "4":        
        op.remover_livros()