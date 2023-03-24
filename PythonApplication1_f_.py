
x = int(input('metres: '))
value = float(input('\n1. міля\n2. дюйм\n3. ярд\n 1 - 3: '))
if value == 1:
    print(x*0.000621371)
elif value == 2:
    print(x*39.3701)
elif value == 3:
    print(x*1.09361)
