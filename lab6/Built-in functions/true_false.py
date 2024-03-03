tuple = []
t = 'True'
x = input("").split()
n = len(x)
for i in range(n):
    tuple.append(x[i])
for x in tuple:
    if x=='1':
        continue
    else:
        t = 'False'
print(t)