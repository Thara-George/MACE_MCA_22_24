def revr(str):
    if len(str)==1:
        return str[-1]
    else:
        return str[-1]+revr(str[:-1])
s=input("Enter a string:")
print("Reverse of string:",revr(s))
