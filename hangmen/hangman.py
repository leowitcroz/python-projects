import random
import os
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#---------------- variaveis ------------------#
word_list = ['banana', 'carro', 'pessego', 'bola', 'pipoca', 'foto']
answer = []
word = random.choice(word_list)
word_length = len(word)
contador = False
cont = 6

#---------------- cria os espacoes vazios ------------------#
for _ in range(word_length):
    answer += '-'

#---------------- jogo em si ------------------#
while contador == False:

    #---------------- pega letra user ------------------#
    guess = input('choose a letter: ').lower()

#----------------- limpa o console -----------#
    os.system('clear') or None


#---------- veririca se a letra ja foi tentada----------#
    if guess in answer:
        print(f'voce ja escolher essa letra {guess}')

#---------------- verifica se ela existe na palavra e diminui as vidas caso nao ------------------#
    if guess not in list(word):
            print(f'essa letra {guess} nao ta na palavra')
            cont -= 1
            if cont == 0:
                contador = True
                print(f'perdeu, a palavra era {word}')
                quit()

#---------------- caso a letra exista ela e colocada no lugar do espaco vazio ------------------#
    for position in range(word_length):
        letter = word[position]
        if letter == guess:
            answer[position] = letter 
      
#---------------- se nao tiver mais espacos vazios o usuario ganhou ------------------#
    if '-' not in answer:
        contador = True
        print(f'voce venceu a palavra correta era {"".join(answer)}')
        quit()

#---------------- apenas detalhes para deixar o jogo mais bonito ------------------#

    print(stages[cont])
    print(answer)
    