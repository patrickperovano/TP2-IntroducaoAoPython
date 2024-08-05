# Exercício 9

"""
Abaixo são apresentadas algumas frases da forma
  Se [sentenca0] então [sentenca1] 

Para cada uma dessas frases transforme elas em variáveis booleanas no python e mostra um exemplo em que a [sentenca1] é verdadeira e outra que ela é falsa. A primeira frase está resolvida como exemplo.

"""

# Exemplo
print("Se é fim de semana e meus amigos estão disponíveis então eu vou a praia")

# Verdadeira
e_fim_de_semana = True
amigos_disponiveis = True
vou_a_praia = e_fim_de_semana and amigos_disponiveis
print("vou_a_praia = ", vou_a_praia)

# Falsa
e_fim_de_semana = True
amigos_disponiveis = False
vou_a_praia = e_fim_de_semana and amigos_disponiveis
print("vou_a_praia = ", vou_a_praia)

# Item a
print("\nSe eu estudar e fazer os exercícios então eu passo na prova")


# Item b
print("\nSe eu tenho um carro ou tenho uma bicicleta então eu posso viajar")



# Item c
print("\nSe estou cansado ou é tarde então eu vou dormir")


# Item d
print("\nSe eu tenho dinheiro e tempo então eu vou viajar")



