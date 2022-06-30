from pkg_resources import ensure_directory
from juridica import Juridica
from fisica import Fisica

class Pessoa(Juridica, Fisica):
    def __init__(self, nome, endereco, idade, registro):
        self.nome = nome
        self.endereco = endereco
        self.idade = idade
        self.registro = registro

        if self.registro == 14:
            Juridica.__init__(self, self.nome, self.endereco, self.registro, self.idade)
            self.pessoa = self.view()
        else:
            Fisica.__init__(self, self.nome, self.endereco, self.registro, self.idade)
            self.pessoa = self.view()

    def __str__(self):
        return self.pessoa

