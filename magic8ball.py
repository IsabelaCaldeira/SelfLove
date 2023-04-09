#Esta é uma adaptação da Magic 8-Ball, um famoso brinquedo americano da década de 50.
#No jogo original, faz-se uma pergunta para a bola e ela retorna uma das oito respostas possíveis
#Aqui, em cada execução é exibida uma das oito frases motivacionais possíveis


import random


print('Welcome to the 8 Magic ball!!')


name = input("What's your name?")

if name == '':
  print('We wanna tell you that:')
else:
  print('Well done,', name, '! Today we wanna tell you that: ')

answer = ''




random_number = random.randint(1, 10)


if random_number == 1:
  answer = '"Success is going from frustration to frustration without losing the enthusiasm.".'
elif random_number == 2:
  answer = '"The greatest proof that you can do the impossible".'
elif random_number == 3:
  answer = '“May the good days become routine and the bad ones rare.”.'
elif random_number == 4:
  answer = '“Even if not every day is a good day, there is always something good in every day.”.'
elif random_number == 5:
  answer = '“Just as happiness does not last forever, neither does sadness".'
elif random_number == 6:
  answer = '“Pain is not eternal, it will pass”.'
elif random_number == 7:
  answer = '“You did not come this far by chance for everything there is a reason. Keep going”.'
elif random_number == 8:
  answer = '“Allow yourself to start and start over as many times as necessary.”.'
elif random_number == 9:
  answer = '“Your competition is with yourself.”.'
elif random_number == 10:
  answer = '"Your best is enough"'
else:
  answer = "Error"


print(answer)