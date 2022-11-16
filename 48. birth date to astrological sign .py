m=str(input('enter the month:'))
d=int(input('enter the date:'))
if (m=='dec' or m=='jan') and (d>=22 or d<=19):
    print('capricorn')
elif (m=='jan' or m=='feb') and (d>19 or d<=18):
    print('aquaris')
elif (m=='feb' or m=='mar') and (d>=19 or d<=20):
    print('pisces')
elif (m=='mar' or m=='april') and (d>=21 or d<=19):
    print('aries')
elif (m=='april' or m=='may') and (d>=20 or d<=31):
    print('taurus')
elif (m=='may' or m=='june') and (d>=21 or d<=20):
    print('gemini')
elif (m=='june' or m=='july') and (d>=21 or d<=22):
    print('cancer')
elif (m=='july' or m=='august') and (d>=23 or d<=22):
    print('leo')
elif (m=='august' or m=='sep') and (d>=23 or d<=22):
    print('virgo')
elif (m=='sep' or m=='oct') and (d>=23 or d<=22):
    print('libra')
elif (m=='oct' or m=='nov') and (d>=23 or d<=21):
    print('scorpio')
elif (m=='nov' or m=='dec') and (d>=22 or d<=21):
    print('sagittaruis')
    
