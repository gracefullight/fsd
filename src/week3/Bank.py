from collections.abc import Iterable


class InvalidAmountError(ValueError):
    def __init__(self, balance: float, amount: float) -> None:
        super().__init__(f"Invalid amount: balance={balance}, amount={amount}")


class Account:
    def __init__(self, balance: float, account_type: str) -> None:
        self.balance: float = balance
        self.type: str = account_type

    def get_balance(self) -> float:
        return self.balance

    def get_type(self) -> str:
        return self.type

    def deposit(self, amount: float) -> None:
        if amount > 0:
            self.balance += amount
        else:
            print("Deposit amount must be positive.")

    def pay(self, to_account: "Account", amount: float) -> None:
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            to_account.deposit(amount)
        else:
            raise InvalidAmountError(self.balance, amount)

    def withdraw(self, amount: float) -> None:
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
        else:
            raise InvalidAmountError(self.balance, amount)


class Customer:
    def __init__(self, name: str, accounts: Iterable[Account] | None = []) -> None:
        self.name: str = name
        self.accounts: list[Account] = list(accounts) if accounts is not None else []

    def __get_name(self) -> str:
        return self.name

    def __set_name(self, name: str) -> None:
        self.name = name

    def __deposit(self, to_account: Account, amount: float) -> None:
        if to_account in self.accounts:
            to_account.deposit(amount)
            print(f"Deposited ${amount} to {to_account.type} account.")
        else:
            print("Account not found.")

    def __pay(self, from_account: Account, to_account: Account, amount: float) -> None:
        if from_account in self.accounts and to_account in self.accounts:
            if from_account.get_balance() >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)
                print(f"Transferred ${amount} from {from_account.type} to {to_account.type}.")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

    def __withdraw(self, from_account: Account, amount: float) -> None:
        if from_account in self.accounts:
            if from_account.get_balance() >= amount:
                from_account.withdraw(amount)
                print(f"Withdrew ${amount} from {from_account.type} account.")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")


class Manager:
    def __init__(self, name: str) -> None:
        self.name = name

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name

    def view_customers(self, bank: "Bank") -> list[Customer]:
        return bank.customers

    def add_customer(self, bank: "Bank", name: str) -> None:
        bank.add_customer(name)

    def remove_customer(self, bank: "Bank", name: str) -> None:
        bank.remove_customer(name)


class Bank:
    def __init__(
        self,
        branch: str,
        manager: Manager | None = None,
        customers: Iterable[Customer] | None = [],
    ) -> None:
        self.branch: str = branch
        self.manager: Manager | None = manager
        self.customers: list[Customer] = list(customers) if customers is not None else []

    def main(self) -> None:
        amount = float(input("Amount to deposit $ "))
        if amount > 0:
            self.customers[0].accounts[0].deposit(amount)
            print(f"Amount ${amount} deposited.")
        else:
            print("Invalid amount.")

        amount2 = float(input("Amount to withdraw $ "))
        if amount2 > 0:
            try:
                self.customers[0].accounts[0].withdraw(amount2)
                print(f"Amount ${amount2} withdrawn.")
            except InvalidAmountError as e:
                print(e)
        else:
            print("Invalid amount.")

        print(f"Current balance: ${self.customers[0].accounts[0].get_balance()}")

    def __manager_login(self) -> None:
        if self.manager is None:
            print("No manager assigned to this bank.")
            return
        print(f"Manager {self.manager.name} logged in.")

    def __customer_login(self) -> None:
        if not self.customers:
            print("No customers registered in this bank.")
            return
        print(f"Customer {self.customers[0].name} logged in.")

    def add_customer(self, name: str) -> None:
        customer = Customer(name)
        self.customers.append(customer)
        print(f"Customer {name} added to the bank.")

    def remove_customer(self, name: str) -> None:
        for i, customer in enumerate(self.customers):
            if customer.name == name:
                del self.customers[i]
                break
        print(f"Customer {name} removed from the bank.")

    def __bank_menu(self) -> None:
        print("Welcome to the Bank!")
        print("1. Manager Login")
        print("2. Customer Login")
        print("3. Add Customer")
        print("4. Remove Customer")
        print("5. Exit")
        choice = input("Please choose an option: ")

        match choice:
            case "1":
                self.__manager_login()
            case "2":
                self.__customer_login()
            case "3":
                name = input("Enter customer name: ")
                self.add_customer(name)
            case "4":
                name = input("Enter customer name to remove: ")
                self.remove_customer(name)
            case "5":
                print("Exiting...")
            case _:
                print("Invalid option. Please try again.")


bank = Bank("ultimo", Manager("John Doe"), [Customer("EK", [Account(0, "Saving")])])
bank.main()
