'''Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.'''
earn_hours = int(input('How much do you earn per hour?\n'))
job_hours = int(input('Number hours worked per month\n'))
total_salary = earn_hours * job_hours
print(f'Total salary in month = R$ {total_salary}')