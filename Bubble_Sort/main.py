def main():
    list = [2,5,3,6,76,8,2,1,0,76,44]
    length= len(list)
    for i in range(length-1):
        for j in range(length-1):
            if list[j+1]<list[j]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp

    print(list)

main()