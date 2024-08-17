# Exercício 3
""" Escreva um programa que pede para o usuário entrar uma certa quantidade de minutos. O programa deve fazer a conversão dessa quantidade em minutos para o formato hora:minuto. Por exemplo, caso o usuário passe o valor de 80 o programa deve mostrar paro o usuário que isso é equivalente a 1h20m. O seu código deve conter comentários para explicar o que está fazendo nas principais linhas
"""

# Escreva seu código aqui

minutos_entrada = input ('Insira a qtd de min: ')
minutos_entrada_int = int(minutos_entrada)
horas = minutos_entrada_int // 60
minutos = minutos_entrada_int % 60
print (f'O total de horas é de: {horas}:{minutos}')