def calcLowestPayment(balance, annualInterestRate):
    '''
    Write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. 
    
    The following variables contain values as described below:
    balance - the outstanding balance on the credit card
    annualInterestRate - annual interest rate as a decimal
    
    The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
    Lowest Payment: 180 
    
    Assume that the interest is compounded monthly according to the balance at the end of the month 
    (after the payment for that month is made). The monthly payment must be a multiple of $10 
    and is the same for all months. Notice that it is possible for the balance to become negative 
    using this payment scheme, which is okay. A summary of the required math is found below:

    Monthly interest rate = (Annual interest rate) / 12.0
    Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    
    balance, annualInterestRate: float
    Returns int
    ''' 
    #print 'Starting balance:', balance
    #print 'Potential interest amount added to balance over one year', balance * annualInterestRate
    #lowestPayment = totalPayment / 12.0
    #print 'Lowest Payment Needed:', lowestPayment

    # calculate monthly interest rate and init lowest payment denom to 10
    monthlyInterestRate = annualInterestRate / 12.0
    lowestPayment = 10
    
    def checkifEnough(lowestPayment, balance):
        balance2 = balance
        for i in range(0, 12):
            balance2 -= lowestPayment
            balance2 += (balance2 * monthlyInterestRate)
            #print 'Month', i, 'balance:', round(balance2,2)
        
        if balance2 > 0:
            balance2 = balance
            return checkifEnough(lowestPayment+10, balance)
            
        return lowestPayment
   
    lowestPayment = checkifEnough(lowestPayment, balance)
    
    print 'Lowest Payment:', lowestPayment

calcLowestPayment(5000, 0.20)    