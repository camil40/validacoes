from django.test import TestCase
from escola.models import Estudante, Curso, Matricula

class ModelEstudanteTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome = "Teste do modelo estudante",
            email = 'teste@gmail.com',
            cpf = "74501596007",
            data_nascimento = "2000-01-01",
            celular = "84 98765-4321"
        )
    def test_verifica_atributos_de_estudantes(self):
        '''Testa os atributos de um estudante quando ele é criado na base de dabos'''
        self.assertEqual(self.estudante.nome, "Teste do modelo estudante")
        self.assertEqual(self.estudante.email, "teste@gmail.com")
        self.assertEqual(self.estudante.cpf, "74501596007")
        self.assertEqual(self.estudante.data_nascimento, "2000-01-01")
        self.assertEqual(self.estudante.celular, "84 98765-4321")
        
class ModelCursoTestCase(TestCase):
    def setUp(self):
        self.curso = Curso.objects.create(
            codigo = "F01",
            descricao = "Teste do modelo curso",
            nivel = "B"
        )
    def test_verifica_atributos_de_curso(self):
        '''Testa os atributos de um curso quando ele é criado na base de dados'''
        self.assertEqual(self.curso.codigo, "F01")
        self.assertEqual(self.curso.descricao, "Teste do modelo curso")
        self.assertEqual(self.curso.nivel, "B")
        
class ModelMatriculaTestCase(TestCase):
    def setUp(self):
        self.estudante = Estudante.objects.create(
            nome="Teste do modelo estudante",
            email="teste@gmail.com",
            cpf="74501596007",
            data_nascimento="2000-01-01",
            celular="84 98765-4321"
        )
        self.curso = Curso.objects.create(
            codigo="F01",
            descricao="Teste do modelo curso",
            nivel="B"
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo="M"
        )
    def test_verifica_atributos_de_matricula(self):
        '''Testa os atributos de um curso quando ele é criado na base de dados'''
        self.assertEqual(self.matricula.estudante, self.estudante)
        self.assertEqual(self.matricula.curso, self.curso)
        self.assertEqual(self.matricula.periodo, "M")