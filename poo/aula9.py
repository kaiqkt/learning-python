class Error(Exception):
    pass


def testar():
    raise Error('Errado')


try:
    testar()
except Error as error:
    print(error)