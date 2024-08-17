# Exercício 1
"""
Considere as seguintes atribuições nas variáveis abaixo e responda as perguntas que vem em seguida. (Caso sinta dúvida você pode usar a função type para conferir os tipos)
"""

a0 = 10
a1 = "10"
a2 = 10.0

print (type(a0))
print (type(a1))
print (type(a2))

b0 = a0 + a2
b1 = a2 + a2
b2 = 5 * a0
b3 = a0 // 2
b4 = a0 / 2

isso_eh_um_int = 10.0
isso_eh_um_float = "10"
isso_eh_uma_string = 10

print (type(b0))
print (type(b1))
print (type(b2))
print (type(b3))
print (type(b4))

print (type(isso_eh_um_int))
print (type(isso_eh_um_float))
print (type(isso_eh_uma_string))





###############################################
#                Perguntas
###############################################
"""
Qual o tipo das variáveis a0, a1 e a2?
"""
# Resposta: a0 = int, a1 = string, a2 = float
"""
Qual o tipo das váriaveis b0, b1, b2, b3 e b4? 
"""
# Resposta: b0 = float, b1 = float, b2 = int, b3 = int, b4 = float
"""
Qual o tipo das variaveis isso_eh_um_int, isso_eh_um_float e isso_eh_uma_string?
(Note que o nome da variável não influencia no seu tipo)
"""
# Resposta: isso_eh_um_int = float, isso_eh_um_float = str, isso_eh_uma_string = int 
"""
Caso existisse um código entrada_do_usuario = input(), qual seria o tipo da variável entrada_do_usuario? O que deveria ser feito caso você queira utilizar a entrada do usuário como um número inteiro?
"""
# Resposta: seria do tipo string. Entretanto, para converter a entrada de str para int, basta utilizar o codigo/expressao a seguir:
#entrada_do_usuario = input("Digite um número: ")
#numero_int = int(entrada_do_usuario)