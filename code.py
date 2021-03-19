adders = []

for n in range(1, 4):
    adders.append(lambda x: x + n)

print(adders[0](10))  # sonuç istenmeyen bir şekilde 13.
# Çünkü n değeri 'global scope' içerisinde en son 3 değerini aldı. Ve bu da adders içerisindeki fonksiyonlardan
# hangisi çağırılırsa çağırılsın 'x+3' dönüleceği anlamına gelir. Çözüm bir sonraki kodda.
