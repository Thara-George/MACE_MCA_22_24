li=list(map(int(input("enter list of numbers:").split())))
i=0
c=0
n=int(input("Enter element to search:"))
while(i<len(li)):
    if li[i]==n:
        c=c+1
    i=i+1
if c==0:
    print("Item not found")
else:
    print("Item found",c,"times")