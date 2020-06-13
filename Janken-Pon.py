import random

hand_signs = ['rock', 'paper', 'scissors']

rand_choice = random.choice(hand_signs)
rounds = int(input('How many rounds you want: '))
game = 0

while game < rounds:
  print(rand_choice)
  user_choice = input("Rock, Paper or Scissors: ")

  if user_choice.lower() == rand_choice:
    game += 1
    rounds += 1
    print(rand_choice, user_choice)
    print("Draw")
    continue

  elif user_choice.lower() != rand_choice:
    #CPU wins
    #rock 
    if user_choice.lower() == 'scissors' and rand_choice == 'rock':
      game += 1
      print(rand_choice, user_choice)
      print('Rock destroys scissors, too bad')
      continue
    # paper
    if user_choice.lower() == 'rock' and rand_choice == 'paper':
      game += 1
      print(rand_choice, user_choice)
      print('Paper covers rock, too bad')
      continue
    #scissors 
    if user_choice.lower() == 'paper' and rand_choice == 'scissors':
      game += 1
      print(rand_choice, user_choice)
      print('Scissors cut paper, too bad')
      continue
    #USER wins
    #rock    
    if user_choice.lower() == 'rock' and rand_choice == 'scissor':
      game += 1
      print(rand_choice, user_choice)
      print('Rock destroys scissors, nice')
      continue
    # paper
    if user_choice.lower() == 'paper' and rand_choice == 'rock':
      game += 1
      print(rand_choice, user_choice)
      print('Paper covers rock, nice')
      continue
    #scissors
    if user_choice.lower() == 'scissor' and rand_choice == 'paper':
      game += 1
      print(rand_choice, user_choice)
      print('Scissors cut paper, nice')
      continue