from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class EstudantesRequisicoesTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste', password='teste')
        user = authenticate(username='teste', password='teste')
        self.client.force_login(user)
        self.url = reverse('Estudantes-list')
        self.detail_url_name = 'Estudantes-detail'

    def test_get_estudantes(self):
        print("Usuário autenticado:", self.client.session['_auth_user_id'])
        response = self.client.get(self.url)
        print('Response status code:', response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_estudante(self):
        data = {'name': 'Novo Estudante', 'age': 21}
        response = self.client.post(self.url, data)
        print('Response status code:', response.status_code)
        print('Response data:', response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_estudante(self):
        data = {'name': 'Estudante Existente', 'age': 22}
        post_response = self.client.post(self.url, data)
        print('Post response status:', post_response.status_code)
        print('Post response data:', post_response.data)
        estudante_url = reverse(self.detail_url_name, args=[post_response.data.get('id')])
        update_data = {'name': 'Estudante Atualizado', 'age': 23}
        put_response = self.client.put(estudante_url, update_data)
        print('PUT response status:', put_response.status_code)
        print('PUT response data:', put_response.data)
        self.assertEqual(put_response.status_code, status.HTTP_200_OK)

    def test_delete_estudante(self):
        data = {'name': 'Estudante para Deletar', 'age': 22}
        post_response = self.client.post(self.url, data)
        print('Post response status:', post_response.status_code)
        print('Post response data:', post_response.data)
        estudante_url = reverse(self.detail_url_name, args=[post_response.data.get('id')])
        delete_response = self.client.delete(estudante_url)
        print('DELETE response status:', delete_response.status_code)
        print('DELETE response data:', delete_response.data)
        self.assertEqual(delete_response.status_code, status.HTTP_204_NO_CONTENT)


