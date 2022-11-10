a=input("Enter first string: ")
b=input("Enter second string: ")
x=a[0:2]
a=a.replace(a[0:2],b[0:2])
b=b.replace(b[0:2],x)
print(a,b)
