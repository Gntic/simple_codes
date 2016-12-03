print ('Jogo da adivinhaçao 2.0')
print ('***********************')
print ('Estou pensando em um numero entre 1 - 10, tente acertar')
num = 5


def tentar():
    tentativa = int(input('Qual numero é: '))
    if tentativa > num:
        print ('Muito alto')
        tentar()
    elif tentativa < num:
        print ('Muito baixo')
        tentar()
    elif tentativa == num:
        print ('Parabens')
        return 1
    else:
        print ('Algo deu errado')

tentar()
