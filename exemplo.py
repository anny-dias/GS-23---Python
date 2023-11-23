import json
from datetime import datetime

# Banco de dados
registros = []
prescricoes = []

def salvar_dados():
    with open('registros.json', 'w') as f:
        json.dump(registros, f)
    with open('prescricoes.json', 'w') as f:
        json.dump(prescricoes, f)

def carregar_dados():
    global registros, prescricoes
    try:
        with open('registros.json', 'r') as f:
            registros = json.load(f)
    except FileNotFoundError:
        registros = []
    
    try:
        with open('prescricoes.json', 'r') as f:
            prescricoes = json.load(f)
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

# Função para editar um registro existente
def editar_registro():
    exibir_registros()
    indice = int(input("Digite o índice do registro que deseja editar: "))

    if 0 <= indice < len(registros):
        nome = input("Digite o novo nome do paciente: ")
        idade = int(input("Digite a nova idade do paciente: "))
        descricao = input("Digite a nova descrição do registro: ")

        registros[indice]['nome'] = nome
        registros[indice]['idade'] = idade
        registros[indice]['descricao'] = descricao
        registros[indice]['data'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        salvar_dados()
        print("Registro editado com sucesso!")
    else:
        print("Índice inválido. Tente novamente.")

# Função para editar uma prescrição existente
def editar_prescricao():
    exibir_prescricoes()
    indice = int(input("Digite o índice da prescrição que deseja editar: "))

    if 0 <= indice < len(prescricoes):
        nome_paciente = input("Digite o novo nome do paciente para prescrição: ")
        medicamento = input("Digite o novo nome do medicamento: ")
        dosagem = input("Digite a nova dosagem: ")

        prescricoes[indice]['nome_paciente'] = nome_paciente
        prescricoes[indice]['medicamento'] = medicamento
        prescricoes[indice]['dosagem'] = dosagem
        prescricoes[indice]['data'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        salvar_dados()
        print("Prescrição editada com sucesso!")
    else:
        print("Índice inválido. Tente novamente.")

# Função para prescrever medicamentos
def prescrever_medicamento():
    exibir_registros()
    indice = int(input("Digite o índice do paciente para prescrição: "))

    if 0 <= indice < len(registros):
        nome_paciente = registros[indice]['nome']
        medicamento = input("Digite o nome do medicamento: ")
        dosagem = input("Digite a dosagem: ")

        adicionar_prescricao(nome_paciente, medicamento, dosagem)
        print("Prescrição adicionada com sucesso!")
    else:
        print("Índice inválido. Tente novamente.")

# Função para exibir todos os registros
def exibir_registros():
    for i, registro in enumerate(registros):
        print(f"{i}. Nome: {registro['nome']}, Idade: {registro['idade']}, Descrição: {registro['descricao']}, Data: {registro['data']}")

# Função para exibir todas as prescrições
def exibir_prescricoes():
    for i, prescricao in enumerate(prescricoes):
        print(f"{i}. Nome do Paciente: {prescricao['nome_paciente']}, Medicamento: {prescricao['medicamento']}, Dosagem: {prescricao['dosagem']}, Data: {prescricao['data']}")

# Função para inserir um novo registro
def inserir_registro():
    nome = input("Digite o nome do paciente: ")
    idade = int(input("Digite a idade do paciente: "))
    descricao = input("Digite a descrição do registro: ")
    adicionar_registro(nome, idade, descricao)
    print("Registro inserido com sucesso!")

# Função para inserir uma nova prescrição
def inserir_prescricao():
    nome_paciente = input("Digite o nome do paciente para prescrição: ")
    medicamento = input("Digite o nome do medicamento: ")
    dosagem = input("Digite a dosagem: ")
    adicionar_prescricao(nome_paciente, medicamento, dosagem)
    print("Prescrição inserida com sucesso!")

# Função para exibir o menu de opções
def exibir_menu():
    print("\n=== Menu ===")
    print("1. Inserir Novo Registro")
    print("2. Inserir Nova Prescrição")
    print("3. Exibir Registros")
    print("4. Exibir Prescrições")
    print("5. Editar Registro Existente")
    print("6. Editar Prescrição Existente")
    print("7. Prescrever Medicamento")
    print("8. Sair")

# Carregar dados existentes
carregar_dados()

# Loop do programa
while True:
    exibir_menu()
    escolha = input("Escolha uma opção (1-8): ")

    if escolha == '1':
        inserir_registro()
    elif escolha == '2':
        inserir_prescricao()
    elif escolha == '3':
        exibir_registros()
    elif escolha == '4':
        exibir_prescricoes()
    elif escolha == '5':
        editar_registro()
    elif escolha == '6':
        editar_prescricao()
    elif escolha == '7':
        prescrever_medicamento()
    elif escolha == '8':
        print("Saindo do programa. Até logo!")
        break
    else:
        print
