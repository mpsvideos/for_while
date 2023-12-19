"""
Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso
e optou por não ter um 13ro andar.

Escreva um código que imprima todos os números exceto o número 13.
Escreva mais um código que resolva o mesmo problema, mas dessa vez usando o laço de repetição 'while'.

Como desafio, imprima eles em ordem decrescente (20, 19, 18...)
"""

print('Laço de repetição utilizando FOR.')
for i in range(1, 21):
    if i == 13:
        continue
    print(i, end=' ')

print('\n')
print('Laço de repetição utilizando WHILE.')
contador = 0
while contador < 20:
    contador += 1
    if contador == 13:
        continue
    print(contador, end=' ')

print('\n')
print('Lista dos números invertidos.')
for i in range(21, 1, -1):
    if i == 13:
        continue
    print(i, end=' ')
