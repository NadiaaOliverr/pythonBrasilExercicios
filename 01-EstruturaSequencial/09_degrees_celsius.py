'''Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura 
em graus Celsius. C = (5 * (F-32) / 9).'''
from decimal import Decimal, getcontext

# Números com 2 casa de precisão
getcontext().prec = 3

degreesF = float(input('Farenheit: '))
degressC = (5 * Decimal((degreesF - 32) / 9))
print(f'Farenheit: {degreesF}F\nCelsius: {degressC}C')