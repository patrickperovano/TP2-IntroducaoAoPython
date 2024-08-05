# Exercício 16
"""
Escreva um código para resolver equações do segundo grau. 
O código deve receber 3 números a, b, c e a equação resolver a equação:
ax**2 + bx + c = 0.
Após receber os valores o seu código deve tentar utilizar a fórmula de Bhaskara. O código não precisa checar caso a equação não tenha solução.
Após a resolução o código deve imprimir as duas soluções da equação. Um início de código é disponibilizado.
"""
# Modifique as linhas de 11 a 13 para receber os valores de entrada pelo usuário
a = 1.0
b = -5.0 
c = 6.0


print("Resolvendo a equacao: ")
equacao = str(a) + "x**2 " + (" +" if b >= 0  else "") + str(b) + ("x +" if c >= 0  else "") + str(c) + " = 0" 
print(equacao)

# Resolva a equacao
delta = None # Troque essa linha para calcular o delta

# Calcule a primeira solução
x0 = None

# Calcule a segunda solução
x1 = None

# Escreva o valor das soluções com uma mensagem para que seja compreendida pelo usuário (não dê print simplemente os valores)