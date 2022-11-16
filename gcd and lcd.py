n=int(input('enter a 1 st positive intiger:'))
m=int(input('emter 2 nd positive intiger:'))
while n%m!=0:
     r=n%m
     n=m
m=r
gcd=m
print('gcd',m)




lcm=n%m/gcd
print('lcm',lcm)