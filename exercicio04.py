# Exercício 4
"""
Analise o seguinte programa abaixo. E faça o que é pedido nos itens:

a) Substitua os comentários em cima de cada linha por uma explicação do que aquela linha faz.
b) Note que a mensagem tem três problemas. O primeiro é que existe um hífen em 'A - Ginasta'. O segundo é que a palavra ginasta aparece com letra maiuscula. E por último, existem dois espaços entre em '... de Andrade  ganhou'. Modifique os valores da variável nome e profissão para corrigir a mensagem.
"""

# Ele atribuiu a variavel nome_e_profissao ao valor Rebeca Rodrigues de Andrade - Ginasta em uma unica variavel.
nome_e_profissao = "Rebeca Rodrigues de Andrade - Ginasta"

# Ele localiza a posicao do hifen na variavel nome_e_profissao
posicao_hifen = nome_e_profissao.find("-")

# Ele pega apenas o valor apresentado antes do hifen, de acordo com a localizacao da etapa anterior
nome = nome_e_profissao[:posicao_hifen]

# Ele faz o inverso do caso acima, onde apresenta o valor apos o hifel.
profissao = nome_e_profissao[posicao_hifen:]

# Adicione código modificar os valores das variáveis nome e profissao de forma a corrigir a mensagem.

# Substitua esse comentário
profissao_strip = profissao.strip("- ")
nome_strip = nome.strip(" ")


profissao_strip = profissao.strip("- ")
nome_strip = nome.strip(" ")

print(f'A {profissao_strip} {nome_strip}, ganhou medalha de ouro no solo e prata no individual geral nas olimpíadas de Paris 2024.')