t=float(input ('enter a air temp in celcius '))
v=float(input('enter a wind velacity in km per hr '))
T=t+273.15
wci=13.12+0.6215*T-11.37*v**0.16+0.3965*T*v**0.16
print(wci)