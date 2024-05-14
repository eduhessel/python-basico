# indice         0  1  2  3  4
# negativo       0 -4 -3 -2 -1
listarNumeros = [1, 2, 3, 4, 5]

# Puxando a lista de números
print('Lista de números:', listarNumeros)

# Pegando o primeiro item da lista de números
print('Primeiro elemento:', listarNumeros[0])

# Pegando o último item da lista de números
print('Ultimo elemento:', listarNumeros[-1])

# Adicionando um único item ao final da lista usando append()
listarNumeros.append(6)
print('Lista após adicionar um item usando append():', listarNumeros)

# Adicionando múltiplos itens ao final da lista usando extend()
listarNumeros.extend([7, 8, 9])
print('Lista após adicionar múltiplos itens usando extend():', listarNumeros)

# Adicionando um item na posição 2 da lista insert()
listarNumeros.insert(2, 10)
print('Lista após adicionar um item na posição 2:', listarNumeros)

# Removendo o número 2 da lista usando remove()
listarNumeros.remove(2)
print('Lista após remover o número 2:', listarNumeros)

# Para cada item da lista, liste o número
for item in listarNumeros:
    print(item * 10)

# Se o número estiver na lista de números printe a mensagem e se não estiver printe outra mensagem
if 3 in listarNumeros:
    print('O número está na lista.')
else:
    print('O número não está na lista.')