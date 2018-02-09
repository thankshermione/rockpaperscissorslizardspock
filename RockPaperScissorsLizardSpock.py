#!/bin/python3

from random import randint

player = input('Choose rock (r), paper (p), scissors (s), lizard (l) or spock (sp) to play!')

if player == 'r':
  print('O vs', end=' ')
  
elif player == 'p':
  print('/ vs', end=' ')

elif player == 's':
  print('>8 vs', end=' ')

elif player == 'l':
  print('S vs', end=' ')
  
else:
  print('^O^ vs', end=' ')


chosen = randint(1,5)

if chosen == 1:
  computer = 'r'
  print('O')
  
elif chosen == 2:
  computer = 'p'
  print('/')
  
elif chosen == 3:
  computer = 's'
  print('>8')
  
elif chosen == 4:
  computer = 'l'
  print('S')
  
else:
  computer = 'sp'
  print('^O^')
  


if player == computer:
  print('It\'s a draw!')
  
  
elif player == 'r' and computer == 'p':
  print('Paper covers rock! You lose :(')
  
elif player == 'r' and computer == 's':
  print('Rock breaks scissors! You win!')
  
elif player == 'r' and computer == 'sp':
  print('Spock vaporises rock! You lose :(')
  
elif player == 'r' and computer == 'l':
  print('Rock crushes lizard! You win!')
  

elif player == 'p' and computer == 's':
  print('Scissors cut paper! You lose :(')
  
elif player == 'p' and computer == 'r':
  print('Paper covers rock! You win!')
  
elif player == 'p' and computer == 'l':
  print('Lizard eats paper! You lose :(')
  
elif player == 'p' and computer == 'sp':
  print('Paper disproves Spock! You win!')
  
  
elif player == 's' and computer == 'r':
  print('Rock breaks scissors! You lose :(')
  
elif player == 's' and computer == 'p':
  print('Scissors cut paper! You win!')
  
elif player == 's' and computer == 'sp':
  print('Spock smashes scissors! You lose :(')
  
elif player == 's' and computer == 'l':
  print('Scissors decapitate lizard! You win!')
  
  
elif player == 'l' and computer == 'r':
  print('Rock crushes lizard! You lose :(')
  
elif player == 'l' and computer == 'p':
  print('Lizard eats paper! You win!')
  
elif player == 'l' and computer == 's':
  print('Scissors decapitate lizard! You lose :(')
  
elif player == 'l' and computer == 'sp':
  print('Lizard poisons spock! You win!')
  
  
elif player == 'sp' and computer == 'p':
  print('Paper disproves Spock! You lose :(')
  
elif player == 'sp' and computer == 'r':
  print('Spock vaporises rock! You win!')
  
elif player == 'sp' and computer == 'l':
  print('Lizard poisons spock! You lose :(')
  
elif player == 'sp' and computer == 's':
  print('Spock smashes scissors! You win!')
