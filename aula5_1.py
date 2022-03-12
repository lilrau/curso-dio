#tupla é imutavel, lista é mutavel
tupla = (1, 10, 12, 14)
print(tupla)
print(tupla[2])
print(len(tupla))
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
lista_numerica = list(tupla)
print(type(lista_numerica))
print(lista_numerica)
lista_numerica[0] = 100
print(lista_numerica)
