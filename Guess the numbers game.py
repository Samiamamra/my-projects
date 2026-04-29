import random 
import os 

# get the difficulty from the user
def get_difficulty():
    while True:
        difficulty = input("Choose a difficulty level (1, 2, 3, 4): ")
        if difficulty in ["1", "2", "3", "4"]:
            return difficulty
        else:
            print("Invalid difficulty level. Please try again.")

# Clear screen function
def clear_screen(): 
    os.system('cls' if os.name == 'nt' else 'clear') 

# creat a random number and number range acording to the difficlty 
def generate_random_number(Difficulty): 
    difficulty_level = {
        "1" : 20,
        "2" : 100,
        "3" : 1000,
        "4" : 10000
    }
    number_range = difficulty_level.get(Difficulty)
    # creat a random number
    random_number = random.randint(1,number_range)
    # return the random number and the number range
    return random_number, number_range

# get the attampts number acording to the difficulty
def get_attempts(Difficulty):
    # creat the attampts number acording to the difficulty
    attempts = {
        "1" : 5,
        "2" : 7,
        "3" : 9,
        "4" : 7
    }
    # return the attampts number
    return attempts.get(Difficulty)

# end game menu
def end_menu():
    # clear screen
    clear_screen()
    # end game mesage
    print("tank you for plaing!\nwhat do you need nouw\n1.return to main menu\n2.exit")
    choose = input("enter your chouse (1 or2):")
    # cheak the user choise
    if choose == "1":
        clear_screen()
        main()
    elif choose == "2":
        exit()
    else:
        clear_screen()
        print("invalid input\nplease try again")
        input("press enter to continue")
        end_menu()

# main function
def main():
    # welcome
    print("welcome to my simpol guess the number game!")
    input("press enter to continue")
    # clear screen
    clear_screen()
    # the user choose the difficulty
    difficulty = get_difficulty()
    
    # creat the random number and the number range and the attempts number
    rnd_num, number_range = generate_random_number(difficulty)
    attempts_number = get_attempts(difficulty)

    # cheak win or lose or retry 
    while True :
        # clear screen
        clear_screen()
        # cheak lose
        if attempts_number == 0:
            # clear screen
            clear_screen()
            print("The number of attempts has ended!\nGame over!")
            input("press enter to continue")
            end_menu()
        # the user enter his guess
        try:
            guess = int(input(f"you have {attempts_number} attempts\nenter your guess, a number betwin 1 and {number_range} :"))
        except ValueError:
            print("invalid input\nplease try again")
            continue
        # cheak win 
        if guess == rnd_num:
            # clear screen
            clear_screen()
            print("you wine!")
            input("press enter to continue")
            end_menu()
        # cheak retry
        else:
            # clear screen
            clear_screen()
            attempts_number -=1
            print("the number you enter is smaller than the secret number")if guess < rnd_num else print("the number you enter is bigger than the secret number")
            input("press enter to continue")
# start the game
if __name__ == "__main__":
    main()
