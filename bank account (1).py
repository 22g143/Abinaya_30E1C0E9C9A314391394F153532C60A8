class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0.0):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__account_balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__account_balance >= amount:
                self.__account_balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.__account_balance:.2f}")
            else:
                print("Insufficient funds for withdrawal.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

    def display_balance(self):
        print(f"Account Balance for {self.__account_holder_name}: ${self.__account_balance:.2f}")


# Test the BankAccount class
if __name__ == "__main__":
    # Create an instance of the BankAccount class
    my_account = BankAccount("123456789", "John Doe", 1000.0)

    # Display initial balance
    my_account.display_balance()

    # Deposit money
    my_account.deposit(500.0)

    # Withdraw money
    my_account.withdraw(200.0)
    
    # Try to withdraw more money than available
    my_account.withdraw(1500.0)

    # Display updated balance
    my_account.display_balance()
