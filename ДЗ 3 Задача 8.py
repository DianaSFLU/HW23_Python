N=int(input("Введіть число більше за нуль: "))
b=0
while N>0:
    if N%10==2:
        print("TRUE")
        b=1
        N=0
    N=N//10 
if b!=1:
    print("FALSE")
       