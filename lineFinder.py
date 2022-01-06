n = int(input("Enter number of points"))
x = []
y = []
for i in range(0,n):
    x.append(int(input("Enter x "))) 
    y.append(int(input("Enter y ")))
m = (y[len(y)-1] - y[len(y) - 2]) / (x[len(x) - 1] - x[len(x) - 2])
for i in range(0,n):
    if m*x[i] - y[i] == 0:
        f = 0
    else:
        f = 1
if f == 0:
    print(f"{m}x - y = 0")
else:
    print("not on same line")