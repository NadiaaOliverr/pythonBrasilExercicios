'''Faça um Programa que peça a temperatura em graus Celsius, 
transforme e mostre em graus Farenheit.'''
from decimal import Decimal, getcontext

# Números com 2 casa de precisão
getcontext().prec = 4

degreesC = float(input('Celsius: '))
degressF = (Decimal(degreesC * 1.8) + 32)
print(f'Farenheit: {degressF}F')