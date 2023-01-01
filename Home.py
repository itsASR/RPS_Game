import random



while True :
    print()
    print("Enter a choice between - Rock,Paper,Scissors or Q for Quit ")
    user = input().lower()
    options = ["rock","paper","scissors"]
    comp = random.choice(options)
                
    if user == comp:
        print("Game Tie because you choose",user,"and Computer also choose",comp)
    elif user == "rock":
        if comp == "paper":
            print("you loose paper cover the rock")
        else:
            print("you win scissors dont cut rock")
    elif user == "paper":
        if comp == "rock":
            print("you win paper cover rock")
        else:
            print("you loose scissor cuts paper")
    elif user == "scissors":
        if comp == "rock":
            print("you loose rock damage scissors")
        else:
            print("you win paper cut by you")
    elif user == "q":
        print("Thank you for playing")
        print()
        print()
        break

