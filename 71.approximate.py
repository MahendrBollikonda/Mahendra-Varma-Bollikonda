n=int(input('enter the number of approximations :'))
pi=3
j=1
for i in range(2,n+1,2):
    j=j+1
    pi=pi+((-1)**j)*4/(i*(i+1)*(i+2))
print('the pi value after',n,'approximations is',pi)