# Write your code here
from random import seed
from random import randint


# DONE
def initialise_player_name():
    name = input("Enter your name: ")
    print("Hello,", name)
    print()

    return name


# DONE
def read_file_ratings():
    names_ratings = []
    file = open('rating.txt', 'r')

    for line in file:
        names_ratings.append(line.rstrip('\n'))

    file.close()

    return names_ratings


# DONE
def read_options():
    options_string = input()

    if options_string == '':
        options_list = ['rock', 'paper', 'scissors']
    else:
        options_list = options_string.split(",")

    print("Okay, let's start")

    return options_list


# DONE
def random_pick(options):
    seed()
    random_number = randint(1, len(options))

    return options[random_number - 1]


# DONE
def compare_options(player_pick, computer_pick, options_list):
    left_list = []
    right_list = []
    match_position = int(0)
    i = int(0)

    if player_pick == computer_pick:
        result = 'draw'
    else:
        # Iterate through options_list appending options to left_list between beginning and player_pick
        while i < len(options_list):
            if player_pick == options_list[i]:
                # print("i = " + str(i) + " => " + options_list[i])
                match_position = i
                i += 1
                break
            else:
                left_list.append(options_list[i])
                i += 1

        # print("left_list = ", left_list)

        # Iterate through options_list adding options to right_list between player_pick and end
        while i < len(options_list):
            right_list.append(options_list[i])
            i += 1

        # print("right_list = ", right_list)

        tail = len(options_list) - (match_position + 1)
        # print("Tail = ", tail)
        shift = int((len(options_list) - 1) / 2) - tail
        # print("Shift = ", shift)
        # print()
        # print("Now to rotate lists...")
        # print()

        # Move options to left_list or right_list
        if shift > 0:  # Pick on the right of the middle of options_list
            # print("shift > 0")
            i = int(0)

            while i < shift:
                right_list.append(left_list[0])
                left_list.remove(left_list[0])
                i += 1

        elif shift < 0:  # Pick on the left of the middle of options_list
            # print("shift < 0")
            shift = shift * -1
            left_list.extend(right_list[tail - shift:])
            del right_list[tail - shift:]

        else:
            pass

        # print(options_list)
        # print("left_list = ", left_list)
        # print("right_list = ", right_list)

        if computer_pick in left_list:
            result = 'win'
        else:
            result = 'lose'

    return result


# DONE
def update_rating(result):
    if result == 'win':
        return int(100)
    elif result == 'draw':
        return int(50)
    else:
        return int(0)


# DONE
def print_message(result, computer_pick):
    if result == 'lose':
        print("Sorry, but the computer chose " + computer_pick)
    elif result == 'draw':
        print("There is a draw (" + computer_pick + ")")
    elif result == 'win':
        print("Well done. The computer chose " + computer_pick + " and failed")
    else:
        pass


# Create file 'rating.txt' with player ratings - DONE
# file = open('rating.txt', 'w', encoding='utf-8')

# player_ratings = ['Tim 350', 'Jane 200', 'Alex 400']

# for player in player_ratings:
    # file.write(player + '\n')

# file.close()

# Initialise player name and rating
player_name = initialise_player_name()
player_rating = int(0)

# Get variables ready for split name-rating
file_names = read_file_ratings()
file_ratings = []
aux_name = ''
aux_rating = ''

file_lines = int(len(file_names))

i = int(0)

# Iterate through file_names splitting name and rating, and update player_rating when player_name exist in the file
while i < file_lines:
    aux_name, aux_rating = file_names[i].split()

    file_names[i] = aux_name
    file_ratings.append(aux_rating)

    if file_names[i] == player_name:
        player_rating = int(file_ratings[i])
        # print("Name:", file_names[i], ", rating:", file_ratings[i])
    i += 1

# Read player's game options as string and returns a list
game_options = read_options()

# Loop to capture player's option and play a round
while True:
    player_option = str(input())

    if player_option in game_options:
        computer_option = random_pick(game_options)  # DONE
        outcome = compare_options(player_option, computer_option, game_options)  # UPDATING
        # print("Outcome = " + outcome)
        player_rating += update_rating(outcome)  # DONE
        print_message(outcome, computer_option)  # DONE
    elif player_option == '!rating':
        print("Your rating:", player_rating)
    elif player_option == '!exit':
        break
    else:
        print("Invalid input")

print("Bye!")
