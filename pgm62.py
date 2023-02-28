class Flower:
    def __init__(self):
        __init__name=input("Enter flower name:")
    def __str(self):
        if(hasattr(self,'petalcolor')):
            return self.petalcolor+""+self.name
        else:
            return "Unknown flower"
    try:
        a.Flower()
        print(a,end,"\n\n")
        setattr(a,"petalcolor","yellow")
        print(a)
    except Exception as e:
        print(e)