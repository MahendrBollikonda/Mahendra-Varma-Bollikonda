t1=float(input('enter t1 value:'))
g1=float(input('enter g1 value:'))
t2=float(input('enter t2 value:'))
g2=float(input('enter g2 value:'))
import math
term1=math.sin(t1)*math.sin(t2)
term2=math.cos(t1)*math.cos(t2)*math.cos(g1-g2)
distance=6371.01*math.acos(term1+term2)
print('the distance is',distance)
