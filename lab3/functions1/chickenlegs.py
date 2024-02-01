def solve(numheads, numlegs):
    for num_chickens in range(numheads + 1):
        num_rabbits = numheads - num_chickens

        if (2 * num_chickens + 4 * num_rabbits) == numlegs:
            return num_chickens, num_rabbits

numheads = 35
numlegs = 94
solution = solve(numheads, numlegs)
if solution:
    num_chickens, num_rabbits = solution
print(f"Number of chickens: {num_chickens}")
print(f"Number of rabbits: {num_rabbits}")
