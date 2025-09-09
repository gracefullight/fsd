from datetime import UTC, datetime


class Account:
    def __init__(self, acc_type: str) -> None:
        self.acc_type = acc_type
        self.balance = 0.0

    def deposit(self) -> None:
        try:
            amount = float(input(f"Amount to deposit into {self.acc_type} $"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        if amount > 0:
            self.balance += amount
            print(f"Amount ${amount:.2f} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self) -> None:
        try:
            amount = float(input(f"Amount to withdraw from {self.acc_type} $"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Amount ${amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient funds or invalid amount.")

    def transfer(self, target_acc: "Account") -> None:
        if target_acc is None:
            print("Target account not found.")
            return
        try:
            amount = float(
                input(f"Amount to transfer from {self.acc_type} to {target_acc.acc_type} $")
            )
        except ValueError:
            print("Invalid input. Please enter a number.")
            return
        if 0 < amount <= self.balance:
            self.balance -= amount
            target_acc.balance += amount
            print(f"Amount ${amount:.2f} transferred successfully.")
        else:
            print("Insufficient funds or invalid amount.")

    def __str__(self) -> str:
        """Return a human-readable balance line for this account."""
        return f"{self.acc_type} Account Balance: ${self.balance:.2f}"


class Customer:
    def __init__(self, name: str) -> None:
        self.name = name
        self.accounts = [Account("Savings"), Account("Loan")]

    def get_account(self, acc_type: str) -> Account | None:
        target = acc_type.strip().lower()
        for acc in self.accounts:
            if acc.acc_type.lower() == target:
                return acc
        print("No valid account type")
        return None

    def deposit(self) -> None:
        acc = self.get_account("Savings")
        if acc:
            acc.deposit()

    def withdraw(self) -> None:
        acc = self.get_account("Savings")
        if acc:
            acc.withdraw()

    def transfer(self) -> None:
        from_acc = self.get_account("Savings")
        to_acc = self.get_account("Loan")
        if from_acc and to_acc:
            from_acc.transfer(to_acc)

    def help_message(self) -> None:
        print(
            "Please type following command:\n"
            "d - deposit\n"
            "w - withdraw\n"
            "t - transfer\n"
            "s - show balance\n"
            "x - exit"
        )

    def show(self) -> None:
        print(f"{self.name} bank statement: {datetime.now(tz=UTC)}")
        print(self.get_account("Savings"))
        print(self.get_account("Loan"))

    def main(self) -> None:
        user_input = input("start banking (d/w/t/s/x):").strip().lower()
        while user_input != "x":
            match user_input:
                case "d":
                    self.deposit()
                case "w":
                    self.withdraw()
                case "t":
                    self.transfer()
                case "s":
                    self.show()
                case _:
                    self.help_message()
            user_input = input("start banking (d/w/t/s/x):").strip().lower()
        # Finish while loop, then good bye
        print("Return back to Bank Menu!")

    def __str__(self) -> str:
        """Return a summary of the customer and their accounts/balances."""
        return (
            f"Customer(name={self.name}\t--> "
            f"{self.get_account('Savings')} | {self.get_account('Loan')})"
        )


class Manager:
    def __init__(self, name: str = "Admin") -> None:
        self.name = name

    def view_customers(self, customers: list[Customer]) -> None:
        if not customers:
            print("No customers found.")
            return
        print(f"Customers managed by {self.name}:")
        for i, cus in enumerate(customers, start=1):
            print(f"{i}. {cus.name}")


class Bank:
    def __init__(self) -> None:
        self.customers = self.init_customers()
        self.manager = Manager()

    def init_customers(self) -> list[Customer]:
        temp: list[Customer] = []
        for i in range(3):
            name = input(f"Enter customer {i + 1} name:")
            temp.append(Customer(name))
        return temp

    def help_message(self) -> None:
        print("Bank Menu options:\nl - login as customer\nv - view all customers\nx - exit")

    def view(self) -> None:
        if not self.customers:
            print("No customers to show.")
            return
        for cus in self.customers:
            print(cus)

    def login(self) -> None:
        name = input("Enter your name: ").strip()
        for cus in self.customers:
            if cus.name.lower() == name.lower():
                cus.main()
                return
        print("Invalid customer name")

    def main(self) -> None:
        user_input = input("Bank Menu (l/v/x):").strip().lower()
        while user_input != "x":
            match user_input:
                case "l":
                    self.login()
                case "v":
                    # Manager view for convenience
                    self.manager.view_customers(self.customers)
                    self.view()
                case _:
                    self.help_message()
            user_input = input("Bank Menu (l/v/x):").strip().lower()
        # Finish while loop, then good bye
        print("Thanks for using us! Good bye!")


bank = Bank()
bank.main()
