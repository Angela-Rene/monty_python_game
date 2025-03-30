print("------------------------------------------------------------------------------")
print("Welcome to the Monty Python Adventure!")
print("You are about to embark on a quest for the Holy Grail. Beware of dangerous encounters!")

player_name = input("What is your name, brave adventurer?")
print("------------------------------------------------------------------------------")
print(f"Welcome, Sir {player_name} of Pythonia! \n This journey will be easier if you can find someone to venture on this quest with you.")


fellow_knight = input("Would you like to (1) look for a companion in the little village nearby, or (2) pass by the village?")
print("-------------------------------------------------------------------------------")
if fellow_knight == "1":
    print("You enter the town and find Sir Bevedere the Wise.")
    print("Being impressed with his wisdom and logic, you ask him to join you on your quest to find the holy grail. He agrees!")
elif fellow_knight == "2":
    print("You have decided to go alone. Good luck!")
else:
    print("Are you sure you are ready for this quest if you cannot decide between yes and no?  Get ready for even more difficult decisions.")
    


print("As you journey through the forest, a knight steps in front of you and says, 'None shall pass!'")
choice = input("Do you (1) fight the knight or (2) try to reason with him?")

if choice == "1":
    print("The knight draws his sword. It's time for battle!")
elif choice == "2":
    print("The knight scoffs at your attempt to reason and attacks anyway.")
else:
    print("You hesitate... and the knight charges!")
    
print("After a surprisingly short battle, you defeat the knight and journey on!")
print("After much more journeying, you come upon the fearsome sorceror...Tim!")

cave_choice = input("Do you (1) trust Tim and avoid the cave ahead, or (2) ignore him and approach the cave?")
if cave_choice == "1":
    print("That was a wise decision.  You continue on your journey and arrive at the Bridge of Death!")
elif cave_choice == "2":
    print("Tim dramatically warns you of the evil that resides in this cave.")
    double_check = input("Do you (1) finally listen to him and leave or (2) continue to ignore his crazy ranting?")
    if double_check == "1":
        print("Good decision. You continue on your journey and arrive at the Bridge of Death!")
    elif double_check == "2":
        print("The Killer Rabbit of Caerbannog attacks!  It's an epic battle, and you barely survive with the help of the Holy Hand Grenade of Antioch.")
        print("You wearily continue on your journey until you suddenly arrive at the Bridge of Death.")
    else:
        print("Another indecisive moment... better just continue on to the Bridge of Death.")
else:
    print("Another indecisive moment.  Better just proceed to the Bridge of Death.")
    


while True:
    response = input("Remember, your quest is- to find the holy grail. Do you want to cross the Bridge of Death? (yes/no)").lower()
    
    if response == "yes":
        print("A troll appears and asks you three questions!")

        question1 = input("First question: What is your name?")
        if question1 == player_name:
            print("Well done!")
            question2 = input("Second question: What is your quest?").lower()
            if question2 == "to find the holy grail":
                print("Correct!")
                question3 = input("What is your favorite color?").lower()
                if question3 == "blue" or question3 == "yellow":
                    print("Yes! You have passed the test and may safely cross the bridge.")
                    print("Congratulations, you have completed your quest! \n Though you never found the grail, you have memories to last a lifetime! \n(And you're still alive!)")
                    break
                # elif question3 == "yellow":
                #     print("Yes! You have passed the test and may safely cross the bridge.")
                #     print("Congratulations, you have completed your quest!")
                #     break
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

        