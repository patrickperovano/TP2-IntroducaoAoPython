# Exercício 16
"""
Escreva um código para resolver equações do segundo grau. 
O código deve receber 3 números a, b, c e a equação resolver a equação:
ax**2 + bx + c = 0.
Após receber os valores o seu código deve tentar utilizar a fórmula de Bhaskara. O código não precisa checar caso a equação não tenha solução.
Após a resolução o código deve imprimir as duas soluções da equação. Um início de código é disponibilizado.
"""
print("Programa solucionar de equações ax**2 + bx + c = 0")
# Modifique as linhas de 11 a 13 para receber os valores de entrada pelo usuário
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Não precisa mexer no print abaixo
print("Resolvendo a equacao: ")
equacao = str(a) + "x**2 " + (" +" if b >= 0  else "") + str(b) + ("x +" if c >= 0  else "") + str(c) + " = 0" 
print(equacao)

# Resolva a equacao
delta = b**2 - 4*a*c

# Calcule a primeira solução
x0 = (-b + delta**0.5) / (2*a)

# Calcule a segunda solução
x1 = (-b - delta**0.5) / (2*a)

# Escreva o valor das soluções com uma mensagem para que seja compreendida pelo usuário (não dê print simplesmente os valores)
print (f"As solucoes das equacoes sao: x0 = {x0} e x1 = {x1}")