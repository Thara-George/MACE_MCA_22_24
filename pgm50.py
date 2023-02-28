def arith(a,b):
    return(a+b,a-b,a*b,a/b)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
res=arith(a,b)
print("sum of",a," and ",b,"=",res[0])
print("difference of",a," and ",b,"=",res[1])
print("product of",a," and ",b,"=",res[2])
print("quotient of",a," and ",b,"=",res[3])
