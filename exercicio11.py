# Exercício 11
"""
Dado o texto na variável mensagem, faça um programa que conta a porcentagem de vogais em relação a todos os caracteres da string (espaços e pontuações devem ser contabilizado na porcentagem). Seu programa deve ter comentários. (Cuidado com as vogais maiúsculas)"""

mensagem = "A importancia da persistencia no aprendizado de programacao nao pode ser subestimada. Assim como em qualquer outra habilidade, a pratica constante e a dedicacao sao fundamentais para alcançar a proficiencia. Inicialmente, a complexidade de certas linguagens e conceitos pode parecer desafiadora, mas com o tempo e a experiencia, o aprendizado se torna mais intuitivo e gratificante."

# Contagem de caracteres presentes na mensagem:
qtd_char = len (mensagem)

# Quantidade de vogais, tanto maiuscula quanto minuscula:
qtd_vogal_a = mensagem.count("a") + mensagem.count("A")
qtd_vogal_e = mensagem.count("e") + mensagem.count("E")
qtd_vogal_i = mensagem.count("i") + mensagem.count("I")
qtd_vogal_o = mensagem.count("o") + mensagem.count("O")
qtd_vogal_u = mensagem.count("u") + mensagem.count("U")

# Soma de todas as vogais:
qtd_vogal = qtd_vogal_a + qtd_vogal_e + qtd_vogal_i + qtd_vogal_o + qtd_vogal_u

# Calculo da porcentagem ja reduzindo as casas decimais:
porcentagem_de_vogais = round(qtd_char / qtd_vogal,2)

# Print para informar a porcentagem:
print ('A porcentagem de vogais é de: ', porcentagem_de_vogais,'%')