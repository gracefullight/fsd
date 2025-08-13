from random import randint
from typing import Any


class Bank:
    def __init__(self, name: str) -> None:
        self.name = name

    def main(self) -> None:
        deposit = float(input("Amount to deposit $"))

        print(f"Amount ${deposit:.2f} deposited")


class Customer:
    def __init__(self, name: str, gender: str) -> None:
        self.customerId = randint(1, 100)
        self.name = name
        self.gender = gender
        self.accounts: list[Any] = []

    def login(self) -> None:
        pass

    def logout(self) -> None:
        pass


class BankAccount:
    def __init__(self, account_type: str) -> None:
        self.balance = 0
        self.type = account_type

    def withdraw(self, amount: int) -> None:
        self.balance -= amount

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def transfer(self, amount: int, target_account: "BankAccount") -> None:
        if self.balance >= amount:
            self.withdraw(amount)
            target_account.deposit(amount)

    def show_balance(self) -> None:
        print(self.balance)
