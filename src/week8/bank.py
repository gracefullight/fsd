from abc import ABC, abstractmethod


class BankAccount(ABC):
    @abstractmethod
    def withdraw(self, amount: float) -> None:
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance: float) -> None:
        self._balance = balance

    def withdraw(self, amount: float) -> None:
        if amount <= self._balance:
            self._balance -= amount
            print("Savings withdrawal successful")
        else:
            print("Insufficient funds in savings!")


class CheckingAccount(BankAccount):
    def __init__(self, balance: float) -> None:
        self._balance = balance

    def withdraw(self, amount: float) -> None:
        self._balance -= amount
        print("Checking withdrawal (may go negative).")


accounts = [SavingsAccount(500), CheckingAccount(500)]
for acc in accounts:
    acc.withdraw(600)
