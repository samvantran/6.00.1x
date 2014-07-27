def calcLowestPayment(balance, annualInterestRate):
    '''
    Write a program that uses bisection search to calculate the minimum fixed monthly payment 
    needed in order pay off a credit card balance within 12 months. 
    
    balance: float - the outstanding balance on the credit card
    annualInterestRate: float - annual interest rate as a decimal
    ''' 
    
    # calculate monthly interest rate, and lower and upper bounds for bisection search
    monthlyInterestRate = annualInterestRate / 12.0
    lowerBound = balance / 12.0
    upperBound = ( balance * ( 1.0 + monthlyInterestRate)**12 ) / 12.0

    def calcPayment(balance, lowerBound, upperBound):
        # copy balance 
        balance2 = balance
        
        # calculate midpoint
        midPoint = (upperBound + lowerBound) / 2.0
        
        # calculate each month's remaining balance after payment & interest
        for i in range(12):
            balance2 -= midPoint
            balance2 += (balance2 * monthlyInterestRate)
        
         # if remaining balance is higher than $0.01, change lower bound to midpoint 
        if balance2 > 0.01:
            return calcPayment(balance, midPoint + 0.01, upperBound)
        # if remaining balance is lower than -$0.01, change upper bound to midpoint
        elif balance < -0.01:
            return calcPayment(balance, lowerBound, midPoint - 0.01)
        else:
            return midPoint   
        
    lowestPayment = round(calcPayment(balance, lowerBound, upperBound), 2)
    print 'Lowest Payment: ', round(lowestPayment, 2)
    
calcLowestPayment(999999, 0.18)