balance = 4773
annualInterestRate = .2

monthlyInterestRate = annualInterestRate/12.0
low = balance/12.0
high = (balance*(1+monthlyInterestRate)**12)/12.0

payment = (low+high)/2.0
epsilon = 0.001
remainingBalance = balance

while abs(remainingBalance) > epsilon:
    unpaidBalance = balance - payment
    for month in range(1,13):
        remainingBalance = unpaidBalance * (1.0 + monthlyInterestRate)
        unpaidBalance = remainingBalance - payment
    if remainingBalance > 0: 
        low = payment
    else:
        high = payment
    payment = (low+high)/2.0    

print('Lowest Payment: ' + str(round(payment,2)))