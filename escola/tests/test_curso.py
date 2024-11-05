from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from escola.models import Curso
from escola.serializers import CursoSerializer

class CursoTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Cursos-list')
        self.client.force_authenticate(user=self.usuario)
        self.curso = Curso.objects.create(
            codigo="F01",
            descricao="Descrição suficientemente longa para passar na validação",
            nivel="B"
        )
    
    def test_requisicao_get_para_listar_cursos(self):
        """Teste de requisição GET"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_requisicao_get_para_listar_um_curso(self):
        """Teste de requisição GET para um curso"""
        response = self.client.get(f'{self.url}{self.curso.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dados_curso = Curso.objects.get(pk=self.curso.id)
        dados_curso_serializados = CursoSerializer(instance=dados_curso).data
        self.assertEqual(response.data, dados_curso_serializados)

    def test_requisicao_post_para_criar_um_curso(self):
        """Teste de requisição POST para um curso"""
        dados = {
            'codigo': 'F02',
            'descricao': 'Esta é uma descrição suficientemente longa para atender ao requisito de 100 a 500 caracteres. Devo garantir que esta descrição seja suficientemente detalhada para passar na validação.',
            'nivel': 'I'
        }
        response = self.client.post(self.url, data=dados, format='json')
        print(response.data)  # Depuração
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        curso = Curso.objects.get(pk=response.data['id'])
        self.assertEqual(curso.codigo, 'F02')
        self.assertEqual(curso.descricao, 'Esta é uma descrição suficientemente longa para atender ao requisito de 100 a 500 caracteres. Devo garantir que esta descrição seja suficientemente detalhada para passar na validação.')
        self.assertEqual(curso.nivel, 'I')

    def test_requisicao_delete_um_curso(self):
        """Teste de requisição DELETE um curso"""
        response = self.client.delete(f'{self.url}{self.curso.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_requisicao_put_para_atualizar_um_curso(self):
        """Teste de requisição PUT para um curso"""
        dados = {
            'codigo': 'F01',
            'descricao': 'Descrição atualizada suficientemente longa para passar na validação de 100 a 500 caracteres.',
            'nivel': 'A'
        }
        response = self.client.put(f'{self.url}{self.curso.id}/', data =dados, format='json')
        print(response.data)  # Depuração
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        curso = Curso.objects.get(pk=self.curso.id)
        self.assertEqual(curso.descricao, 'Descrição atualizada suficientemente longa para passar na validação de 100 a 500 caracteres.')
        self.assertEqual(curso.nivel, 'A')