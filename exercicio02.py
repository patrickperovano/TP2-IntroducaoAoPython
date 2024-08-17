# Exercício 2
"""
Considere a variável mensagem do tipo str abaixo. Escreva um programa em Python que:

a) Imprima o primeiro caractere da string. 
b) Imprima o último caractere.
c) Imprima o último caractere de maneira diferente do item b.
d) Imprima o terceiro caractere da string.
e) Imprima os três primeiros caracteres da string.
f) Imprima os dois últimos caracteres da string.
g) Imprima o tamanho da string.


Dica: Lembre-se de que em Python, os índices das strings começam em 0.
"""

mensagem = "Instituto Infnet"

# Item a - Imprima o primeiro caractere da string. 
# Escreva seu código abaixo
print (mensagem[0])

# Item b - Imprima o último caractere.
# Escreva seu código abaixo
print (mensagem[-1])

# Item c - Imprima o último caractere de maneira diferente do item b.
# Escreva seu código abaixo
print (mensagem[len(mensagem) -1])

# Item d - Imprima o terceiro caractere da string.
# Escreva seu código abaixo
print (mensagem[2])

# Item e - Imprima os três primeiros caracteres da string.
# Escreva seu código abaixo
print (mensagem[0:3])

# Item f - Imprima os dois últimos caracteres da string.
# Escreva seu código abaixo
print (mensagem[-2:])

# Item g - Imprima o tamanho da string.
# Escreva seu código abaixo
print (len(mensagem))