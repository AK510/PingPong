print("Welcome to Treasure Island.")
print("Your missio is to Find the treasure")
c1=input("Where you would like to go Left Or Right---->")
if(c1=="right" or c1=="Right"):
    print("Game Over")
else:
    c2=input("Now You want to swim or wait--->")
    if(c2=="Wait" or c2=="wait"):
        print("Game Over")
    else:
        c3=input("Choose a color :: Red/Blue/Yellow--->")
        if(c3=="Red" or c3=="red"):
            print("game Over")
        elif(c3=="Blue" or c3=="Blue"):
            print("game Over")
        else:
            print("You win!")
    
