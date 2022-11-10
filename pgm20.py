d={'name':'Thara','age':21,'course':'MCA'}
k=input("Enter the key to check: ")
if(k in d.keys()):
    print("Key already exists")
else:
    print("Key does not exists")
