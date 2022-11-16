a=int(input('enter cofficient of x² :'))
b=int(input('enter cofficient of x :'))
c=int(input('enter constant :'))
d=(b**2)-(4*a*c)
if d>0:
    root1=(-b+(d**0.5))/(2*a)
    root2=(-b-(d**0.5))/(2*a)
    print(root1)
    print(root2)
else:
    print('roots are complex')