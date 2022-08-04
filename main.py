import random as ran

game_running = True
ran_number = ran.randint(1, 10)
attempt = 3

while game_running:
    print(attempt, "attempts left")
    try:
        player_guess = int(input("Guess the number: "))
    except ValueError:
        print("Not a number")
        continue
    
    if player_guess == ran_number:
         print("You guessed it right!")
         game_running = False
    else:
        if attempt == 0:
            print("Game over")
            game_running = False
        else:
            print("Try again")
            attempt -= 1
            