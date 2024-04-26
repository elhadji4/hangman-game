import json
import random

play = 0
while play < 4:
    with open('verbs.json') as verbs_file:
        data = json.load(verbs_file)
        if play % 2 == 0:
            verbs_list = data["verbs_level_one"]
        else:
            verbs_list = data["verbs_level_two"]

    random_verb = random.choice(verbs_list)

    reveal_count = min(2, len(random_verb) - 1) if len(random_verb) >= 5 else 1  # Ensure reveal_count is at most 2 if length >= 5, otherwise 1
    reveal_positions = random.sample(range(1, len(random_verb)), reveal_count)

    # Mask the verb with underscores except for the revealed characters
    masked_verb = ""
    for i in range(len(random_verb)):
        if i == 0 or i in reveal_positions:
            masked_verb += random_verb[i]
        else:
            masked_verb += "_"

    # Prompt the user to guess the verb by typing the missed character(s)
    
    max_attempts = 3
    attempts = 0
    while attempts < max_attempts:
        user_guess = input(f"Guess the verb by typing the missed character(s) for '{masked_verb}': ").lower()
        if user_guess == random_verb.lower():  # Use .lower() to make the comparison case-insensitive
            print("Congratulations! You guessed the verb correctly.")
            break
        else:
            attempts += 1
            if attempts < max_attempts:
                print("Incorrect guess. Try again.")
            else:
                print(f"Sorry, you've run out of attempts. The correct verb was '{random_verb}'.")
    
    play_again = input("Do you want to play again? Type 'yes' to play again or anything else to exit: ").lower()
    if play_again != 'yes':
        break
    play += 1
