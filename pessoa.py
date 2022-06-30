from pkg_resources import ensure_directory
from juridica import Juridica
from fisica import Fisica

class Pessoa:
    def __init__(self, nome, endereco, idade, registro):
        self.nome = nome
        self.endereco = endereco
        self.idade = idade
        self.registro = registro

        if self.registro == 14:
            self.pessoa = Juridica(self.nome, self.endereco, self.idade, self.registro)
        else:
            self.pessoa = Fisica(self.nome, self.endereco, self.idade, self.registro)

    def __str__(self):
        out_put = self.pessoa.view()
        return out_put

