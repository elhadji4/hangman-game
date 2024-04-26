import json
import random
import playsound
import time



def get_file(player_counter,win_count):
    with open('verbs.json') as verbs_file:
        data = json.load(verbs_file)
        if win_count >= 5:
            verbs_list = data["verbs_level_two"]
        else:
            verbs_list = data["verbs_level_one"]

    random_verb = random.choice(verbs_list)
    return random_verb

def verb_len_counter(random_verb, reveal_count):
    reveal_count = min(2, len(random_verb) - 1) + 1 if len(random_verb) >= 5 else 1
    reveal_positions = random.sample(range(1, len(random_verb)), reveal_count)
    masked_verb = ""
    for i in range(len(random_verb)):
        if i == 0 or i in reveal_positions:
            masked_verb += random_verb[i]
        else:
            masked_verb += "_"
    return masked_verb

def player_game(random_verb, masked_verb, points):
    max_attempts = 1
    attempts = 0
    while attempts < max_attempts:
        print(f"Points: {points}")  
        user_guess = input(f"Guess the verb by typing the complete verb with any missing character(s) for '{masked_verb}': ").lower()
        if user_guess == random_verb.lower():
            print("Congratulations! You guessed the verb correctly.")
            # for playing mp3 file
            playsound.playsound("sounds/you-win-sequence-2-183949.mp3")
            points += 1  
            return True, points  # Indicate win and return updated points
        else:
            attempts += 1
            if attempts < max_attempts:
                print("Incorrect guess. Try again.")
            else:
                points -= 1
                if points < 0:
                     print(f"Sorry (Game Over.), you've run out of attempts. The correct verb was '{random_verb}'.")
                     exit 
                return False, points  # Indicate loss and return updated points
    print("Unexpected condition encountered. Returning None.")
    return False, points  


def play_hangman_game():
    while True:
        player_counter = 0
        win_count = 0
        points = 0  # Initialize points
        play_again = 'yes'  # Define play_again variable outside the loop
        while play_again.lower() == 'yes':  # Check if play_again is 'yes'
            player_counter, win_count, points = play_round(player_counter, win_count, points)
            if win_count == 5:
                play_again = input("You've won 5 times. Moving to the next level of verbs \n Type 'y' to continue or 'x' to exit: ").lower()
                if play_again not in ['y', 'x']:
                    print("Invalid input. Please type 'y' to continue or 'x' to exit.")
                else:
                    win_count = 0  # Reset win count after prompting the user to continue
            if player_counter >= 3:
                print("Congratulations! You've won three times. Moving to the next level of verbs.")
                
                player_counter = 0  # Reset player counter
        if play_again == 'x' or points == -1:  # Check if points become -1 or user chooses to exit
            break

def play_round(player_counter, win_count, points):
    random_verb = get_file(player_counter, win_count)
    reveal_count = 1  # Initial reveal count
    while points >= 0:  # Check if points are greater than or equal to 0
        masked_verb = verb_len_counter(random_verb, reveal_count)
        result, points = player_game(random_verb, masked_verb, points)
        if result:  # If the player won
            player_counter += 1  # Increment player counter on win
            win_count += 1
            break
        else:
            reveal_count += 1  # Increment reveal count on unsuccessful guess
            if points == -1:
                break  # Break out of the loop if points become -1
    return player_counter, win_count, points

# Call the function to start the game
play_hangman_game()

