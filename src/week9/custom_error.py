class InvalidMarkException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


def main() -> None:
    try:
        mark = 120
        if mark < 0 or mark > 100:
            raise InvalidMarkException("Mark must be between 0 and 100")
        print(f"Valid Mark is {mark}")
    except InvalidMarkException as e:
        print(e)


if __name__ == "__main__":
    main()
