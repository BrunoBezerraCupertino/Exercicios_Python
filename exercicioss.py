"""
#1.Faça um Programa que peça dois números e imprima o maior deles.
n_1 = input('um numero: ')
n_2 = input('um numero: ')


if n_1 > n_2:
    print(f'o primeiro numero é maior {n_1}')
    
elif n_1 < n_2:
    print(f'o segundo numero é maior {n_2}')
 """

""" 
#2.Faça um Programa que peça um valor e mostre na tela se o valor é
#positivo ou negativo.
n = int(input('um numero: '))

if n > 0:
    print(f'esse numero é positivo')
else:
    print(f'esse numero é negativo')
"""

""" 
#3.Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino.
letra = input('digite f ou m: ')

if letra.isalpha():
    if letra == 'f' or letra == 'F':
        print(f'feminino')
    elif letra == 'm' or letra == 'M':
        print(f'masculino')
    else:
        print('digite apenas F ou M')
else:
    print(f'digite uma letra') 
"""

""" 
#4.Faça um Programa que verifique se uma letra digitada
#é vogal ou consoante.

letra = input('letra: ')

if letra.isalpha():
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        print(f'letra {letra} é uma vogal')
    else:
        print(f'letra {letra} é uma consoante')

else:
    print(f'digite uma letra')
"""
""" 
#5.Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#  A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#  A mensagem "Reprovado", se a média for menor do que sete;
#  A mensagem "Aprovado com Distinção", se a média for igual a dez.

nota_1 = float(input('primeira nota: '))
nota_2 = float(input('segunda nota: '))
media = (nota_1 + nota_2) / 2

if media >= 7 and media < 10:
    print(f'Media {media}')
    print('Aprovado')
elif media < 7:
    print(f'Media {media}')
    print('Reprovado')
elif media >= 10.0:
    print(f'Media {media}')
    print('Aprovado com Distinção') 
"""
""" 
#6.Faça um Programa que leia três números e mostre o maior deles.
n_1 = int(input('primeiro numero: '))
n_2 = int(input('segundo numero: '))
n_3 = int(input('terceiro numero: '))

if n_1 > n_2 and n_3:
    print(f'o numero {n_1} é o maior')
elif n_2 > n_1 and n_3:
    print(f'o numero {n_2} é o maior')
elif n_3 > n_2 and n_1:
    print(f'o numero {n_3} é o maior') 
"""
""" 
#7.Faça um Programa que leia três números e mostre o maior e o menor deles
n_1 = int(input('primeiro numero: '))
n_2 = int(input('segundo numero: '))
n_3 = int(input('terceiro numero: '))

if n_1 < n_2 and n_3:
    print(f'o numero {n_1} é o menor')
elif n_2 < n_1 and n_3:
    print(f'o numero {n_2} é o menor')
elif n_3 < n_2 and n_1:
    print(f'o numero {n_3} é o menor')
"""
""" 
#8.Faça um programa que pergunte o preço de três produtos e
#informe qual produto você deve comprar, sabendo que a decisão
#é sempre pelo mais barato.
preco_1 = float(input('primeiro produto:'))
preco_2 = float(input('segundo produto: '))
preco_3 = float(input('terceiro produto: '))

if preco_1 < preco_2 and preco_3:
    print(f'compra o primeiro que é mais barato irmão, ta só R${preco_1}')
elif preco_2 < preco_1 and preco_3:
    print(f'compra o segundo que é mais barato irmão, ta só R${preco_2}')
elif preco_3 < preco_2 and preco_1:
    print(f'compra o terceiro que é mais barato irmão, ta só R${preco_3}')
"""

