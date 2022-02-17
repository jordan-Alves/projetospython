import os

#importando a classe Retangulo
from retangulo import Retangulo

os.system('cls')

#instanciando os objetos
retangulo1 = Retangulo
retangulo2 = Retangulo
retangulo3 = Retangulo
retangulo4 = Retangulo

#cabeçalho
print('CALCULOS PARA AREA E PERIMETRO DE UM RETANGULO')

#argumentos para encontrar a area
resultado1 = retangulo1.area(10,5)
resultado2 = retangulo2.area(100,5)

print('AREA---------------------------------------------')
print(f'A area do retangulo é: {resultado1}')
print(f'A area do retangulo é: {resultado2}')
print('-'*70)

#argumentos para encontrar o perimetro
resultado3 = retangulo3.perimetro(10,5)
resultado4 = retangulo4.perimetro(100,5)

print('PERIMETRO-----------------------------------------')
print(f'A area do retangulo é: {resultado3}')
print(f'A area do retangulo é: {resultado4}')
print('-'*70)
print()