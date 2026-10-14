correct_door_sequence = ""

door1 = input("Door 1, left or right? ")
door1.lower()
if door1 == "right":
    print("Game over")
elif door1 == "left":
    door2 = input("Door 2, left or right? ")
    door2.lower()
    if door2 == "left":
        print("Game over")
    elif door2 == "right":
        door3 = input("Door 3, left or right? ")
        door3.lower()
        if door3 == "left":
                print("Game over")
        elif door3 == "right":
            door4 = input("Door 4, left or right? ")
            door4.lower()
            if door4 == "right":
                    print("Game over")
            elif door4 == "left":
                print("You found the treasure")
else:
     print("Error, game over")