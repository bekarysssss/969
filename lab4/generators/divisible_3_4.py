def itr_numbers(n):
    i = 0
    while i <=n:
        if(i%12 == 0):
            yield i
        i+=1

numbers = itr_numbers(int(input()))
for x in numbers:
    print(x, end = ' ')