#Задано два натуральних числа n і m. Потрібно знайти
#кількість натуральних і кількість простих n-значних чисел
#більших m.
n=int(input("Введіть число: "))
m=int(input("Введіть число: "))
resultNaturalCount=0
resultSimpleCount=0
minNNumber=10**(n-1)
maxNNumber=(10**n)-1
test = 0
if m<minNNumber:
    resultNaturalCount=(maxNNumber-minNNumber)+1
    for number in range(minNNumber,maxNNumber+1):
        if number>1:
            for j in range(2,number):
                if number%j==0:
                    test = test + 1
            if test == 0:       
                resultSimpleCount=resultSimpleCount+1
            test=0
elif m>=minNNumber and m<maxNNumber:
    resultNaturalCount=maxNNumber-m
    for number in range(m+1,maxNNumber+1):
        if number>1:
            for j in range(2,number):
                if number%j==0:
                    test = test + 1
            if test == 0:       
                resultSimpleCount=resultSimpleCount+1
            test=0
else:
    resultNaturalCount=0
    resultSimpleCount=0
print(resultNaturalCount)
print(resultSimpleCount)