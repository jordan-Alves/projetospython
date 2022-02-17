#Curso Tecnico de Informatica
#Autor: Sebastiao Marcos
#Data de incio: 16/02/2022
#Termino:16/02/2022
#orientação a objetos

import os

#importando a classe pessoa
from pessoa import Pessoa

os.system('cls')

#criando as instancias e passando os argumentos
john = Pessoa('John Doe', 50,1970)
jane = Pessoa('Jane Smith',40,1980)

#saida
print('-'*70)
print(john)
print('-'*70)
print(jane)
print('-'*70)
print()