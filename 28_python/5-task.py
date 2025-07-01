from module1 import BankAccount


account1 = BankAccount("Jose", 1000)

account1.deposit(500)

account1.withdraw(200)

print(f"Current balance: {account1.get_balance()}")

