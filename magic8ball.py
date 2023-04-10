#This game is an adapation of the famous Magic 8-Ball, a famous toy from the 50s 
#In the original game, you make questions to the ballfaz-se uma pergunta para a bola and it return with eight possibles answers
#Here, in each execuation it is shown a motivational phrase
#Enjoy <3


import random


print('Welcome to the 8 Magic ball!!')


name = input("What's your name?")

if name == '':
  print('We wanna tell you that:')
else:
  print('Well done,', name, '! Today we wanna tell you that: ')

answer = ''




random_number = random.randint(1, 11)


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
  answer = '“Allow yourself to start new and start over as many times as necessary.”.'
elif random_number == 9:
  answer = '“Your competition is with yourself.”.'
elif random_number == 10:
  answer = '"Your best is enough"'
elif random_number == 10:
  answer = '"Do it for yourself"'
else:
  answer = "Error"


print(answer)