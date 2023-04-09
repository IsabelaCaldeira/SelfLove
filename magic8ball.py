#Esta é uma adaptação da Magic 8-Ball, um famoso brinquedo americano da década de 50.
#No jogo original, faz-se uma pergunta para a bola e ela retorna uma das oito respostas possíveis
#Aqui, em cada execução é exibida uma das oito frases motivacionais possíveis


import random


print('Seja bem-vindx a Bola Mágica da Virtude!')


name = input('Qual o seu nome? ')

if name == '':
  print('Queremos te dizer que:')
else:
  print('Muito bem,', name, '! Hoje queremos te dizer que: ')

answer = ''




random_number = random.randint(1, 9)


if random_number == 1:
  answer = '"O êxito é ir de frustração a frustração sem perder a animação".'
elif random_number == 2:
  answer = '"A maior prova de que você pode fazer o impossível, é superar circunstâncias difíceis".'
elif random_number == 3:
  answer = '“Que os dias bons se tornem rotina, e os ruins se tornem raros”.'
elif random_number == 4:
  answer = '“Mesmo que nem todo dia seja bom, há algo de bom todo dia”.'
elif random_number == 5:
  answer = '“Da mesma forma que a felicidade não dura para sempre, a tristeza também não”.'
elif random_number == 6:
  answer = '“As dores não são eternas, se permita, o seu melhor é o suficiente”.'
elif random_number == 7:
  answer = '“Você não chegou até aqui por acaso, para tudo existe uma razão. Continue em frente”.'
elif random_number == 8:
  answer = '“Permita-se começar e recomeçar quantas vezes forem necessárias”.'
elif random_number == 9:
  answer = '“A sua competição é com você mesmo”.'
else:
  answer = "Error"


print(answer)