from juridica import Juridica
from fisica import Fisica


if __name__ == "__main__":
    try:
        nome = str(input("Nome: "))
        endereco = str(input("Endereço: "))
        registro = str(input("CPF/CNPJ: "))
        idade = int(input("Idade: "))

        verificador_conversor = int(registro)

        if len(registro) == 14:
            user = Juridica(nome, endereco, registro, idade)
            print(user)
        elif len(registro) == 11:
            user = Fisica(nome, endereco, registro, idade)
            print(user)
        else:
            print("Valor passado de CPF/CNPJ não é válido!\n")

    except ValueError:
        print("Dado informado não é um número válido!\n")