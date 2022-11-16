n=int(input('enter a first  :'))
s=0
c=0
while n!=0:
    s=s+n
    c=c+1
    n=int(input('enter the next number :'))
average=s/c
print('the sum of {} number is {}'.format(c,s))
print('the average of {} number is {}'.format(c,average))