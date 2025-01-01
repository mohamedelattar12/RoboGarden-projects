import math
def main():
    r = int(input("pls enter the radius "))
    circumference = 2 * math.pi * r
    area = 2 * math.pi * (r**2)

    print(f"circumference is {circumference}")
    print(f"area is {area}")



main()