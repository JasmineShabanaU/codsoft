import random
import string


def build_character_pool():
    letters = string.ascii_letters
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{}<>?/"

    print("\nChoose character types to include:")
    use_letters = input("Include letters? (y/n): ").strip().lower() == "y"
    use_digits = input("Include numbers? (y/n): ").strip().lower() == "y"
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"

    pool = ""

    if use_letters:
        pool += letters
    if use_digits:
        pool += digits
    if use_symbols:
        pool += symbols

    return pool


def generate_password(length, pool):
    password = "".join(random.choice(pool) for _ in range(length))
    return password


def main():
    print("=" * 35)
    print("      PASSWORD GENERATOR")
    print("=" * 35)

    try:
        length = int(input("Enter password length: "))

        if length <= 0:
            print("Password length must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    character_pool = build_character_pool()

    if not character_pool:
        print("You must select at least one character type.")
        return

    password = generate_password(length, character_pool)

    print("\nGenerated Password:")
    print(password)


if __name__ == "__main__":
    main()
