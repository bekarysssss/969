class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, months, percent):
        for i in range(months):
            self.balance += percent*self.balance
    
    def withdraw(self, take):
        if take > self.balance:
            print("Not enough balance!")
        else:
            print("Withdrawing", take, "and your balance:", self.balance-take)
            self.balance = self.balance-take

account = Account("Bekarys", 150000)
account.withdraw(20000)
account.withdraw(160000)
account.deposit(24, 12.5)