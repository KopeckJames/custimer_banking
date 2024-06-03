from savings_account import create_savings_account
from cd_account import create_cd_account
# ADD YOUR CODE HERE

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = float(input("What is your opening balance for the savings account? "))
    savings_interest_rate = float(input("What is the interest rate % for the savings account? "))
    savings_months = int(input("How many months for the savings account? "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest_rate, savings_months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"\nSavings Account Interest Earned: ${interest_earned:.2f}")
    print(f"Updated Savings Account Balance: ${updated_savings_balance:.2f}")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = float(input("\nWhat is your opening balance for CD account? "))
    cd_interest_rate = float(input("What is the interest rate  % for CD account? "))
    cd_months = int(input("How many months for CD account? "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest_rate, cd_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"\nCD Account Interest Earned: ${cd_interest_earned:.2f}")
    print(f"Updated CD Account Balance: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    main()
