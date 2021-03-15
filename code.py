diict = {"abc": 100, "def": 200, "xyz": 50}

a = sorted(diict, key=lambda element: diict[element])

print(a)
