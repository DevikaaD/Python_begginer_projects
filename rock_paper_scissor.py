import random

user_score = 0
comp_score = 0

options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Enter Rock/Paper/Scissor or Q for quiting: ").lower()
    if user_input =='q':
        break
    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    comp_pick = options[random_number]
    print("Computer picked", comp_pick)

    if user_input == "rock" and comp_pick == "scissor":
        print("You won!")
        user_score +=1
    elif user_input == "paper" and comp_pick == "rock":
        print("You won!")
        user_score +=1
    elif user_input == "scissor" and comp_pick == "paper":
        print("You won!")
        user_score +=1
    elif user_input == comp_pick:
        print("Its tie no one wins")
    else:
        print("You lost!")
        comp_score +=1

print("Your score is",user_score)
print("Computer score is",comp_score)
print("Goodbye")