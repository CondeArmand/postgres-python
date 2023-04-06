import faker
import random
import datetime
import utilities


# Gerar usuario com as seguintes informações (nome, dtnascimento, tipo, curso)
def generate_usuario():
    fake = faker.Faker('pt_BR')
    nome = fake.name()
    dtnascimento = fake.date_of_birth()
    tipo = random.choice(['aluno', 'professor'])

    if tipo == 'aluno':
        curso = random.choice(['Ciência da Computação', 'Engenharia de Software', 'Engenharia de Computação'])
    else:
        curso = None

    return nome, dtnascimento, tipo, curso


# Gerar livro com as seguintes informações (isbn, area, ano_publicacao)
def generate_livro():
    fake = faker.Faker('pt_BR')
    isbn = fake.isbn13()
    isbn = str(isbn)
    area = random.choice(['Ciência da Computação', 'Engenharia de Software', 'Engenharia de Computação'])
    ano_publicacao = fake.year()

    return isbn, area, ano_publicacao


def generate_locacao():
    fake = faker.Faker('pt_BR')
    hr_locacao = fake.time()
    data_locacao = datetime.date.today() + datetime.timedelta(days=random.randint(1, 30))
    hr_devolucao = fake.time()
    data_devolucao = data_locacao + datetime.timedelta(days=random.randint(1, 30))
    id_usuario = random.randint(1, 1000)
    id_livro = random.randint(1, 500)

    return id_usuario, id_livro, data_locacao, hr_locacao, data_devolucao, hr_devolucao
