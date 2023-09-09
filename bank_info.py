import json
from datetime import date

with open('transactions.json') as f:
    business_account = json.load(f)

    print(business_account["override_accounts"][0]["type"])


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