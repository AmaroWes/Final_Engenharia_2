class Juridica:
    def __init__(self, nome, endereco, registro, idade):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = registro
        self.idade = idade

    def __str__(self):
        dados = self.view()
        return dados
    
    def view(self):
        return f"Nome: {self.nome} \nIdade: {self.idade} \nCNPJ: {self.cnpj} \nEndereço: {self.endereco}"