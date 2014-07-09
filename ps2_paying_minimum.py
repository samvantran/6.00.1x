'''
Problem Statement:
Write a program to calculate the credit card balance after one year if a person only
pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal
'''

# Retrieve data from user
balance = float(raw_input('Please enter starting balance: '))
monthlyPaymentRate = float(raw_input('Please enter the monthly minimum payment rate (ex. 0.05): '))
annualInterestRate = float(raw_input('Please enter the annual interest rate (ex. 0.20): '))
numMonths = float(raw_input('Please enter the number of months of payment: '))

'''
This is an example test case:
balance = 5000
annualInterestRate = 0.20
monthlyPaymentRate = 0.04
'''

def calcRemainingBalance(balance, monthlyPaymentRate, annualInterestRate, numMonths):
    '''
    This fn calculates the remaining balance after deducting the monthly payment then adding interest amount

    balance, annualInterestRate, and monthlyPaymentRate: floats
    numMonths: integer
    '''

    totalPaid = 0
    for i in range(0, numMonths):
        print 'Month: ', i + 1

        monthlyPayment = balance * monthlyPaymentRate
        totalPaid += monthlyPayment
        print 'Minimum monthly payment: ', round(monthlyPayment, 2)

        # subtract payment from balance
        balance = balance - monthlyPayment

        # add interest to balance
        balance = balance + (balance * (annualInterestRate / 12.0))
        print 'Remaining balance: ', round(balance, 2)

    print 'Total paid: ', round(totalPaid, 2)
    print 'Remaining Balance: ', round(balance,2)

print 'Starting balance: ', balance

remainingBalance = calcRemainingBalance(balance, monthlyPaymentRate, annualInterestRate, 12)
