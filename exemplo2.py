import datetime  # Adicionamos a biblioteca datetime para lidar com datas reais.

class Paciente:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __str__(self):
        return f"{self.nome}, {self.idade} anos, Endereço: {self.endereco}"


class RegistroPaciente:
    def __init__(self, paciente, sintomas, diagnostico, tratamento):
        self.paciente = paciente
        self.sintomas = sintomas
        self.diagnostico = diagnostico
        self.tratamento = tratamento
        self.data_registro = None

    def registrar(self):
        # Obtemos a data e hora atuais
        now = datetime.datetime.now()
        self.data_registro = now.strftime("Data de registro: %Y-%m-%d %H:%M:%S")
        print("Registro salvo com sucesso!")

    def __str__(self):
        return f"Registro para {self.paciente.nome} em {self.data_registro}\nSintomas: {self.sintomas}\nDiagnóstico: {self.diagnostico}\nTratamento: {self.tratamento}"


class Hospital:
    def __init__(self, nome):
        self.nome = nome
        self.registros = []

    def adicionar_registro(self, registro):
        registro.registrar()
        self.registros.append(registro)

    def mostrar_registros(self):
        for registro in self.registros:
            print(registro)

    def inserir_registro(self):
        nome = input("Nome do paciente: ")
        idade = int(input("Idade do paciente: "))
        endereco = input("Endereço do paciente: ")
        sintomas = input("Sintomas: ")
        diagnostico = input("Diagnóstico: ")
        tratamento = input("Tratamento: ")

        paciente = Paciente(nome, idade, endereco)
        registro = RegistroPaciente(paciente, sintomas, diagnostico, tratamento)
        self.adicionar_registro(registro)


# Exemplo de uso:
hospital = Hospital("Hospital XYZ")

# Inserindo manualmente um registro
paciente1 = Paciente("João", 30, "Rua A, 123")
registro1 = RegistroPaciente(paciente1, "Febre, Dor de cabeça", "Gripe", "Repouso e medicamentos")
hospital.adicionar_registro(registro1)

# Inserindo um registro via entrada do usuário
hospital.inserir_registro()

# Mostrando todos os registros
hospital.mostrar_registros()
