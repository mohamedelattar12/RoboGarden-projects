def main():
    while True:
        first_number = input("Please enter a number: ")
        try:
            first_number = int(first_number)
            print(f"You entered the number: {first_number}")
            break
        except ValueError:
            print("That's not a valid number. Please try again.")
    while True:
        second_number = input("Please enter a number: ")
        try:
            second_number = int(second_number)
            print(f"You entered the number: {second_number}")
            break
        except ValueError:
            print("That's not a valid number. Please try again.")

    sum= first_number+second_number
    substraction= first_number - second_number
    multiplication = first_number*second_number
    division = first_number/ second_number

    print("",sum,"\n",substraction,"\n",multiplication,"\n",division)

main()    