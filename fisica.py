class Fisica:
    def __init__(self, nome, endereco, registro, idade):
        self.nome = nome
        self.endereco = endereco
        self.cpf = registro
        self.idade = idade

    def __str__(self):
        dados = f"Nome: {self.nome} \nIdade: {self.idade} \nCPF: {self.cpf} \nEndereço: {self.endereco}"
        return dados