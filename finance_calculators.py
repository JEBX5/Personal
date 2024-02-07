import math

#Program is for financial calculations. It can work out either 1.0 investment returns, or 2.0 bond costs

#print instructions showing users the two options available in program - 'investment' or 'bond':
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll have to pay on a home loan")
print() # line break

#request input of either 'investment' or 'bond' to choose program
selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

print() # line break

# clean 'selection' variable so it is ALWAYS lower case
selection=selection.lower()

# ----------------------------------------- 1.0 INVESTMENT CODING SECTION -----------------------------------------

if(selection == "investment"):

#request variables for investment calculations:
    
    deposit = float(input("Please enter how much money you are depositing: "))
    interest = float(input("Please enter the interest rate without a percent sign: "))
    years = float(input("How many years do you plan to save for?: "))

    print() # line break

    #Request use to choose calculation method:
    calculation_method = input("Enter either 'simple' or 'compound' to choose your calculation method: ")

    print() # line break

    # clean calculation method input so it is lower case
    calculation_method = calculation_method.lower()

    # convert whole number intest into decimal (percentage)
    interest = interest / 100

# -------------------------------- 1.1 SIMPLE Investment Coding ---------------------
    
# if user selects 'simple' method, do the following:
    if(calculation_method == "simple"):

        #amount is the result of the interest calculations
        amount = deposit * (1 + (interest * years))

# -------------------------------- 1.2 COMPOUND Investment Coding ---------------------
        
# if the user selects the 'compound' method, do the following:    
    elif(calculation_method == "compound"):

        #amount is the result of the interest calculations
        amount = deposit * math.pow((1 + interest) , years)
    
# error statement if use does not enter 'simple' or 'compound'
    else:
        print("Please restart the program and enter the correct term of 'simple' or 'compound'")
    
    print()
    print("Your investment of £" + str(round(deposit,2)) + " will grow to £" + str(round(amount,2)) + " after " + str(int(years)) +" years!")
    print()

# ----------------------------- 2.0 BOND CODING SECTION --------------------------------------------------------------------------
    
elif(selection == "bond"):

    #request variables for investment calculations:
    
    house_value = float(input("Please enter the value of your house in £: "))
    interest = float(input("Please enter the annual interest rate you wish to borrow, without a percent sign: "))
    month = int(input("How many months do you want to repay over?: "))

    # convert whole number interest into decimal (percentage)
    interest = interest / 100
   
   # convert annual interest into monthly interest
    monthly_interest = interest / 12

    repayment = (monthly_interest * house_value) / (1 - (1 + monthly_interest) ** (- month))

    print() # line break

    #output message!
    print("Your monthly repayment is £" + str(round(repayment,2)))


else:
    selection = input("Sorry you have inputed an incorrect response, please restart the program and enter either 'investment' or 'bond'")