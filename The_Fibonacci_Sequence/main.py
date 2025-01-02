while True:
    x=int(input("pls enter number of iteration for Fibonacci must be > 2: "))
    if x >2:
        break
l=[0,1]
for i in range(3,(x+1)):
    num= l[0]+l[1]
    l[0]=l[1]
    l[1]=num
    print("num is ",num)