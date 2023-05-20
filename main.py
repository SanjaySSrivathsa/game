print("Welcome to Treasure Island. Your mission is to find the treasure.")
x=input("Do u want to go 'left' or 'right' ?? ")
q=x.lower()
if q == "right":
    print("Fall into a hole. Game Over.")
elif q == "left":
    e=input("Do want to 'swim' or 'wait' ??")
    w=e.lower()
    if w=="swim":
        print("Attacked by trout. Game Over.")
    elif w=="wait":
        r=input("In which door u want to go inside ?? IS it 'red' , 'blue' or 'yellow'")
        t=r.lower()
        if t=="red":
            print("Burned by fire.Game Over")
        elif t=="blue":
            print("Burned by fire. Game Over")
        elif t=="yellow":
            print("You Win!")
        else:
            print("game over!!")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")

