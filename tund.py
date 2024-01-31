#5
num = input("kirjutage numbrit: ")
sum = 0
korrutis = 1
for arv in num:
    arv = int(arv)
    sum += arv
    korrutis *= arv
print("Sum:", sum)
print("korrutis:", korrutis)



#4
number = input("kirjutage numbrit: ")
pööratud_arv = ""
for i in range(len(number)-1, -1, -1):
  pööratud_arv += number[i]
print("pööratud arv:", pööratud_arv)

#3
sum = 0
L = 14
for i in range(L + 1):
    sum += i
print("Numbriliste seeriate summa 0-st kuni", L, "on:", sum)






