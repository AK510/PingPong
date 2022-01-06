import random
computer=["Rock","Paper","Scissor"]
print("Here we Go")
print("1 For Rock")
print("2 For Paper")
print("3 For Scissor")
u=int(input("Enter your Choice--->"))
c=random.randint(1,3)
print("You Choose "+computer[u-1])
print("Computer Choose "+computer[c-1])
if(u==c):
   print("Tie!!") 
elif((u==1 and c==3) or (u==2 and c==1) or (u==3 and c==2)):
    print("You Win...........")
elif((u==1 and c==2) or (u==2 and c==3) or (u==3 and c==1)):
    print("You loose...")