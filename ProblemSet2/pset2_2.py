balance = 3926
annualInterestRate = .2

monthlyInterestRate = annualInterestRate/12.0
payment = 10

while True:
    unpaidBalance = balance - payment
    for month in range(1,13):
        remainingBalance = unpaidBalance * (1.0 + monthlyInterestRate)
        unpaidBalance = remainingBalance - payment
    if remainingBalance > 0: 
        payment += 10
    else:
        break

print('Lowest Payment: ' + str(payment))