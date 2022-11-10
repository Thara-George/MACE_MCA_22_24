a=input("Enter a line of text: ")
n=""
for x in a:
    if(x.isalpha() or x==' '):
        n+=x
print('No.of words in the text= ',len(n.split()))
