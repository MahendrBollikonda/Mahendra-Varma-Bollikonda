import math
h=int(input('enter hight:'))
a=float(input('enter the accelration:'))
vi=int(input('enter the intial speed:'))
vf=math.sqrt(vi**2+2*a*h)
print('the final speed is',vf,'m/s')