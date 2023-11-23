#Sistemas de gerenciamento eletrônico de registros com prescrição eletrônica

import json
from datetime import datetime

# Banco de dados 
registros = []
prescricoes = []

def salvar_dados():
    with open('registros.json', 'w') as arquivo:
        json.dump(registros, arquivo)
    with open('prescricoes.json', 'w') as arquivo:
        json.dump(prescricoes, arquivo)

def carregar_dados():
    global registros, prescricoes
    try:
        with open('registros.json', 'r', encoding='utf-8') as arquivo:
            registros = json.load(arquivo)
    except FileNotFoundError:
        registros = []
    
    try:
        with open('prescricoes.json', 'r', encoding='utf-8') as arquivo:
            prescricoes = json.load(arquivo)
    except FileNotFoundError:
        prescricoes = []

# Função para adicionar um registro
def adicionar_registro(nome, idade, descricao):
    registro = {
        'nome': nome,
        'idade': idade,
        'descricao': descricao,
        'data': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    registros.append(registro)
    salvar_dados()

# Função para adicionar uma prescrição
def adicionar_prescricao(nome_paciente, medicamento, dosagem):
    prescricao = {
        'nome_paciente': nome_paciente,
        'medicamento': medicamento,
        'dosagem': dosagem,
        'data': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    prescricoes.append(prescricao)
    salvar_dados()

# Função para exibir todos os registros
def exibir_registros():
    for registro in registros:
        print(f"Nome: {registro['nome']}, Idade: {registro['idade']}, Descrição: {registro['descricao']}, Data: {registro['data']}")

# Função para exibir todas as prescrições
def exibir_prescricoes():
    for prescricao in prescricoes:
        print(f"Nome do Paciente: {prescricao['nome_paciente']}, Medicamento: {prescricao['medicamento']}, Dosagem: {prescricao['dosagem']}, Data: {prescricao['data']}")

# Função para inserir um novo registro
def inserir_registro():
    nome = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    descricao = input("Digite a descrição do registro: ")
    adicionar_registro(nome, idade, descricao)
    print("Registro inserido com sucesso!")

# Carregar dados existentes
carregar_dados()

# Exemplo de uso
inserir_registro()
exibir_registros()
