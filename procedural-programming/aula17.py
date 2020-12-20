try:
    print('a')
    a = []
    print(a[1])
except NameError as error:
    print('Erro', error)
except (IndexError, KeyError) as error:
    print('Erro', error)
except Exception as error:
    print('Ocorreu um erro inesperado.')