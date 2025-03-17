class BankAccount:
    total_accounts = 0 
    all_accounts = [] 

    def __init__(self, account_holder, account_type, initial_balance=0):
        if not account_holder:
            raise ValueError("Must Enter A Name!")
        self.account_holder = account_holder
        self.account_type = account_type  
        self.balance = initial_balance
        self.transactions = [] 
        BankAccount.total_accounts += 1 
        BankAccount.all_accounts.append(self) 
        print(f"New {account_type} Account Created for {account_holder}")

    def deposit(self, amount):
        if not self.validate_amount(amount) or amount > 50000:
            return "Deposit unsuccessful: Invalid amount or exceeds limit."
        self.balance += amount
        self.transactions.append(f"Deposited: ₹{amount}")
        return f"Deposit Successful! New Balance: ₹{self.balance}"

    def withdraw(self, amount):
        transaction_fee = 10
        total_deduction = amount + transaction_fee

        if not self.validate_amount(amount) or total_deduction > self.balance:
            return "Withdrawal Unsuccessful: Insufficient balance or invalid amount."
        self.balance -= total_deduction
        self.transactions.append(f"Withdrawn: ₹{amount} (Fee: ₹{transaction_fee})")
        return f"Withdrawal Successful! New Balance: ₹{self.balance}"

    def transfer(self, recipient, amount):
        if not isinstance(recipient, BankAccount) or not self.validate_amount(amount):
            return "Transfer failed "
        if amount > self.balance:
            return "Transfer failed: Not enough amount."

        self.balance -= amount
        recipient.balance += amount
        self.transactions.append(f"Transferred: ₹{amount} to {recipient.account_holder}")
        recipient.transactions.append(f"Received: ₹{amount} from {self.account_holder}")
        return f"Transfer Successful! New Balance: ₹{self.balance}"

    def check_balance(self):
        return f"Account Balance for {self.account_holder}: ₹{self.balance}"

    def get_transaction_history(self):
        return self.transactions if self.transactions else ["No transactions yet."]

    @classmethod
    def total_bank_accounts(cls):
        return f"Total Bank Accounts: {cls.total_accounts}"

    @staticmethod
    def validate_amount(amount):
        return amount > 0 and amount <= 50000

