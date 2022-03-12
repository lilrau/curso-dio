#para descobrir qual é maior:
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
if a > b and a > c:
    print('O maior número é {}'.format(a))
elif b > a and b > c:
    print('O maior número é {}'.format(b))
else:
    print('O maior número é {}'.format(c))
#para descobrir se um número é par:
x = int(input('Entre com o primeiro valor: '))
y = int(input('Entre com o segundo valor: '))
resto_x = x % 2
resto_y = y % 2
if resto_x == 0 or resto_y == 0:
    print('Um número par foi digitado.')
else:
    print('Nenhum número par foi digitado.')
#para verificar se as notas foram digitadas corretamente:
m = int(input('Primeiro bimestre: '))
# m = int(input('Primeiro bimestre: '))
# if m > 10:
#      m = int(input('Nota incorreta. Primeiro bimestre: '))
n = int(input('Segundo bimestre: '))
f = int(input('Terceiro bimestre: '))
g = int(input('Quarto bimestre: '))
média = (m + n + f + g) / 4
if m <= 10 and n <= 10 and f <= q0 and g <= 10:
    print('Média: {}.'.format(media))
else:
    print('Foi informada uma nota incorreta.')
