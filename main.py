from pessoa import Pessoa


if __name__ == "__main__":
    try:
        nome = str(input("Nome: "))
        endereco = str(input("Endereço: "))
        registro = str(input("CPF/CNPJ: "))
        idade = int(input("Idade: "))

        verificador_conversor = int(registro)

        print("\nCarregando!\n")

        if len(registro) == 14 or len(registro) == 11:
            user = Pessoa(nome, endereco, registro, idade)
            print("Os seus dados são.....\n")
            print(user)
            print("\nFinalizando sistema.....\n")
        else:
            print("Valor passado de CPF/CNPJ não é válido!\n")

    except ValueError:
        print("Dado informado não é um número válido!\n")