lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
print(lista_animal[1])
soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
print(sum(lista))
if 'lobo' in lista_animal:
    print('existe um lobo na lista.')
else:
    print('não existe um lobo na lista. Será incluído.')
    lista_animal.append('lobo')
    print(lista_animal)
# nova_lista = lista_animal * 3
# print(nova_lista)
lista_animal.remove('elefante')
print(lista_animal)
# lista_animal.pop(0)
# print(lista_animal)
lista.sort()
lista_animal.sort()
print(lista_animal)
print(lista)
lista_animal.reverse()
print(lista_animal)
lista_animal[0] = 'macaco'
print(lista_animal)
