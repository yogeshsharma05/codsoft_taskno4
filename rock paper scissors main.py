
import random
print("1=Rock")
print("2=Paper")
print("3=Scissors")
options = [1,2,3]

user_choice = input("Choose 1, 2, or 3: ")

computer_choice = random.choice(options)

print("You chose: ", user_choice)

print("Computer chose: ", computer_choice)

if user_choice == computer_choice:

    print("It's a tie!")

elif user_choice == "1" and computer_choice == "3":

    print("You win!")

elif user_choice == "2" and computer_choice == "1":

    print("You win!")

elif user_choice == "3" and computer_choice == "2":

    print("You win!")

else:

    print("Computer wins!")