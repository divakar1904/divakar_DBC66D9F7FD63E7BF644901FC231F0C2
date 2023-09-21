class BankAccount:

    def __init__(self, account_number, account_holder_name, account_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = account_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if self.__account_balance >= amount:
            self.__account_balance -= amount
        else:
            print("Insufficient balance")

    def display_balance(self):
        return self.__account_balance

# creating instance for testing
account = BankAccount('1234567890', 'John Doe', 1000)
account.deposit(500)
print(account.display_balance()) # should display 1500
account.withdraw(200)
print(account.display_balance()) # should display 1300
