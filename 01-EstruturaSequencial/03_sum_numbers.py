'''Faça um Programa que peça dois números e imprima a soma.'''
number_one = int(input())
number_two = int(input())
sum_numbers = (lambda number_one, number_two: number_one + number_two)
print(f'The sum of numbers {number_one} + {number_two} = {sum_numbers(number_one, number_two)}')
