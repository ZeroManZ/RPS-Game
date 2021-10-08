import random
def get_choide(choice):
    if choice == "R" :
        return "Rock"
    elif choice == "P" :
        return "Paper"
    elif choice== "S" :
        return "Scissors"
    else :
        return "Not a Valid Choice"

def main() :

    name=input(f'Please enter yourname : ')
    name = name.upper()
    print('Welcome',name,'to Rock , Paper & Scissors Game . Have Fun !')
    print("[R]=Rock , [P]=Paper , [S]=Scissors $ [Q]=Quit Game")

    choices = ["R","P","C"]
    counter = 1
    game_on = True

    while game_on:
        # co f dung de ep kiêu string de edit no nhu kieu du lieu
        user_choice = input(f"Game #{counter}.Please enter your choice:")
        user_choice = user_choice.upper()
        if user_choice == "Q" :
            print('Thanks for joining ! Have a nice day !')
            game_on = False
        else :
            random_index = random.randint(0,2)
            computer_choice = choices[random_index]

            print(f"You selected : {get_choide(user_choice)}")
            print(f"Computer choice : {get_choide(computer_choice)}")

            #winning Rules
            if user_choice =="R" and computer_choice == "S" :
                print('Congratuation , you Win . Rock beats Scissors !')
            elif user_choice =="P" and computer_choice == "R" :
                print('Congratuation , You Win . Paper covers Rock ! ')
            elif user_choice =="S" and computer_choice == "P" :
                print('Congratuation , you Win . Scissors cuts Paper !')

            #losing Rules
            elif user_choice =="R" and computer_choice == "P" :
                print('So sorry , Computer Wins . Paper covers Rock ! ')
            elif user_choice =="S" and computer_choice == "R" :
                print('So sorry , Computer Wins . Rock beats Scissors !')
            elif user_choice =="P" and computer_choice == "S" :
                print('So sorry , Computer Wins . Scissors cuts Paper !')

            #Draw Rule
            elif user_choice==computer_choice:
                print(f"Wow ! That's Draw . Both you and computer selected : {get_choide(user_choice)}")
            else :
                print('Invalid option : Please Only Choose [R] - [P] - [S] or [Q]')
        counter += 1
        print("-"*50)

if __name__ == "__main__" :
    main()