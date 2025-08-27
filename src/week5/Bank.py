class Bank:
    def __init__(self) -> None:
        self.balance = 1000.0

    def get_initial_balance(self) -> float:
        return float(input("Starting balance $"))

    def get_user_input(self, input_for: str) -> float:
        return float(input(f"Amount to {input_for} $"))

    def deposit(self) -> None:
        deposit_amount = self.get_user_input("deposit")
        self.balance += deposit_amount
        print(f"Amount ${deposit_amount:.2f} deposited successfully.")

    def withdraw(self) -> None:
        withdraw_amount = self.get_user_input("withdraw")
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print(f"Amount ${withdraw_amount:.2f} withdrawn successfully.")
        else:
            print("Insufficient funds.")

    def show_balance(self) -> None:
        print(f"Current balance is ${self.balance:.2f}")

    def help_message(self) -> None:
        print(
            "Please type following command:\nd - deposit\nw - withdraw\ns - show balance\nx - exit"
        )

    def get_users_input(self) -> None:
        pass

    def main(self) -> None:
        user_input = input("start banking (d/w/s/x):").strip().lower()
        while user_input != "x":
            match user_input:
                case "d":
                    self.deposit()
                case "w":
                    self.withdraw()
                case "s":
                    self.show_balance()
                case _:
                    self.help_message()
            user_input = input("start banking (d/w/s/x):").strip().lower()
        # Finish while loop, then good bye
        print("Thanks for using us! Good bye!")
