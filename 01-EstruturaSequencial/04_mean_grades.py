'''Faça um Programa que peça as 4 notas bimestrais 
e mostre a média.'''
from functools import reduce
grades = []
for i in range(4):
    grade = float(input())
    grades.append(grade)

sum_grades = reduce(
    (lambda value_one, value_two: value_one + value_two), grades)
mean_grades = sum_grades / 4
print(f'The mean of grades informed is {mean_grades}')
