from rest_framework import serializers
from escola.models import Estudante, Curso, Matricula
import re
from datetime import datetime
from escola.validators import  cpf_invalido, nome_invalido, celular_invalido, descricao_invalido, nivel_invalido, periodo_invalido

class EstudanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','cpf','data_nascimento','celular']
    
    def validate(self, dados):
        if cpf_invalido(dados['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter 11 dígitos!'})
        if nome_invalido(dados['nome']): 
            raise serializers.ValidationError({'nome': 'O nome só pode ter letras!'})
        if celular_invalido(dados['celular']):
            raise serializers.ValidationError({'celular': 'O celular precisa ter 13 dígitos!'})
        return dados
    
    def validate_email(self, email):
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(regex, email):
            raise serializers.ValidationError('E-mail inválido!')
        return email
    def validate_data(self, data):
        try:
            data_obj = datetime.strptime(data, "%d/%m/%Y")
            ano_atual = datetime.now().year
            if not (ano_atual - 100 <= data_obj.year <= ano_atual):
                raise serializers.ValidationError('Data fora do intervalo de 100 anos!')
            return data
        except ValueError:
            raise serializers.ValidationError('Formato de data inválido!')

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
    def validate(self, dados):
        if descricao_invalido(dados['descricao']):
            raise serializers.ValidationError('A descrição deve ter entre 100 e 500 caracteres.')
        if nivel_invalido(dados['nivel']):
            raise serializers.ValidationError("Escolha entre 'B' (Básico), 'I' (Intermediário) ou 'A' (Avançado)")
        return dados

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []
    def validate_periodo(self, dados):
        if periodo_invalido(dados['periodo']):
            raise serializers.ValidationError("Escolha entre 'B' (Básico), 'I' (Intermediário) ou 'A' (Avançado)")
        return dados

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso','periodo']
    def get_periodo(self,obj):
        return obj.get_periodo_display()

class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source = 'estudante.nome')
    class Meta:
        model = Matricula
        fields = ['estudante_nome']
        
        
class EstudanteSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Estudante
        fields = ['id','nome','email','celular']