def ischeck(str):
    if str.startswith('Is'):
        return str
    else:
        return 'Is'+str
s=input("Enter a string:")
print(ischeck(s))