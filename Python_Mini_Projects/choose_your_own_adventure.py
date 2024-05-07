name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, It has come to end and you can go to left or right. Which way would you like to go ? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across it. Type walk to walk around it and swim to swim across: ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost.")

    else:
        print("Not a valid option. You loose")

elif answer == "right":
    answer = input("You came across a bridge, it looks woobly, do you want to cross it or head back (cross/ back)? ")
    if answer == "back":
        print("You go back and loose")
    elif answer == "cross":
        answer = input ("You cross the bridge and meet a stranger. Do you want to talk to them? (yes/ no)")
        
        if answer == "yes":
            print("You talked to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignored the stranger, They got angry. You loose")
        else:
            print("Not a valid option. You loose")
    else:
        print("Not a valid option. You loose")
else:
    print("Not a valid option. You loose")

print("Thank you for trying", name)