import random

hand_signs = ['rock', 'paper', 'scissors']

rand_choice = random.choice(hand_signs)
rounds = int(input('How many rounds you want: '))
game = 0
user_score = 0
cpu_score = 0


def checkWinner(user_score, cpu_score, rounds, game):
    score = "The score was {}:{}".format(user_score, cpu_score)
    if game == rounds:
        if user_score > (rounds / 2):
            print("You win, nice")
            print(score)
        else:
            print("You lost, whack")
            print(score)


print(user_score, cpu_score)
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
        # CPU wins
        # rock
        if user_choice.lower() == 'scissors' and rand_choice == 'rock':
            game += 1
            cpu_score += 1
            print(rand_choice, user_choice)
            print('Rock destroys scissors, too bad')
            checkWinner(user_score, cpu_score, rounds, game)
            continue
        # paper
        if user_choice.lower() == 'rock' and rand_choice == 'paper':
            game += 1
            cpu_score += 1
            print(rand_choice, user_choice)
            print('Paper covers rock, too bad')
            checkWinner(user_score, cpu_score, rounds, game)
            continue
        # scissors
        if user_choice.lower() == 'paper' and rand_choice == 'scissors':
            game += 1
            cpu_score += 1
            print(rand_choice, user_choice)
            print('Scissors cut paper, too bad')
            checkWinner(user_score, cpu_score, rounds, game)
            continue
        # USER wins
        # rock
        if user_choice.lower() == 'rock' and rand_choice == 'scissors':
            game += 1
            user_score += 1
            print(rand_choice, user_choice)
            print('Rock destroys scissors, nice')
            checkWinner(user_score, cpu_score, rounds, game)
            continue
        # paper
        if user_choice.lower() == 'paper' and rand_choice == 'rock':
            game += 1
            user_score += 1
            print(rand_choice, user_choice)
            print('Paper covers rock, nice')
            checkWinner(user_score, cpu_score, rounds, game)
            continue
        # scissors
        if user_choice.lower() == 'scissors' and rand_choice == 'paper':
            game += 1
            user_score += 1
            print(rand_choice, user_choice)
            print('Scissors cut paper, nice')
            checkWinner(user_score, cpu_score, rounds, game)
            continue
