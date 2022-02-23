import os


from equacao import Equacao

os.system('cls')

#instanciando o objeto
equacao1 = Equacao

#invocando a função cálculo
x1, x2 = equacao1.equacao(1, 5, -6)

#saida
print('-'*70)
print(f'o valor de x1; {x1}')
print(f'o valor de x2: {x2}')
print('-'*70)

print()