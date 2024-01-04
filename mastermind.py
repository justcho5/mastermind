import random
from collections import Counter
COLORS = ['R','B','Y','O','G','P']

def select_code():
    code = random.choices(COLORS,k=4)
    return code


def validate_input(user_input, secret_code):
    black_pegs = 0
    white_pegs = 0
    non_match = []
    color_counter = Counter(secret_code)

    for i, color in enumerate(user_input):
        if color==secret_code[i]:
            black_pegs+=1
            color_counter[color]-=1
        else:
            non_match.append(i)

    for i in non_match:
        if (user_input[i] in color_counter) and (color_counter[user_input[i]]>0):
            white_pegs+=1 
            color_counter[user_input[i]]-=1

    return black_pegs, white_pegs

def check_formatting(user_input):
    if len(user_input) != 4:
        return False
    for char in user_input:
        if char not in COLORS:
            return False
    return True


def play_game():

    secret_code = select_code()

    for i in range(10):
        print(f'This is attempt number {i+1}, you have {10-i} guesses left.')
        user_input = input("Choose your four colors (R, B, Y, O, G, P): ")

        while not check_formatting(user_input):
            print("Unrecognized input, try again")
            user_input = input("Choose your four colors (R, B, Y, O, G, P): ")

        black_pegs, white_pegs = validate_input(user_input, secret_code)

        if black_pegs == 4:
            print("YOU WIN")
            break
            
        print(f'{black_pegs} black pegs, {white_pegs} white pegs')
    print(f"Sorry, you lose. The correct answer was {secret_code}")
play_game()


    

        

