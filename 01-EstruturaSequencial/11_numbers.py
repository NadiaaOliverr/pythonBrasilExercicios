''''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo.'''

number_one_int = int(input())
number_two_int = int(input())
number_three_real = float(input())

operation_one = (2 * number_one_int) * (number_two_int / 2)
operation_two = (3 * number_one_int) + number_three_real
operation_three = (number_three_real**3)

print(operation_one)
print(operation_two)
print(operation_three)