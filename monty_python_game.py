print("------------------------------------------------------------------------------")
print("Welcome to the Monty Python Adventure!")
print("You are about to embark on a quest for the Holy Grail. Beware of dangerous encounters!")

print("------------------------------------------------------------------------------")
player_name = input("What is your name, brave adventurer?")
print("------------------------------------------------------------------------------")
print(f"Welcome, Sir {player_name} of Pythonia!")



print("A knight steps in front of you and says, 'None shall pass!'")
choice = input("Do you (1) fight the knight or (2) try to reason with him?")

if choice == "1":
    print("The knight draws his sword. It's time for battle!")
elif choice == "2":
    print("The knight scoffs at your attempt to reason and attacks anyway.")
else:
    print("You hesitate... and the knight charges!")
    
print("After a surprisingly short battle, you defeat the knight and journey to the Bridge of Death!")

while True:
    response = input("Do you want to cross the Bridge of Death? (yes/no)").lower()
    print("Remember, your quest is- to find the holy grail")
    
    if response == "yes":
        print("A troll appears and asks you three questions!")

        question1 = input("First question: What is your name?")
        if question1 == player_name:
            print("Well done!")
            question2 = input("Second question: What is your quest?").lower()
            if question2 == "to find the holy grail":
                print("Correct!")
                question3 = input("What is your favorite color?").lower()
                if question3 == "blue":
                    print("Yes! You have passed the test and may safely cross the bridge.")
                    print("Congratulations, you have completed your quest!")
                    break
                elif question3 == "yellow":
                    print("Yes! You have passed the test and may safely cross the bridge.")
                    print("Congratulations, you have completed your quest!")
                    break
                else:
                    print("NO! \nYou are hurled from the bridge into oblivion!")
                    break
            else:
                print("Wrong! \nYou are hurled from the bridge into oblivion!")
                break
        else:
            print("Wrong! \nYou are hurled from the bridge into oblivion!")
            break
            
            
    elif response == "no":
        print("You wisely turn back.")
        break
    else:
        print("Please answer 'yes' or 'no'.")
        
        
print(f"Farewell, Sir {player_name}!")

        