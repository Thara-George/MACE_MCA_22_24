def sum(num):
    if num==1:
        return 1
    else:
        return num+sum(num-1)
n=int(input("Enter limit:"))
print("Sum=",sum(n-1))