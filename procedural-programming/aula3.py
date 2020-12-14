var = 'valor'


def func():
    print(var)


def func2(arg=None):
    global var
    var = 'a'
    arg = var
    print(var)
    return arg


func()
outra_variavel = func2(arg=var)

print(outra_variavel)
