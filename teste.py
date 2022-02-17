from re import M


def multiplica(a,b):
    m = a * b
    return m


def soma(a,b):
    soma = a + b

    multi = multiplica(a,b)
    print(multi)
    
    return soma


a = 5
b = 10


# programa principal


resultado = soma(a ,b)


print(resultado)