upper_or_lower = input("")
upper = 0
lower = 0
for x in upper_or_lower:
        if x.isupper():
            upper +=1
        elif x.islower(): 
            lower+=1
print("Upper:  "+ str(upper))
print("Lower:  " + str(lower))