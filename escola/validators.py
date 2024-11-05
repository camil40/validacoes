'''Arquivo criado para isolar as condições de validação das informações necessarias'''

def cpf_invalido(cpf):
    return len(cpf) != 11

def nome_invalido(nome):
	return  not nome.isalpha()

def celular_invalido(celular):
	return len(celular)  != 13

def descricao_invalido(descricao):
    return len(descricao) < 100 or len(descricao) > 500


def nivel_invalido(valid_nivel):
    return valid_nivel == ['B', 'I', 'A']

def periodo_invalido(valid_periodos):
    return valid_periodos == ['M', 'V', 'N']
        
        