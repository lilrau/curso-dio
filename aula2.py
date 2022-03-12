nome = str(input('Olá, qual o seu nome? \n'))
cap_nome = nome.capitalize()
a = int(input('{}, digite um valor: '.format(cap_nome)))
b = int(input('Digite outro valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao = float(divisao)
print('\nSoma: {} '
      '\nSubtração: {} '
      '\nMultiplicação: {} '
      '\nDivisão: {}'.format(soma,
                             subtracao,
                             multiplicacao,
                             divisao))
print('\n{}, os resultados de sua soma, subtração, multiplicação e divisão são, respectivamente: {}, {}, {} e {}'
      .format(cap_nome,
              soma,
              subtracao,
              multiplicacao,
              divisao))
