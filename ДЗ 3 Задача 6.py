A=int(input("Введіть число: "))
B=int(input("Введіть число більше за перше: "))
count=1
for elem in range(A,B+1):
    if elem%2==0 and elem%3==0:
        count=count*elem
if count==1:
    print(count-1)
else:
    print(count)
