import sys

size = int(input("Enter size of list: "))
if size <= 0:
    print("Size must be a positive integer.")
    sys.exit(1)

numbers = [0] * size
print(f"array {numbers}")

numbers[0] = 10
numbers[-1] = -5
# 우측 변경
# numbers[size // 2] = 3
numbers[(size - 1) // 2] = 3

print(f"array {numbers}")
