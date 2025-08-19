import sys

MAX_VOTING_AGE = 70
MIN_VOTING_AGE = 18

age = 18  # int(input("What is your age: "))

if age > MAX_VOTING_AGE:
    print("Optional voting in Australia")
elif age >= MIN_VOTING_AGE and age <= MAX_VOTING_AGE:
    print("Eligible to vote in Australia!")
else:
    print("Not eligible")


balance = 1000
account_blocked = False
withdrawals = [200, 500, 400]

for amount in withdrawals:
    if account_blocked:
        print("Account is blocked. Stopping transactions.")
        break

    if balance >= amount:
        balance -= amount
        print(f"Withdrew {amount}. | New balance: {balance}")
    else:
        print(f"Insufficient funds for {amount}")


SKIP_NUMBER = 5

for i in range(1, 11):
    if i == SKIP_NUMBER:
        continue
    print(i)


MAX_FACTORIAL_INPUT = 20

n = int(input("Enter n: "))
if n < 0:
    print("Factorial is not defined for negative numbers")
    sys.exit()
elif n > MAX_FACTORIAL_INPUT:
    print("Too large to calculate")
    sys.exit()

fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"The factorial of {n} is {fact}")
