p=int(input('enter a princple : '))
r=int(input('enter a rate of intrest :'))
t=int(input('enter a pireod of time :'))
amount=p*(pow((1+r/100),t))
ci=amount-p
print('compound intrest',ci)
print('total amount',amount)
