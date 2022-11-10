d1=dict(((1,'Anju'),(2,'Thara'),(3,'Liya'),(4,'Sita')))
print({x:d1[x] for x in sorted(d1)})
print({x:d1[x] for x in sorted(d1,reverse=True)})
