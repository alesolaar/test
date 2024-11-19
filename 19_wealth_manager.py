class BankAccount:
  def __init__(self, initial_balance=0):
    self.balance = initial_balance

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError('Deposit amount must be positive')
    self.balance += amount

  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError('Withdrawal amount must be positive')
    if amount > self.balance:
      raise ValueError('Insufficient funds')
    self.balance -= amount


import unittest

class TestBankAccount(unittest.TestCase):
    # setUp: Inicializa un objeto BankAccount antes de cada prueba
    def setUp(self):
        self.account = BankAccount(initial_balance=100)

    # tearDown: Limpia los recursos después de cada prueba
    def tearDown(self):
        self.account = None

    # Prueba: Verificar que el balance inicial es 100
    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)

    # Prueba: Depositar una cantidad positiva
    def test_deposit_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)  # Balance esperado: 100 + 50

    # Prueba: Depositar 0 debería lanzar un ValueError
    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    # Prueba: Retirar una cantidad v
