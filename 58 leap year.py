y=int(input('enter the year :'))
if (y%400==0) and (y%100==0):
    print('it is a leap Year')
elif (y%4==0) and (y%100!=0):
    print('it is a leap Year')
else:
    print('it is not leap Year')