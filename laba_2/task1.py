n = int(input("Введите кол-во строк:"))
triangle = []
for i in range(n):
    temp = []
    for j in range(i+1):
        if j == 0 or j == i:
             temp.append(1)
        else:
             temp.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

    triangle.append(temp)
for temp in triangle:
    print (" ".join(map(str, temp)))

