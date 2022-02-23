import os

from agenda import Agenda

os.system('cls')

#instanciando objeto
cadastro = Agenda

# Entrada de dados
for c in range(3):
    cadastro.dicionario['nome'] = str(input('nome: '))
    cadastro.dicionario['Telefone'] = str(input('Telefone: '))

    cadastro.lista.append(cadastro.dicionario.copy())

#saida
os.system('cls')
print('AGENDA TELEFONICA------------------------------------------')
print('\nNome\tTelefone')
for registro in cadastro.lista:
    print('',end=' ' + '\n')
    for chave, valor in registro.items():
        print(f'{valor}', end='\t')

print()
print()