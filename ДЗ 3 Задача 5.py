A=int(input("Введіть число: "))
B=int(input("Введіть число більше за перше: "))
a=1
for elem in range(A,B+1):
    while a<=elem:
        print(elem)
        a=a+1
    a=1