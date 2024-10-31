from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class AuthenticationUserTestCase(APITestCase):
    def setUp(self):
        self.usuario = User.objects.create_superuser(username='admin', password='admin')
        self.url = reverse('Estudantes-list')
        
    def test_autenticacao_user_com_credenciais_corretas(self):
        '''Teste que verifica se o login esta acontecendo de forma correta'''
        usuario = authenticate(username='admin',password='admin')
        self.assertTrue((usuario is not None) and usuario.is_authenticated)
        
    def test_autenticacao_user_com_username_incorreto(self):
        '''Teste que verifica se o login vai acusar erro se o username está errado'''
        usuario = authenticate(username='admn',password='admin')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)
        
    def test_autenticacao_user_com_senha_incorreta(self):
        '''Teste que verifica se o login vai acusar erro se a senha está errada'''
        usuario = authenticate(username='admin',password='admn')
        self.assertFalse((usuario is not None) and usuario.is_authenticated)
        

class AuthenticationUserAcessTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='teste',password='teste')
        login_successful = self.client.login(username='teste', password='teste') 
        print('Login successful:', login_successful)

    def test_user_logado_tem_acesso_a_rota_estudantes(self):
        '''Teste que verifica se o usuario logado tem acessoa arota'''
        url = reverse('Estudantes-list')
        response = self.client.get(url)
        print('Response status code:', response.status_code)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_nao_logado_nao_tem_acesso_a_rota_estudantes(self):
        '''Teste que verifica se o usuario não logado não tem acesso a rota'''
        self.client.logout()  
        url = reverse('Estudantes-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)





