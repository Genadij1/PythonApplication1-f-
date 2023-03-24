
x = int(input('number_1= '))
y = int(input('number_2= '))
value = int(input('\n1. sum\n2. dif\n3. a-mean\n4. product\nОбери варіант від 1 до 4: '))
if value == 1:
	print(x+y)
elif value == 2:
	print(x-y)
elif value == 3:
	print((x+y)/2)
elif value == 4:
	print(x*y)
else:
	print('1-4!')
