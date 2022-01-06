s = int(input("Enter number of step"))
n=0
while s!=0:
    if s%2==0:
        s /=2
    else:
        s -=1
    n+=1
print(n)