import random

def get_user_choice():
    user_input = input("Wähle Schere, Stein oder Papier: ").lower()
    if user_input in ["schere", "stein", "papier"]:
        return user_input
    else:
        print("Ungültige Eingabe. Bitte wähle erneut.")
        return get_user_choice()

def get_computer_choice():
    return random.choice(["schere", "stein", "papier"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Unentschieden!"
    elif (user_choice == "schere" and computer_choice == "papier") or \
         (user_choice == "stein" and computer_choice == "schere") or \
         (user_choice == "papier" and computer_choice == "stein"):
        return "Du gewinnst!"
    else:
        return "Computer gewinnt!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"Du hast {user_choice} gewählt. Der Computer hat {computer_choice} gewählt.")
    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()