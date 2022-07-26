import random

while True:
    
    choices= ["rock","paper","scissors"]
        
    computer = random.choice(choices)
    player = None
        
    while player not in choices:
        player = input("rock, paper, scissors?: ").lower()
        
    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie..")
    elif player=="rock":
        if computer =="scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win..")
        if computer =="paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose..")
    elif player=="scissors":
        if computer =="rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose..")
        if computer =="paper":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win..")
    elif player=="paper":
        if computer =="rock":
            print("computer: ",computer)
            print("player: ",player)
            print("You Win..")
        if computer =="scissors":
            print("computer: ",computer)
            print("player: ",player)
            print("You lose..")
    play =input("Play again? (y/n): ").lower()
    if play !="y":
        break
print("Bye..")