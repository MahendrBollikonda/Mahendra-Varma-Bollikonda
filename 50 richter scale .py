n=float(input('enter a magenitude:'))
if n<2.0:
	print('micro')
elif n>=2.0 and n<3.0:
	print('very minor')
elif n>=3.0 and n<4.0:
	print('minor')
elif n>=4.0 and n<5.0:
	print('light')
elif n>=5.0 and n<6.0:
	print('moderate')
elif n>=6.0 and n<7.0:
	print('strong')
elif n>=7.0 and n<8.0:
	print('major')
elif n>=8.0 and n<10.0:
	print('greate')
elif n>10.0:
	print('meteroic')