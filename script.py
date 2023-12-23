import random as ran
import music as mu
from os import system


def difficulty_setting():

    # Checks if setting is a valid number for the generator
    try:
        player_setting = int(input("Input highest guessable number, input must be between 1 and 1000: "))

        # Checks if setting is in the range of the generator
        if player_setting <= 1:
            print("Inputted value is too small, pick a larger number")
            mu.invalid_aud()
            game()
            
        if player_setting > 1000:
            print("Inputted value is too large, pick a smaller number")
            mu.invalid_aud()
            game()
            

    except ValueError :
        print("Pick a number")
        mu.invalid_aud()
        game()       

    # Sets the setting to put into game()
    print("Highest guessable number is", player_setting)
    return player_setting 

def play_again():

    # Range of possible inputs, *.lower() method ensures that input is valid reguardless of casing
    str_valid_input_accept = ["yes", "y"]
    str_valid_input_deny = ["no", "n"]
    
    player_input = input("Play again? : ")

    # Checks players options
    try:
        if str(player_input).lower() in str_valid_input_deny:
            print("The game has ended.")
            mu.endgame_aud()
            return 0 
            

        elif str(player_input).lower() in str_valid_input_accept:
            return game()
        else: 
            print("Invalid value, Try again")
            mu.invalid_aud()
            play_again() 
        
       
    except ValueError:
        print("Invalid value, Try again")
        mu.invalid_aud()
        play_again()
     

def game():
    
    print(
        """
#####################===GUESS==THE==NUMBER===###################
        """
    )

    # Set Difficulty
    highest_guessable_num = difficulty_setting()

    # Check if the selected difficulty is valid
    try:
        ran_number = ran.randint(1, highest_guessable_num)
    except ValueError:
        mu.invalid_aud()
        return game()

    # On game start set game_running to true, play startgame.wav, and set the number of attempts
    game_running = True
    mu.startgame_aud()
    attempt = 3

    # Two loops; outer loop starts the game, inner loop goes throught the attempts
    while game_running:
        while attempt > 0:
            system('cls')
            if attempt != 3:
                print("----------------------------------------------------------------")
                print("Try again")

            elif attempt == 1: print("Last attempt")
            else: print(attempt, "attempts left")

            # Checks if player's guess is valid (a valid number) 
            try:
                player_guess = int(input("Guess the number : "))
            except ValueError:
                print("Invalid input; pick a number")
                mu.invalid_aud()
                continue
            
            # Checks if the player's guess is out of range
            if player_guess > highest_guessable_num:
                print("Your guess is higher than the highest guessable number, try again")
                mu.invalid_aud()
                continue

            # Checks if player's guess is correct
            if player_guess == ran_number:
                print("""
****************************************************************
                """)
                
                print("You guessed it right!")
                
                print("""
****************************************************************
                """)
                mu.win_aud()
                break
                
            else:
                mu.incorrect_aud()
                if player_guess > ran_number:
                    print("Your guess is too high!")
                elif player_guess < ran_number:
                    print("Your guess is too low!")
                input('Press enter to continue: ')
                attempt -= 1
        break
    
    # When attempts drains, run through this code, gives player another chance to play again
    if attempt == 0:
        system('cls')
        print("The answer is", ran_number)
        print("Gameover")
        mu.lose_aud()
        return play_again()
    else:
        return play_again()

########################################################################

