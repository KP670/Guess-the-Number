import random as ran

game_running = True
ran_number = ran.randint(1, 10)
print(ran_number)

while game_running:
    try:
        player_guess = int(input("Guess the number: "))
    except ValueError:
        print("Not a number")
        continue
    
    if player_guess == ran_number:
         print("You guessed it right!")
         game_running = False
    else:
        print("Try again")
        continue