a = list(filter(lambda y: y < 25, map(lambda x: x**2, range(10))))

print(a)

b = [i**2 for i in range(10) if i**2 < 25]

print(b)
