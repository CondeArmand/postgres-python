import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import data_generator
import utilities

conn = psycopg2.connect(database="biblioteca", host="localhost", user="postgres", password="montepicos")
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cursor = conn.cursor()

# connection check
if conn:
    print("Connection successful!")
else:
    print("Connection failed!")

while True:
    opcao = input(
        "1 - Gerar dados\n2 - Consultar dados\n3 - manipular o sql\n4 - Consultar a quantidade de dados\n"
        "5 - Sair\nOpção: ")
    if opcao == "1":

        opcao2 = input("1 - Gerar usuários\n2 - Gerar livros\n3 - Gerar locações\nOpção: ")
        if opcao2 == "1":

            quantidade = int(input("Quantos usuários deseja gerar? "))
            print("Gerando usuários...")

            for i in range(quantidade):
                usuario = data_generator.generate_usuario()
                cursor.execute("INSERT INTO usuarios (nome, dtnascimento, tipo, curso) VALUES (%s, %s, %s, %s)",
                               usuario)

        elif opcao2 == "2":

            quantidade = int(input("Quantos livros deseja gerar? "))
            print("Gerando livros...")

            for i in range(quantidade):
                livro = data_generator.generate_livro()
                cursor.execute("INSERT INTO livros (isbn, area, ano_publicacao) VALUES (%s, %s, %s)", livro)

        elif opcao2 == "3":

            quantidade = int(input("Quantas locações deseja gerar? "))
            print("Gerando locações...")

            for i in range(quantidade):
                locacao = data_generator.generate_locacao()
                cursor.execute(
                    "INSERT INTO locacao (id_usuario, id_livro, dtemprestimo, hremprestimo, dtdevolucao, hrdevolucao) "
                    "VALUES (%s, %s, %s, %s, %s, %s)", locacao)

    elif opcao == "2":
        opcao2 = input("1 - Consultar usuários\n2 - Consultar livros\n3 - locações\nOpção: ")

        if opcao2 == "1":
            cursor.execute("SELECT * FROM usuarios")
            utilities.print_select(cursor)

        elif opcao2 == "2":
            cursor.execute("SELECT * FROM livros")
            utilities.print_select(cursor)

        elif opcao2 == "3":
            cursor.execute("SELECT * FROM locacao")
            utilities.print_select(cursor)

    elif opcao == "3":

        while True:
            sql = input("SQL> ")
            if sql == "exit":
                break
            cursor.execute(sql)
            utilities.print_select(cursor)

    elif opcao == "4":
        opcao2 = input("1 - Consultar usuários\n2 - Consultar livros\n3 - Consultar Locações\nOpção: ")

        if opcao2 == "1":
            cursor.execute("SELECT COUNT(*) FROM usuarios")
            utilities.print_select(cursor)

        elif opcao2 == "2":
            cursor.execute("SELECT COUNT(*) FROM livros")
            utilities.print_select(cursor)

        elif opcao2 == "3":
            cursor.execute("SELECT COUNT(*) FROM locacao")
            utilities.print_select(cursor)

    elif opcao == "5":
        break

conn.close()
