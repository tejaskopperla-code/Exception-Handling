try:
    num1,num2 =eval(input("Enter two numbers, separted by a coma"))
    result = num1 /num2
    print("The Result is :  ",result)

except ZeroDivisionError:
    print("division by zero is an error !!")

except SyntaxError:
    print("Coma is missing . Please enter numbers separted by coma like this 1,2")

except:
    print("Wrong output")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")