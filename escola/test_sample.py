import pytest
from .models import Estudante

'''Testar a criação de instancias'''
@pytest.mark.django_db
def test_criacao_estudante():
    aluno = Estudante.objects.create(nome="João", idade=15, classe="9º Ano", data_nascimento="1998-07-14", celular="84 99900-1122")
    assert aluno.nome == "João"
    assert aluno.email == 15
    assert aluno.cpf == "9º Ano"
    assert aluno.data_nascimento == "1998-07-14"
    assert aluno.celular == "84 99900-1122"