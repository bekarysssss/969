def generate(N):
    for i in range(1, N + 1):
        yield i ** 2

N = 9
generator = generate(N)
for square in generator:
    print(square)
