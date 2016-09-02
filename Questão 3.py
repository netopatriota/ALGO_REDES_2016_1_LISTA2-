"""Você foi contratado como desenvolvedor do UNIPÊ que está com a necessidade de
avaliar as 3 (três) notas de um aluno do curso de Redes de Computadores e mostrar
a média aritmética e a mensagem constante da tabela abaixo baseada na média
aritmética do aluno. Desenvolva esse programa utilizando python versão 3.5.
Média Aritmética Mensagem
0,0 até 4,0 (não incluso) Reprovado
4,0 até 7,0 (não incluso) Prova Final
7,0 até 10,0 Aprovado
"""

nome = input('Digite o nome do aluno(a): ')
print ('Lembre de usar . (ponto) ao invés de , (vírgula).')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3

if media >= 7.00:
    print (nome, 'Muito bem, você foi a aprovado(a) e sua média foi: %.2f' %media)
elif media >= 4.00 and media < 7.00:
    print (nome, 'Você está quase lá. Vai precisar fazer recuperação, sua média foi: %.2f' %media)
else:
    print (nome, 'Não foi dessa vez, sua média foi %.2f e você está reprovado(a)' %media)
