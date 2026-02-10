try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age entered")
    else:
        print("Valid age")

except:
    print("Error in age input")

    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd") 