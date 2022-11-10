l1=list(map(int,input("Enter the first list: ").split()))
l2=list(map(int,input("Enter the second list: ").split()))
if(len(l1)==len(l2)):
    print("Both list has Same length")
else:
    print("Both list has Different length")
if(sum(l1)==sum(l2)):
    print("Both list has Same Sum")
else:
    print("Both list has Different Sum")
if(set(l1)&set(l2)):
    print("Common values are: ",set(l1)&set(l2))
else:
    print("No Common values")
    

