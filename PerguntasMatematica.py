print()
print("**** Seja bem vindo(a)! ****")
print('Estamos iniciando o nosso primeiro projeto - perguntas Matemáticas!\n')

perguntas = {'Pergunta 1': {
    'pergunta': 'Quanto é 450 + 56? ',
    'respostas': {'a': '454', 'b': '506', 'c': '360'},
    'resposta_certa': 'b',
    },
    'Pergunta 2': {
    'pergunta': 'Teste a sua memória, quanto é 2.457 - 635? ',
    'respostas': {'a': '1.325', 'b': '1.000', 'c': '1.822'},
    'resposta_certa': 'c',
    },
    'Pergunta 3': {
    'pergunta': 'Quanto é 45 * 8? ',
    'respostas': {'a': '280', 'b': '0', 'c': '365'},
    'resposta_certa': 'a',
    },
    'Pergunta 4': {
    'pergunta': 'Quanto é 8.928 / 4 ? ',
    'respostas': {'a': 'Não sei.', 'b': '568', 'c': '2.232'},
    'resposta_certa': 'c',
    }
}

print()

respostas_certas = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv["respostas"].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('Parabéns!')
        respostas_certas += 1
    else:
        print('Você errou.')

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100
print(f'Você {respostas_certas} respostas.')
print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')