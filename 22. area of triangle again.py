import math
s1=int(input('enter a value of s1:'))
s2=int(input('enter a value of s2:'))
s3=int(input('enter a value of s3:'))
s=(s1+s2*s3)
area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print(area)