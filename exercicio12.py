nomes = [0] * 5

for x in range(5):
    nomes[x] = input('Digite o nome: ')

print(f'A lista de nomes é: ', end=' ')
for y in range(5):
    print(nomes[y], end=' ')

print()
print(f'A lista inversa de nomes é: ', end=' ')
for y in range(4,-1,-1):
    print(nomes[y], end=' ')
