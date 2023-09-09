import json
from datetime import date, timedelta, datetime


# Define a function to filter transactions within the past 30 days
def filter_transactions(transactions):
    today = date.today()
    thirty_days_ago = today - timedelta(days=30)

    filtered_transactions = []

    for transaction in transactions:
        date_transacted = datetime.strptime(transaction["date_transacted"], "%Y-%m-%d").date()
        if thirty_days_ago <= date_transacted <= today:
            filtered_transactions.append(transaction)

    return filtered_transactions

with open('transactions.json') as f:
    business_account = json.load(f)

    # Get transactions for the first account
    checking_transactions = business_account["override_accounts"][0]["transactions"]
    filtered_checking_transactions = filter_transactions(checking_transactions)

    # Get transactions for the second account
    savings_transactions = business_account["override_accounts"][1]["transactions"]
    filtered_savings_transactions = filter_transactions(savings_transactions)
    print("Checking Account Transactions in the Last 30 Days:")
    for transaction in filtered_checking_transactions:
        print(transaction)

    print("\nSavings Account Transactions in the Last 30 Days:")
    for transaction in filtered_savings_transactions:
        print(transaction)
class BankInfo:
    """
    This is the class that has all the information of the user's bank statement
    """
    def get_current_date(self):
        today = date.today()
        return today
    def get_total_checking(self):
        pass
    def set_total_checking(self):
        pass
    def get_total_saving(self):
        pass
    def set_total_saving(self):
        pass
    def get_total_spend(self):
        pass
    def get_total_earned(self):
        pass
    def get_rent(self):
        pass
    def get_food(self):
        pass
    def get_transportation(self):
        pass
    def get_travel(self):
        pass
    def get_other(self):
        pass
    def get_progress_percentage(self):
        pass
    def get_budget_goal_percentage(self):
        pass