class BankAccount:
    def __init__(self, first_name='', last_name='', account_id=0, account_type='', pin=0, balance=0.0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_id = account_id
        self.account_type = account_type
        self.pin = pin
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount 
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount 
        return self.balance
    
    def display_balance(self):
        print(f"Balance actual: ${self.balance:.2f}") #2 por decimales y f por flotante
        return self.balance
    
alejandra = BankAccount('Alejandra', 'Martínez', 12, 'L', 1111, 400.00)

alejandra.deposit(96)
alejandra.withdraw(25)
alejandra.display_balance()
    
    