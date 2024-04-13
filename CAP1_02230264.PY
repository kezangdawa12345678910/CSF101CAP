################################
# Your Name
# Your Section
# Your Student ID Number
################################
# REFERENCES
# Links that you referred while solving
# the problem
# https://www.youtube.com/watch?v=LpZmZs2_BC4
# https://www.youtube.com/watch?v=aequTxAvQq4
################################
# SOLUTION
# Your Solution Score:49524
# Put your number here:4
################################
# Read the input.txt file
def read_input():
    text_file = open('CSF101CAP/input_4_cap1.txt', 'r')
    return text_file

# code here to read your input file
# solution

def calculate_score(read_lines):


    all_rounds = []
    for line in read_lines:
    # to remove "\n"
        if line[-1] == '\n':
            all_rounds.append(line[:-1])
        else:
            all_rounds.append(line)


# choices
    choices = {'rock': 1, 'paper': 2, 'scissors': 3}

# outcomes
    outcomes = {'win': 6, 'draw': 3, 'lost': 0}

# Initialize total score
    total_score = 0

    for rounds in all_rounds:
        if rounds[0] in ['A', 'B', 'C'] and rounds[2] in ['X', 'Y', 'Z']:
        # Determine opponent choice based on first letter
            if rounds[0] == 'A':
                 opponent = choices['rock']
            elif rounds[0] == 'B':
                opponent = choices['paper']
            else:
                opponent = choices['scissors']

        # Determine user choice based on second letter
        if rounds[2] == 'X':
            if opponent == choices['rock']:
                user_choice = choices['scissors']
            elif opponent == choices['paper']:
                user_choice = choices['rock']
            else:
                user_choice = choices['paper']
            total_score += user_choice + outcomes['lost']
        elif rounds[2] == 'Y':
            user_choice = opponent
            total_score += user_choice + outcomes['draw']
        else:
            if opponent == choices['rock']:
                user_choice = choices['paper']
            elif opponent == choices['paper']:
                user_choice = choices['scissors']
            else:
                user_choice = choices['rock']
            total_score += user_choice + outcomes['win']
    else:
        print("Invalid Entry")

    print("Total Score: ", total_score)

calculate_score(read_input())
