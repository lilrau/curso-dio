# conjunto = {1, 2, 3, 2, 4, 4, 1}
# print(conjunto)
# conjunto.add(5)
# print(conjunto)
# conjunto.discard(2)
# print(conjunto)
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto1.union(conjunto2)
print(conjunto_uniao)
conjunto_inter = conjunto1.intersection(conjunto2)
print(conjunto_inter)
conjunto_diferenca1 = conjunto1.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print(conjunto_diferenca1)
print(conjunto_diferenca2)
conjunto_dif_sim = conjunto1.symmetric_difference(conjunto2)
print(conjunto_dif_sim)
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
conjunto_animais = set(lista)
print(conjunto_animais)
