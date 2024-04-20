import textwrap


def menu():
    intro = """\n
    ========= National American Bank ==========
        [1] Deposit
        [2] Withdraw
        [3] Statement
        [4] New User
        [5] New Account
        [6] List Accounts
        [0] Exit
        ==> """
    return input(textwrap.dedent(intro))


def deposit(balance, value, statement, /):
    if value > 0:
        balance += value
        statement += "Deposit of R$ {:.2f}.\n".format(value)
        print("\n=== Successful deposit! ===")
    else:
        print("Invalid value.")

    return balance, statement


def withdraw(*, balance, value, statement, limit, number_withdraw, limit_withdraw):

    if number_withdraw >= limit_withdraw:
        print("Withdrawal limit reached!! Try again tomorrow.")

    elif value > balance:
        print("Insufficient balance to withdraw. Please, check your statement.")

    elif value > limit:
        print("Your withdrawal limit is R$ {:.2f}".format(limit))

    elif value > 0:
        balance -= value
        statement += "Withdraw of R$ {:.2f}.".format(value)
        number_withdraw += 1
        print("\n=== Successful withdraw! ===")

    else:
        print("Invalid operation. Try again!!")

    return balance, statement


def show_statements(balance, /, *, statement):
    print("\n === Statements ===")
    print("No movement." if not statement else statement)
    print("Balance: R$ {}".format(balance))
    print("=====================")


def create_account(agency, number_account, users):
    cpf = input("Enter CPF: ")
    user = list_user(cpf, users)

    if user:
        print("\n=== Account created successfully. ===")
        return {"agency": agency, "number_account": number_account, "user": user}

    print("\n=== User not found, account creation flow closed. Create user first. ===")


def list_user(cpf, users):
    users_list = [user for user in users if user["cpf"] == cpf]
    return users_list[0] if users_list else None


def create_user(users):
    cpf = input("Enter CPF: ")
    user = list_user(cpf, users)

    if user:
        print("=== User already registered with CPF. ===")
        return

    name = input("Enter name: ")
    birth_date = input("Enter birth date (YYYY-MM-DD): ")
    address = input("Enter address: ")
    users.append({"name": name, "birth_date": birth_date, "cpf": cpf, "address": address})

    print(f"===== User created successfully! =====")


def list_account(accounts):
    for account in accounts:
        menu_account = f"""\
            Agency: {account['agency']}
            C/C: {account['number_account']}
            Holder: {account['user']['name']}
        """
        print("=" * 50)
        print(textwrap.dedent(menu_account))


def main():
    LIMIT_WITHDRAW = 3
    AGENCY = "0001"

    balance = 0
    statement = ""
    limit = 500
    number_withdraw = 0
    users = []
    accounts = []

    while True:
        option = menu()

        if option == "1":
            print("\n=========== DEPOSIT ===========")
            value = float(input("Enter deposit value: "))
            balance, statement = deposit(balance, value, statement)

        elif option == "2":
            value = float(input("Enter withdraw amount: "))
            balance, statement = withdraw(balance=balance, value=value, statement=statement, limit=limit,
                                          number_withdraw=number_withdraw, limit_withdraw=LIMIT_WITHDRAW)

        elif option == "3":
            show_statements(balance, statement=statement)

        elif option == "4":
            create_user(users)

        elif option == "5":
            number_account = len(accounts) + 1
            account = create_account(AGENCY, number_account, users)
            if account:
                accounts.append(account)

        elif option == "6":
            list_account(accounts)

        elif option == "0":
            print("Exit the system.")
            SystemExit(0)
            break

        else:
            print("Invalid option. Try again!")


main()
