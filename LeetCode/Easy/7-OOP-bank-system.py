from datetime import datetime

class BankAccount:
    # we difine the exchange rates outside the _init_ constructor and within the class attribute
    #we call this | Class Attributes: These are shared among all instances of a class. They are defined within the class but outside any instance methods. Class attributes are accessed using the class name or through an instance | this is useful because the exchange rates are constant values that do not change from one instance to another.

    exchange_rates = {  # Currency conversion rates (relative to USD)
        "USD": 1.0,
        "EUR": 0.91,
        "GBP": 0.76,
        "JPY": 131.5
    }

    def __init__(self, account_holder, initial_balance=0, currency="USD"):
        
        """Initialize a bank account with holder name, balance, and currency
        as attributes. attribute in OOP is shared by all instances of the class
        class attributes is defined within the class costructor"""

        """Instance Attributes or attributes: These are specific to each instance of a class. They are usually defined within the __init__ method and are accessed using the self keyword """
     
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private balance
        self.currency = currency  # Currency of the account
        self.transaction_history = []  # Stores transaction records

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.__balance += amount
            self._record_transaction(f"Deposited {amount} {self.currency}")
            print(f"✅ Deposited {amount} {self.currency}. New balance: {self.__balance} {self.currency}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money if enough balance is available."""
        if amount > self.__balance:
            print(f"❌ Insufficient funds. Available balance: {self.__balance} {self.currency}")
        elif amount > 0:
            self.__balance -= amount
            self._record_transaction(f"Withdrew {amount} {self.currency}")
            print(f"✅ Withdrawn {amount} {self.currency}. Remaining balance: {self.__balance} {self.currency}")
        else:
            print("❌ Withdrawal amount must be positive.")

    def transfer(self, recipient_account, amount):
        """Transfer money to another account, with currency conversion if needed."""
        #isinstance() function to check if the recipient_account is an instance of the BankAccount class
        if not isinstance(recipient_account, BankAccount):
            print("❌ Transfer failed: Invalid recipient account.")
            return False

        if amount <= 0:
            print("❌ Transfer amount must be positive.")
            return False

        if self.__balance < amount:
            print(f"❌ Insufficient funds for transfer. Available balance: {self.__balance} {self.currency}")
            return False

        # Currency conversion
        if self.currency != recipient_account.currency:
            converted_amount = self.convert_currency(amount, self.currency, recipient_account.currency)
            print(f"🔄 Converting {amount} {self.currency} to {converted_amount:.2f} {recipient_account.currency}")
        else:
            converted_amount = amount

        # Perform the transfer
        self.__balance -= amount
        recipient_account.__balance += converted_amount
        self._record_transaction(f"Transferred {amount} {self.currency} to {recipient_account.account_holder}")
        recipient_account._record_transaction(f"Received {converted_amount:.2f} {recipient_account.currency} from {self.account_holder}")

        print(f"✅ Transfer of {amount} {self.currency} to {recipient_account.account_holder} successful.")
        return True

    def get_balance(self):
        """Retrieve the account balance."""
        return self.__balance

    def _record_transaction(self, description):
        """Private method to store transaction history."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append(f"[{timestamp}] {description}")

    def show_transaction_history(self):
        """Print all recorded transactions."""
        print(f"\n📜 Transaction History for {self.account_holder} ({self.currency}):")
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            for transaction in self.transaction_history:
                print(transaction)

    """The @classmethod decorator in Python is used to define a method that is bound to the class and not the instance of the class. This means that the method can be called on the class itself, rather than on instances of the class. The first parameter of a class method is always cls, which refers to the class itself.
    
    """
    @classmethod
    def convert_currency(cls, amount, from_currency, to_currency):
        """Convert an amount from one currency to another based on exchange rates."""
        if from_currency not in cls.exchange_rates or to_currency not in cls.exchange_rates:
            print("❌ Unsupported currency.")
            return amount  # Return the same amount if conversion is not possible
        usd_amount = amount / cls.exchange_rates[from_currency]  # Convert to USD first
        return usd_amount * cls.exchange_rates[to_currency]  # Convert to target currency



"""the SavingsAccount class is defined as a subclass of the BankAccount class to extend the functionality of a standard bank account with additional features specific to a savings account.
By using inheritance, the SavingsAccount class can reuse the attributes and methods of the BankAccount class while adding or modifying features as needed.
Reasons for Defining SavingsAccount as a Subclass| code resuablity | clear structure | specialzed features
"""
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, initial_balance=0, currency="USD", interest_rate=0.02):
        """Constructor for Savings Account, extending BankAccount"""
        super().__init__(account_holder, initial_balance, currency)  # Inherit attributes from BankAccount
        self.interest_rate = interest_rate  # Interest rate in decimal (2% = 0.02)

    def apply_interest(self):
        """Apply interest to the account balance."""
        interest_earned = self.get_balance() * self.interest_rate
        self.deposit(interest_earned)  # Use parent class deposit() method
        print(f"📈 Interest of {interest_earned:.2f} {self.currency} applied.")




#----- here johns_account is an instances of the class (BankAccount)

# Create accounts in different currencies
johns_account = BankAccount("John Doe", 1000, "USD")  # USD account

emilys_savings = SavingsAccount("Emily Smith", 800, "EUR", interest_rate=0.03)  # EUR savings account
liams_account = BankAccount("Liam Brown", 1500, "GBP")  # GBP account

# ✅ Perform deposits and withdrawals
johns_account.deposit(500)
johns_account.withdraw(200)


emilys_savings.deposit(300)

emilys_savings.get_balance()
emilys_savings.apply_interest()  # Apply interest


# ✅ Currency Conversion in Transfer
johns_account.transfer('emilys_savings', 100)  # Transfer from USD to EUR
emilys_savings.transfer(liams_account, 50)  # Transfer from EUR to GBP

# ✅ Show transaction history
johns_account.show_transaction_history()
emilys_savings.show_transaction_history()
liams_account.show_transaction_history()

# ✅ Check final balances
print(f"🔍 John's Final Balance: {johns_account.get_balance()} {johns_account.currency}")
print(f"🔍 Emily's Final Balance: {emilys_savings.get_balance()} {emilys_savings.currency}")
print(f"🔍 Liam's Final Balance: {liams_account.get_balance()} {liams_account.currency}")

