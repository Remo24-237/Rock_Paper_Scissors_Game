import random

def RPS():
    # create a list of play options
    t = ["Rock", "Paper", "Scissors"]
    # assign a random play to the computer
    computer = t[random.randint(0, 2)]
    # set player to false
    player = False

    while player == False:
        # set player to True
        player = input("Rock, Paper, Scissors ?")
        if player == computer:
            print("Tie!!!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!!!", player, "smashes", computer)
        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!!!", player, "covers", computer)
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose!", computer, "smashes", player)
            else:
                print("You win!!!", player, "cut", computer)
        elif player == "Quit" or "quit":
            print("Thank you for playing.")
            break
        else:
            print("Check your spelling entry and try again ")

        player = False
        computer = t[random.randint(0, 2)]

if __name__ == '__main__':
    RPS()
