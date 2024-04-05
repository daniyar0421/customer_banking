# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE\
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    
    saving_balance= float(input("what was the saving account balance? "))
    saving_interest= float (input("what is the apr for the savings acount?"))
    savings_maturity= int(input("what is the total number of months you want to calculate the interest gained on the account?"))

    # Call the create_savings_account function and pass the variables from the user.
   
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    
    print("The interest earned on the savings account is: $", format (interest_earned, ',.2f'))
    print('The future savings account balance after',savings_maturity,'months is: $', format(updated_savings_balance, ',.2f'))
    
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    cd_balance= float(input('what is your initial CD account balance?'))
    cd_interest= float(input('What is the APR for the CD account?'))
    cd_maturity= int(input('What is the lenghs of months for your CD ?'))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    print('The interest on the CD is : $', format{interest_earned, ',.2f'})
    print('The future CD account balance after',cd_maturity,'months is: $', format{updated_cd_balance, ',.2f'})
if __name__ == "__main__":
    main()
