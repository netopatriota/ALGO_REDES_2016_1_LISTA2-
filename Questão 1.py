"""
1) Você foi contratado como desenvolvedor do Cinépolis que está com a necessidade
de avaliar a opinião de 10 (dez) espectadores com relação a qualidade dos filmes
apresentados em suas salas de cinema. Cada espectador de um cinema respondeu a
um questionário no qual constava sua opinião em relação ao filme: ótimo – 3, bom –
2, regular – 1. Faça um programa utilizando python versão 3.5 que receba a opinião
dos 10 (dez) espectadores, calcule e mostre:
a) A quantidade de pessoas que responderam ótimo;
b) A quantidade de pessoas que responderam bom;
c) A quantidade de pessoas que responderam regular.
"""

#incialização dos contadores
contador_regular = 0
contador_bom = 0
contador_otimo = 0

for i in range(10):
	opiniao = int(input('Digite sua opiniao sobre o filme: '))

	if opiniao == 1: #REGULAR
		contador_regular = contador_regular + 1
	elif opiniao == 2: #BOM
		contador_bom = contador_bom + 1
	else: #OTIMO
		contador_otimo = contador_otimo + 1

print ('Quantidade de opinioes em REGULAR = %d' % contador_regular)
print ('Quantidade de opinioes em BOM = %d' % contador_bom)
print ('Quantidade de opinioes em OTIMO = %d' % contador_otimo)



#assistir MR. Robot