# Exercício 8
"""
Escreva um programa que inicialize uma variável com o valor 5 para representar o número de milhas. Depois, converta esse valor para quilômetros e depois para metros, usando km = milhas / 0.62137 e metros = 1000 * km. Imprima o resultado na seguinte forma:

milhas
5
km
8.04672
metros
8046.72
"""

milhas = 5
km = round(milhas / 0.62137,5)
metros = round(1000 * km,2)

print ("milhas")
print (milhas)
print ("km")
print (km)
print ("metros")
print (metros)
