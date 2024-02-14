print("**** Seja bem vindo(a)! ****\n")
print('Estamos iniciando o nosso primeiro projeto em grupo, fique a vontade para escolher a sua opção')

perguntas = {'Pergunta 1': {
    'pergunta': 'Qual a linguagem de programação você escolheria para fazer o Projeto IntegradorI ? ',
    'respostas': {'a': 'Linguagem Python? ', 'b': 'Linguagem Java? '},
    'resposta': ' ',
    },
    'Pergunta 2': {
    'pergunta': 'Em que parte do Projeto IntegradorI você mais se identifica? ',
    'respostas': {'a': 'Tecnologias Back-end? ', 'b': 'Tecnologia Front-end? '},
    'resposta': ' ',
    },
    'Pergunta 3': {
    'pergunta': 'No Projeto IntegradorI você gostaria de ficar em qual área para executar a sua tarefa? ',
    'respostas': {'a': 'Back-end', 'b': 'Front-end', 'c': 'Pesquisar', 'd': 'Monografia'},
     'resposta': '',
    },
    'Pergunta 4': {
    'pergunta': 'Está com duvida em qual deve escolher? ',
    'respostas': {'a': 'Já escolhi! ', 'b': 'Não sei em qual me encaixar. '},
    'resposta': ' ',
    },
}

print()

respostas: str = ''
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    for rk, rv in pv["respostas"].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['respostas']:
        print('Parabéns pela escolha! ou sua habilidade!')
        respostas += 1
    else:
        print('Está com duvida.')

## qtd_perguntas = 0
## qtd_perguntas = len(perguntas)

## porcentagem = print(int)
## porcentagem_acerto = respostas / qtd_perguntas * 100
## print(f'Você {respostas} respostas.')
## print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')
