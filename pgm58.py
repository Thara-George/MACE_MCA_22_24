class Validate(Exception):pass
try:
    username:"Thara"
    password:"Thara@123"
    user=input("Enter username:")
    passwd=input("Enter password:")
    if user!=username or passwd!=password:
        raise Validate("Invalid user credentials:")
    else:
        print("login succes")
except Validate as e:
    print(e)
