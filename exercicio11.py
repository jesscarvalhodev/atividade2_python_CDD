numeros = [0] * 30
for x in range(30):
    numeros[x] = int(input('Digite um número: '))

qtd = 0
num = int(input('Digite o número a ser pesquisado: '))
for y in range(30):
    if num == numeros[y]:
        qtd += 1

print(f'O número {num} aparece {qtd} vezes na lista')
