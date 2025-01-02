x=int(input("pls enter a number: "))
num=x
while x>1:
    num=num*(x-1)
    x-=1
if x==0:
    print(1)
else:
    print(num)