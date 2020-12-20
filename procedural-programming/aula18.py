def divide(p1, p2):
    try:
        return p1 / p2
    except ZeroDivisionError as error:
        print(error)
        raise


try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(error)


def converte_numero(v):
    try:
        v = int(v)
        return v
    except ValueError:
        try:
            v = float(v)
            return v
        except ValueError as error:
            print(error)
            pass


numero = converte_numero(input('Digute um numero: '))

if numero is not None:
    print(numero * 3)
else:
    print('Isso nao é um numero')