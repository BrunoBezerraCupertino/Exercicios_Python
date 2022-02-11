perguntas = {
    'pergunta 1': {
        'pergunta': 'quanto é 2+2? ',
        'resposta': {'a':'5', 'b':'4', 'c':'8',},
        'resposta_certa': 'b'
    },
    'pergunta 2': {
        'pergunta': 'quanto é 2+5? ',
        'resposta': {'a': '5', 'b': '4', 'c': '7', },
        'resposta_certa': 'c'
    },
}
print()
respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('resposta:')
    for rk, rv in pv['resposta'].items():
        print(f'[{rk}]: {rv}')

    resposta_usoario = input('letra: ')
    if resposta_usoario == pv ['resposta_certa']:
        print('correto')
        respostas_certas +=1
    else:
        print('ERROU')
    print()


"""
Desafio FizzBuzz
se o numero for divisivel só por 3 é Fizz
se o numero for divisivel só por 5 é Buzz
se o numero for divisivel por 3 e 5 é FizzBuzz
"""


# def fb(n):
#     if n % 3 == 0 and n % 5 == 0:
#         return f'fizzbuzz, {n} é divisivel por 3 e por 5'
#     if n % 3 == 0:
#         return f'fizz, {n} é divisivel por 3'
#     if n % 5 == 0:
#         return f'buzz, {n} é divisivel por 5'
#     return n
# print(fb(44))
# print(fb(15))
# print(fb(9))
# print(fb(30))
