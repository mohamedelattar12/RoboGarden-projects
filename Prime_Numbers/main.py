n=int(input("pls enter the range n "))

for i in range(1,n+1):
    if i==1 or i==2 or i==3:
        print(i)
    else:
        for j in range(2,int(i/2+1)):
            if i%j==0:
                break
        else:
            print(i)