""" 
#9.Faça um Programa que leia três números e mostre-os em ordem decrescente.

n_1 = int(input('primeiro numero: '))
n_2 = int(input('segundo numero: '))
n_3 = int(input('terceiro numero: '))

ordem = (n_1, n_2, n_3)
nova_ordem = sorted(ordem, reverse=True)
print(nova_ordem) 
"""
""" 
#10.Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
#ou "Valor Inválido!", conforme o caso.

turno = str(input('qual turno voce estuda? M-matutino ou V-Vespertino \
 ou N- Noturno: '))

if turno == 'm' or turno == 'M':
    print('Bom Dia!')
elif turno == 'v' or turno == 'V':
    print('Boa Tarde!')
elif turno == 'n' or turno == 'N':
    print('Boa Noite!')
elif turno.isdigit():
    print('numero não irmão, lê de novo')
else:
    print('digite apenas M, V e N')
"""
""" 
#11.As Organizações Tabajara resolveram dar um aumento de salário
#aos seus colaboradores e lhe contraram para desenvolver o programa
#que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste
#segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5%
#Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

salario_inicial = int(input('salario: '))

if salario_inicial <= 280:
    percentual = 20
elif salario_inicial > 281 and salario_inicial <= 700:
    percentual = 15
elif salario_inicial > 701 and salario_inicial <= 1500:
    percentual = 10
elif salario_inicial > 1501:
    percentual = 5

porcentagem = percentual / 100
aumento = salario_inicial * porcentagem
novo_salario = (salario_inicial + aumento)

print(f'salario inicial: R${salario_inicial}')
print(f'o percentual é: {percentual}%')
print(f'o aumento isolado foi de: R${aumento}')
print(f'o novo salario é: R${novo_salario:.2f}')
"""
""" 
# 12.Faça um programa para o cálculo de uma folha de pagamento,
# sabendo que os descontos são do Imposto de Renda, que depende
# do salário bruto (conforme tabela abaixo) e 3% para o Sindicato
# e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado
# (é a empresa que deposita). O Salário Líquido corresponde ao Salário
# Bruto menos os descontos. O programa deverá pedir ao usuário o valor
# da sua hora e a quantidade de horas trabalhadas no mês.
# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20 % Imprima na tela as
# informações, dispostas conforme o exemplo abaixo. No exemplo o valor
# da hora é 5 e a quantidade de hora é 220.
# Salário Bruto: (5 * 220)                : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00  
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00

din = float(input('quanto voce ganha por hora?: '))
horas = int(input('quantas horas voce trabalha por mes?: '))
salario_bruto = din * horas

if salario_bruto <= 900:
    ir = 0
elif salario_bruto > 901 and salario_bruto <= 1500:
    ir = 5
elif salario_bruto > 1501 and salario_bruto <= 2500:
    ir = 10
elif salario_bruto > 2501:
    ir = 20

ir_2 = ir / 100
sindi = 3 /100
inss = 10
fgts = 11
inss_2 = inss /100
fgts_2 = fgts /100
desc_ir = salario_bruto * ir_2
desc_inss = salario_bruto * inss_2
desc_fgts = salario_bruto * fgts_2
desc_total = desc_inss + desc_ir + sindi
salario_liquido = salario_bruto - desc_total

print(f'salario bruto: R${salario_bruto:.2f}')
print(f'desconto dod sindicato 3%: R${sindi:.2f}')
print(f'IR de {ir}%: R${desc_ir:.2f}')
print(f'INSS de {inss}%: R${desc_inss:.2f}')
print(f'FGTS de {fgts}%: R${desc_fgts:.2f}')
print(f'Total de descontos: R${desc_total:.2f}')
print(f'seu salario liquido é de: R${salario_liquido:.2f}')
"""
"""
#13.Faça um Programa que leia um número e exiba o dia correspondente da
#semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve
#aparecer valor inválido.

dias = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado']

#for i in range(len(dias)):
#   print (i, dias[i])


numero = int(input('diga um numero correspondente a um dia da semana (1-Domingo, 2- Segunda, etc.): '))

if numero == 1:
    print(dias[0])
elif numero == 2:
    print(dias[1])
elif numero == 3:
    print(dias[2])
elif numero == 4:
    print(dias[3])
elif numero == 5:
    print(dias[4])
elif numero == 6:
    print(dias[5])
elif numero == 7:
    print(dias[6])
elif numero > 7:
    print('só tem 7 dias cara')
"""
#14.Faça um programa que lê as duas notas parciais obtidas por um aluno
#numa disciplina ao longo de um semestre, e calcule a sua média.
#A atribuição de conceitos obedece à tabela abaixo:
#Média de Aproveitamento  Conceito
#Entre 9.0 e 10.0        A
#Entre 7.5 e 9.0         B
#Entre 6.0 e 7.5         C
#Entre 4.0 e 6.0         D
#Entre 4.0 e zero        E
#O algoritmo deve mostrar na tela as notas, a média, o conceito
#correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
#ou “REPROVADO” se o conceito for D ou E.


nota_1 = float(input('primeira nota: '))
nota_2 = float(input('segunda nota: '))

media = (nota_1 + nota_2) / 2

if media > 10:
    nota = 'S'
elif media >= 9 and media <= 10:
    nota = 'A'
elif media >= 7.5 and media < 9.0:
    nota = 'B'
elif media >= 6 and media < 7.5:
    nota = 'C'
elif media >= 4 and media < 6:
    nota = 'D'
elif media >= 0 and media < 4:
    nota = 'E'

if nota == 'S':
    status = 'APROVADASSO'
elif nota == 'A' or nota == 'B' or nota == 'C':
    status = 'APROVADO'
elif nota == 'D' or nota == 'E':
    status = 'REPROVADO'

print(f'sua primeira nota foi: {nota_1}')
print(f'sua segunda nota foi: {nota_2}')
print(f'sua media foi: {media}')
print(f'status: {status}')


#15.