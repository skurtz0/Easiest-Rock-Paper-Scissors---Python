import random

user_Score = 0
computer_Score = 0

rps = ["Rock", "Paper", "Scissors"]

while True:
    user_Input =  input ("Rock/Paper/Scissors or Quit:   ")

    if user_Input == "Quit":
        break
    if user_Input not in rps:
        continue

    random_Number = random.randint(0,2)
    #Rock:0, Paper:1, Scissors:2

    computer_Pick = rps[random_Number]

    print("Computer Picked", computer_Pick )
    
    if user_Input == "Rock" and computer_Pick == "Scissors":
        print("You won")
        user_Score += 1
        continue

    elif user_Input == "Paper" and computer_Pick == "Rock":
        print("You won")
        user_Score += 1
        continue

    elif user_Input == "Scissors" and computer_Pick == "Paper":
        print("You won")
        user_Score += 1
        continue

    else:
        print("You lost")
        computer_Score += 1

print("The Scores", user_Score, "to", computer_Score)
    


