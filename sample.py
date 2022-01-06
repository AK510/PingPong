n = int(input("Enter number of points"))
c = input("Enter co-ordinates")
colist = c.split(" ")
clist = []
for x in colist:
    clist.append(int(x))
m = (clist[1] - clist[3]) / (clist[0] - clist[2])
for i in range(0, n, 2):
    if m*clist[i] - clist[i+1] == 0:
        f = 0
    else:
        f = 1
if f == 0:
    if m < 0:
        m *= -1
        print(f"{m}x + y = 0")
    else:
        print(f"{m}x - y = 0")
else:
    print("not on same line")