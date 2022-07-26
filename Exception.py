try:
    num1 = int(input("Enter first number "))
    num2 = int(input("Enter Second number "))
    res=num1/num2
    print(res)
except ZeroDivisionError:
    print("Cannot divide by error")
except ValueError:
    print("Enter only integer")
    