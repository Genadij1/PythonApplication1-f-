
x = int(input('number_1= '))
y = int(input('number_2= '))
z = int(input('number_3= '))
value = int(input('\n1. sum\n2. product\n 1 or 2: '))
if value == 1:
	print(x+y+z)
elif value == 2:
	print(x*y*z)
else:
	print('1 or 2!')