balance = 4213
annualInterestRate = .2
monthlyPaymentRate = .04

minimumMonthlyPayment = monthlyPaymentRate * balance
monthlyInterestRate = annualInterestRate/12.0
totalPaid = 0.0

monthlyUnpaidBalance = balance - minimumMonthlyPayment

for month in range(1,13):
    print('Month: '+ str(month))
    minimumMonthlyPayment = monthlyPaymentRate * balance
    print('Minimum monthly payment: '+str(round(minimumMonthlyPayment,2)))
    monthlyUnpaidBalance = balance - minimumMonthlyPayment
    balance = monthlyUnpaidBalance*(1.0 + monthlyInterestRate)
    print('Remaining balance: ' + str(round(balance,2)))
    totalPaid += minimumMonthlyPayment

print('Total paid: ' + str(round(totalPaid,2)))
print('Remaining balance: ' + str(round(balance,2)))