adders = []

for n in range(1, 4):
    adders.append(lambda x, a=n: x + a)

print(adders[0](10))  # sonuç 11.
# Bu durum aslında fonksiyon yaratılmasıyla ilişkili. Fonksiyon parametresine atanan varsayılan değer aynen tutulur ve fonksiyon 
# çağırılırken de bu değer kullanılır. 

ms = [ 2, 6, 6, 7, 8]
print(ms[3])
