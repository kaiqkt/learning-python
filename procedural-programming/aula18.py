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
