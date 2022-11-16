n=int(input('enter value of n:'))
tousands=n//1000
n1=n%1000
hundreds=n1//100
n2=n1%100
tens=n2//10
n3=n2%10
m=tousands**3+hundreds**3+tens**3+n3**3
if n==m:
    print('it is amstrong')
else :
    print('it is not amstrong number')