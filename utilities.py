import faker
import random
import datetime


# Imprimir o resultado do select no console em forma de lista

def print_select(cursor):
    # imprimir de forma tratada
    for row in cursor.fetchall():
        print(row)


# Contar a quantidade de dados retornados

def how_many_rows_back(cursor):
    count = 0
    for row in cursor.fetchall():
        count += 1
    print(count)
