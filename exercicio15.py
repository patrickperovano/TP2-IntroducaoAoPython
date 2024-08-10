#Exercício 15

"""
Alice e Bob são dois amigos e querem se comunicar através de mensagens escritas de maneira que outras pessoas que eventualmente peguem suas mensagens não consigam decifrar. Assim, eles criam uma criptografia com o seguinte algoritmo:

1) Dividem a mensagem ao meio
2) A primeira metade da mensagem vai ocupar as posições pares do texto. Já a segunda metade vai ocupar as posições ímpares. Considerando que a primeira posição é a 0.

Por exemplo, a mensagem "Olá Alice." seria transformada em:

        posicao |0 1 2 3 4 5 6 7 8 9 
           pares|O # l # á #   # A #    
        ímpares |# l # i # c # e # .
         ____________________________
         
mensagem_encriptada = Olliác eA.
(Veja no moddle uma figura com esse exemplo)
Escreva um código parar desencriptar a mensagem definida na variável mensagem_encriptada e imprimir a mensagem original. Seu código deve conter comentários.
"""

mensagem_encriptada = "Otleár cAelpitcaed!a .R eMsaosl vaig omruad acro mn oessssae  cnroivpot omgértaofdioa ,n iancgrueédmi tvoa iq uceo nnsoesgsuai rú llteirm an omsesnassa gmeemn sfaogie nisn."

# Escreva seu código abaixo