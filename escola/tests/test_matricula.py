from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Matricula, Estudante, Curso
from escola.serializers import MatriculaSerializer

class MatriculaTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Matriculas-list')
        self.client.force_authenticate(user=self.usuario)
        self.estudante = Estudante.objects.create(
            nome='Teste estudante',
            email='testeestudante@gmail.com',
            cpf='68224431002',
            data_nascimento='2024-01-02',
            celular='86 99999-9999'
        )
        self.curso = Curso.objects.create(
            codigo="F01",
            descricao="Teste do modelo curso",
            nivel="B"
        )
        self.matricula = Matricula.objects.create(
            estudante=self.estudante,
            curso=self.curso,
            periodo='M'
        )
    
    def test_requisicao_get_para_listar_matriculas(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_uma_matricula(self):
        """Teste de requisição GET para uma matrícula"""
        response = self.client.get(f'{self.url}{self.matricula.id}/')  # /matriculas/1/
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_matricula = Matricula.objects.get(pk=self.matricula.id)
        dados_matricula_serializados = MatriculaSerializer(instance=dados_matricula).data
        self.assertEqual(response.data, dados_matricula_serializados)

    def test_requisicao_post_para_criar_uma_matricula(self):
        """Teste de requisição POST para uma matrícula"""
        dados = {
            'estudante': self.estudante.id,
            'curso': self.curso.id,
            'periodo': 'M'
        }
        response = self.client.post(self.url, data=dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        matricula = Matricula.objects.get(pk=response.data['id'])
        self.assertEqual(matricula.estudante.nome, 'Teste estudante')
        self.assertEqual(matricula.curso.descricao, 'Teste do modelo curso')
        self.assertEqual(matricula.periodo, 'M')
        

    def test_requisicao_delete_uma_matricula(self):
        """Teste de requisição DELETE uma matrícula"""
        response = self.client.delete(f'{self.url}{self.matricula.id}/')  # /matriculas/1/
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_uma_matricula(self):
        """Teste de requisição PUT para uma matrícula"""
        dados = {
            'estudante': self.estudante.id,
            'curso': self.curso.id,
            'periodo': 'V'
        }
        response = self.client.put(f'{self.url}{self.matricula.id}/', data=dados, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        matricula = Matricula.objects.get(pk=self.matricula.id)
        self.assertEqual(matricula.periodo, 'V')
