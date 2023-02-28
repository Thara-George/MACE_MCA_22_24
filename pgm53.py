def sumdigit(n):
    if n==0:
        return 0
    else:
        return n%10+sumdigit(int(n/10))
n=int(input("Enter a number:"))
print("Sum of digits:",sumdigit(n))