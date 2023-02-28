try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print(a/b)
except ZeroDivisionError as ze:
    print("Division by zero error",ze)
except ValueError as e:
    print("Non integer value entered",e)