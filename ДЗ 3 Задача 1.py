X=int(input("Введіть число: "))
Y=int(input("Введіть число: "))
a=(X+Y)/2
print(a)
if X<a:
    print(a-X,Y-a)
else:
    print(X-a,a-Y)
