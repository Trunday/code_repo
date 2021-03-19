def adder(n):
    def inner(x):
        return x + n
    return inner


adder_1 = adder(10)
adder_2 = adder(10)
adder_3 = adder(10)
# bir kısayaol?

print(adder_1(1))
print(adder_2(2))
print(adder_3(3))
