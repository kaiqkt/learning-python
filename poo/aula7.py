class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.class_name = self.__class__.__name__

    def falar(self):
        print(f"{self.class_name} esta falando")

class Cliente(Pessoa):
    pass


class Aluno(Pessoa):
    pass


cliente = Cliente("Kaique", 19)
cliente.falar()