
lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[3]
    print('fechando arquivo')
    arquivo.close()
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
# except ArithmeticError:
#     print('Houve um erro ao realizar uma operação aritmética')
except IndexError:
    print('Erro ao acessar indíce inválido da lista')
except Exception as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção.')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()
