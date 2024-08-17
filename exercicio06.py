# Exercício 6

""" Abaixo é apresentada a variável palavra. Com relação ao valor da variável palavra responda:

a) Quantas letras possui essa palavra?

b) Quantas vezes a letra 'o' aparece nessa palavra?

c) Qual a posição da letra v nessa palavra?

d) Escreva essa palavra de trás para frente.

e) Divida essa palavra em duas com a mesma quantidade de caracteres.

Você deve utilizar código python para ajudar a responder essas perguntas.
"""

palavra = "pneumoultramicroscopicossilicovulcanoconiotico"

# Item a - Quantas letras possui essa palavra?
letra_a = len(palavra)
print (letra_a)

# Item b - Quantas vezes a letra 'o' aparece nessa palavra?
letra_b = palavra.count('o')
print (letra_b)

# Item c - Qual a posição da letra v nessa palavra?
letra_c = palavra.find ('v')
print (letra_c)

# Item d - Escreva essa palavra de trás para frente.
letra_d = palavra[::-1]
print (letra_d)

# Item e - Divida essa palavra em duas com a mesma quantidade de caracteres.
meio = len(palavra) // 2
primeira_parte = palavra[:meio]
segunda_parte = palavra[meio:]
print (primeira_parte)
print (segunda_parte)