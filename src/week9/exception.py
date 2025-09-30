from pathlib import Path

CURRENT_DIR = Path(__file__).parent

try:
    a = (CURRENT_DIR / "hello.txt").read_text()
    print(a)
except FileNotFoundError:
    print("File not found")
finally:
    print("Done")
