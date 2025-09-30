Aqui está um **README.md** que documenta o funcionamento do seu projeto da biblioteca:

---

# 📚 Sistema de Biblioteca (SQLite + Python)

Este projeto é um sistema simples de gerenciamento de livros utilizando **Python** e **SQLite**.
Ele permite **cadastrar, listar, atualizar e remover** livros do banco de dados `biblioteca.db`.

---

## 📂 Estrutura do Projeto

* **biblioteca.db** → Banco de dados SQLite que armazena as informações dos livros.
* **funcoes.py** → Contém as funções responsáveis pelas operações no banco de dados (CRUD).
* **main.py** → Arquivo principal que cria a tabela e exibe o menu de navegação do sistema.

---

## ⚙️ Funcionalidades

### 1. **Cadastrar Livro**

* Insere um novo livro no banco com os seguintes dados:

  * Título
  * Autor
  * Ano de publicação
  * Disponibilidade (padrão: `sim`)

### 2. **Listar Livros**

* Exibe todos os livros cadastrados com:

  * ID
  * Título
  * Autor
  * Ano
  * Disponibilidade

### 3. **Atualizar Disponibilidade**

* Atualiza o campo `disponivel` de um livro específico (ex.: de `sim` para `não`).

### 4. **Remover Livro**

* Remove um livro do banco a partir do seu **ID**.

### 5. **Sair**

* Encerra o programa.

---

## 🛠️ Como Executar

1. Certifique-se de ter o **Python 3** instalado.
2. Clone ou copie os arquivos do projeto.
3. Execute o arquivo principal:

```bash
python main.py
```

4. Use o menu interativo para navegar pelo sistema.

---

## 🗄️ Estrutura da Tabela no Banco

A tabela **livros** é criada automaticamente caso não exista, com os seguintes campos:

| Campo        | Tipo    | Descrição                            |
| ------------ | ------- | ------------------------------------ |
| `id`         | INTEGER | Identificador único (chave primária) |
| `titulo`     | TEXT    | Nome do livro                        |
| `autor`      | TEXT    | Nome do autor                        |
| `ano`        | INTEGER | Ano de publicação                    |
| `disponivel` | TEXT    | Situação (`sim` ou `não`)            |

---

## 🚀 Melhorias Futuras

* Implementar interface gráfica (ex.: **Tkinter** ou **Streamlit**).
* Adicionar busca por título/autor.
* Exportar lista de livros para CSV/Excel.
* Melhorar validações de entrada.

