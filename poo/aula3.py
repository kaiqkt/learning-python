"""
 public, protected, private
 _
 __ private (_NameClass__nomeatributo)
"""


class BaseDeDados:
    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def insert_client(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_cliente(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_client(self, id):
        del self.__dados['clientes'][id]


bd = BaseDeDados()
bd.insert_client(1, "Kaique")
print(bd.dados)

