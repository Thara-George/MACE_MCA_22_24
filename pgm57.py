try:
    n=int(input("Enter a number:"))
    if n<90 or n>120:
        raise ValueError("Abnormal condition")
except ValueError as e:
    print(e)