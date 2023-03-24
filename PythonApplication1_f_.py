
x = int(input('number_1= '))
y = int(input('number_2= '))
z = int(input('number_3= '))
value = int(input('\n1. max\n2. min\n3. a-mean\n  1 - 3: '))
if value == 1:
    if x > y > z:
        print(x)
    elif y > x > z:
        print(y)
    elif z > x > y:
        print(z)
if value == 2:
    if x < y < z:
        print(x)
    elif y < x < z:
        print(y)
    elif z < x < y:
        print(z)
if value == 3:
    print(x*y*z)
else:
    print("1 - 3!")
    
   