import random


def choice():
    options = ['R', 'P', 'S']
    player_choice = input("Pick between these 3 options (R, P, S): ").upper()
    computer_choice = random.choice(options)
    print(f"Player ({player_choice}) : CPU ({computer_choice})")

    while True:
        if player_choice not in options:
            print('Invalid input, Try again')
        elif player_choice == computer_choice:
            print(f"Both selected {player_choice}. It's a tie")
            choice()
        elif player_choice == 'R':
            if computer_choice == 'S':
                print("Rock breaks Scissors. You win")
            else:
                print("Paper covers Rock. CPU win")
        elif player_choice == 'P':
            if computer_choice == 'R':
                print("Paper covers Rock. You win")
            else:
                print("Scissors cut Paper. CPU win")
        elif player_choice == 'S':
            if computer_choice == 'P':
                print("Scissors cut Paper. You win")
            else:
                print("Rock breaks Scissors. CPU win")
        break
choice()