# Calcula a tabuada de um número usando laço de repetição.
n = int(input('Digite um número para calcular a tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {:2}'.format(n, c, c * n))
