# Exercício 4
"""
Análise o seguinte o programa abaixo. E faça o que é pedido nos itens abaixo:

a) Substitua os comentários em cima de cada linha por uma explicação do que aquela linha faz.
b) Note que a mensagem tem três problemas. O primeiro é que existe um hífen em 'A - Ginasta'. O segundo é que a palavra ginasta aparece com letra maiuscula. E por último, existem dois espaços entre em '... de Andrade  ganhou'. Modifique os valores da variável nome e profissão para corrigir a mensagem.
"""

# Substitua esse comentário
nome_e_profissao = "Rebeca Rodrigues de Andrade - Ginasta"

# Substitua esse comentário
posicao_hifen = nome_e_profissao.find("-")

# Substitua esse comentário
nome = nome_e_profissao[:posicao_hifen]

# Substitua esse comentário
profissao = nome_e_profissao[posicao_hifen:]

# Adicione código modificar os valores das variáveis nome e profissao de forma a corrigir a mensagem.


# Substitua esse comentário
print("A", profissao, nome, "ganhou medalha de ouro no solo e prata no individual geral nas olimpíadas da Paris 2024.")