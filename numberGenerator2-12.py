import random

d = []
values = {'1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0,
        '10':0,
        '11':0,
        '12':0}
for i in range(200):
    a = random.randint(0,7)
    b = random.randint(0,7)
    c = a+b 
    d.append(c)
for i in d:
    for j in values.keys():
        if i == int(j):
            values[j] = values[j] + 1
print ('list of values :')          
print(d)
print('\n')
print('dictionary of values: ')
print(values)
print('\n')
n=values.items()
print('sorted by size: ')
print(sorted(n))
