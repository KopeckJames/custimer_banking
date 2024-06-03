"""Import the Account class from the Account.py file."""
from Account import Account

def create_cd_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class
    cd_account = Account(balance, 0.0)

  # Calculate interest earned (assuming monthly interest accrual)
    interest_earned = (balance * interest_rate * months / 12)/100

  # Calculate the new balance
    new_balance = balance + interest_earned

  # Update the balance using set_balance with the new balance
    cd_account.set_balance(new_balance)

  # Update the interest earned in the account object (assuming set_interest method exists)
    cd_account.set_interest(interest_earned)

  # Return the updated balance and interest earned
    return new_balance, interest_earned
