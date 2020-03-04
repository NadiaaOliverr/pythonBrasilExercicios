'''Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58'''

from decimal import Decimal, getcontext

getcontext().prec = 3

height = float(input())
ideal_weight = Decimal((72.7 * height)) - 58
print(ideal_weight)