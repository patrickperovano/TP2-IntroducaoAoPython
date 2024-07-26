# Exercício 9
# O código foi gerado inicialmente por causa desse enunciado:

# Você está enchendo uma piscina e tem duas mangueiras. A mangueira verde enche em 1,5 horas e a mangueira azul em 1,2 horas. Você deseja acelerar o processo usando as duas mangueiras. Quanto tempo levará usando as duas mangueiras, em minutos?

# Modifique o código para o caso de serem usadas duas mangueiras verdes iguais para encher a piscina. Imprima o valor do tempo levado usando a função print().

time_green = 1.5
time_blue = 1.2

minutes_green = 60 * time_green
minutes_blue = 60 * time_blue

rate_hose_green = 1 / minutes_green
rate_hose_blue = 1 / minutes_blue

rate_host_combined = 2*rate_hose_green + rate_hose_blue

time = 1 / rate_host_combined

print(time)

