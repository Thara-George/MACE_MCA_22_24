class Book:
    def __init__(self):
        self.title=input("Enter title:")
        self.author=input("Enter author name:")
    def __str(self):
        if(hasattr(self,'publisher')):
            return self.title+'written by'+self.author+'is published by'+self.publisher
        else:
            return 'unknown publisher'
try:
    b=Book()
    print(b,end='\n\n')
    setattr(b,'publisher','penguin')
    print(b)
except Exception as e:
    print(e)