a=input('Enter the current year: ')
b=input('Enter the future year: ')
leap=[year for year in range(int(a),int(b)) if(year%400==0)or(year%100 and year%4==0)]
print(leap)      
