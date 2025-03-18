print("Welcome to the Monty Python Adventure!")
print("You are about to embark on a quest for the Holy Grail. Beware of dangerous encounters!")

player_name = input("What is your name, brave adventurer?")
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
    
    if response == "yes":
        print("A troll appears and asks you three questions!")
        break
    elif response == "no":
        print("You wisely turn back.")
        break
    else:
        print("Please answer 'yes' or 'no'.")
        
        
print("Congratulations, you have completed your quest!")
print(f"Farewell, Sir {player_name}!")

        