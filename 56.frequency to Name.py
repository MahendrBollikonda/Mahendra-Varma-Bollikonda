n=float(input('enter a freqency range'))
if n<3e9:
    print('radio waves')
elif n<=3e9 and n>3e12:
    print('micro waves')
elif n<=3e12 and n>4.3e14:
    print('infrared light')
elif n<=4.3e14 and n>7.5e14:
    print('visible light')
elif n<=7.5e14 and n>3e17:
    print('ultra voilet')
elif n<=3e17 and n>3e19:
    print('x rays')
else:
    print('gamma rays')
    
