a = int(input("Введите число "))
b = int(input("ВВедите число "))
c = int(input("Введите число "))
if a==b==c:
    print(3)
elif a==b or a==c or b==c or b==a:
    print(2)
else:
    print(0)