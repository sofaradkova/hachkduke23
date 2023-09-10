import json
from datetime import date, timedelta, datetime

def filter_transactions(transactions):
    today = date.today()
    thirty_days_ago = today - timedelta(days=30)

    filtered_transactions = []

    for i in transactions:
        date_transacted = datetime.strptime(i["date_transacted"], "%Y-%m-%d").date()
        if thirty_days_ago <= date_transacted <= today:
            filtered_transactions.append(i)

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
    for i in filtered_checking_transactions:
        print(i)

    print("\nSavings Account Transactions in the Last 30 Days:")
    for i in filtered_savings_transactions:
        print(i)

class BankInfo:
    """
    This is the class that has all the information of the user's bank statement
    """

    def __init__(self, checking_transactions, saving_transactions):
        self.checking_transactions = checking_transactions
        self.saving_transactions = saving_transactions
        self.checking = business_account["override_accounts"][0]
        self.saving = business_account['override_accounts'][1]
    @staticmethod
    def calculate_balance(transactions, starting_balance):
        total = sum(i["amount"] for i in transactions)
        return starting_balance + total if total > 0 else starting_balance - abs(total)

    @staticmethod
    def calculate_total_spent(transactions):
        spent_transactions = [i for i in transactions if i["amount"] < 0]
        total_spent = abs(sum(i["amount"] for i in spent_transactions))
        return total_spent

    @staticmethod
    def calculate_total_earned(transactions):
        earned_transactions = [i for i in transactions if i["amount"] > 0]
        total_earned = abs(sum(i["amount"] for i in earned_transactions))
        return total_earned

    def calculate_category_total(self, transactions, category):
        category_transactions = [i for i in transactions if category in i["description"].lower()]
        total = sum(i["amount"] for i in category_transactions)
        return abs(total)

    def get_checking_balance(self):
        return self.calculate_balance(self.checking_transactions, self.checking["starting_balance"])

    def get_saving_balance(self):
        return self.calculate_balance(self.saving_transactions, self.saving["starting_balance"])

    def get_total_spent(self):
        return self.calculate_total_spent(self.checking_transactions)

    def get_total_earned(self):
        return self.calculate_total_earned(self.checking_transactions)

    def get_rent(self):
        return self.calculate_category_total(self.checking_transactions, "rent")

    def get_food(self):
        return self.calculate_category_total(self.checking_transactions, "food")

    def get_transportation(self):
        return self.calculate_category_total(self.checking_transactions, "transportation")

    def get_travel(self):
        return self.calculate_category_total(self.checking_transactions, "travel")

    def get_other(self):
        return self.calculate_category_total(self.checking_transactions, "miscellaneous")

    def get_progress_percentage(self):
        pass

    def get_budget_goal_percentage(self):
        pass

bank = BankInfo(filtered_checking_transactions, filtered_savings_transactions)
print(bank.get_travel())
print(bank.get_total_spent())
print(bank.get_total_earned())