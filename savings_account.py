"""Import the Account class from the Account.py file."""
from Account import Account


# Define a function for the Savings Account
def create_savings_account(balance, interest_rate, months):
  """Creates a savings account, calculates interest earned, and updates the account balance.

  Args:
      balance (float): The initial savings account balance.
      interest_rate (float): The APR interest rate for the savings account.
      months (int): The length of months to determine the amount of interest.

  Returns:
      tuple[float, float]: A tuple containing the updated savings account balance and the interest earned.
  """

  # Create an instance of the `Account` class
  savings_account = Account(balance, 0.0)

  # Calculate interest earned (assuming monthly interest accrual)
  interest_earned = (balance * interest_rate * months / 12)/100

  # Calculate the new balance
  new_balance = balance + interest_earned

  # Update the balance using set_balance with the new balance
  savings_account.set_balance(new_balance)

  # Update the interest earned in the account object (assuming set_interest method exists)
  savings_account.set_interest(interest_earned)

  # Return the updated balance and interest earned
  return new_balance, interest_earned
