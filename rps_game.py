import random

def rock_paper_scissors():
    choices = ["kámen", "nůžky", "papír"]
    computer_choice = random.choice(choices)
    player_choice = input("Zvol si kámen, nůžky nebo papír: ").lower()
    if player_choice == computer_choice:
        print("Remíza!")
    elif (player_choice == "kámen" and computer_choice == "nůžky") or (player_choice == "nůžky" and computer_choice == "papír") or (player_choice == "papír" and computer_choice == "kámen"):
        print("Vyhrál jsi!")
    else:
        print("Prohrál jsi.")


while True:
    rock_paper_scissors()