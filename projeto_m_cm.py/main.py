#curso Técnico de informatica
#Autor: Jordan monteiro
#Data incicio : 22/02/2022
#Término: 22/02/2022
#orientação a objetos
import os

os.system('cls')

from metroscm import metros

valor = metros
print('-------------CONVERSOR DE METROS EM CM----------------')
metro = int(input('Digite o valor em M:'))



resultado = valor.conversao(metro)

print(f'O resultado foi {resultado} CM')