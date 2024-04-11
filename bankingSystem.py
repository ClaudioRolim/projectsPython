
menu = """ 
############ National American Bank ############
==> Select a menu option:\n[1] Deposit\n[2] Withdraw\n[3] Statement\n[0] Exit
==> """

balance = 0
statement = ""
limit = 500
number_withdraw = 0
LIMIT_WITHDRAW = 3

while True:
    option = input(menu)

    if option == "1":
        print("\n############ DEPOSIT ############")
        value = float(input("Enter your deposit amount R$ "))
        print("#################################\n")
        if value > 0:
            balance += value
            statement += "Deposit of R$ {:.2f}.\n".format(value)
        else:
            print("Invalid value.")

    if option == "2":
        print("\n############ WITHDRAW ############")
        value = float(input("Enter your withdraw amount: "))
        print("##################################")
        if number_withdraw == LIMIT_WITHDRAW:
            print("Withdrawal limit reached!! Try again tomorrow.")
            continue
        if balance < value <= 500:
            print("Insufficient balance to withdraw. Please, check your statement.")
            continue
        if value > 500:
            print("Your withdrawal limit is R$ {:.2f}".format(limit))
            continue
        if value > 0:
            balance -= value
            statement += "Withdraw of R$ {:.2f}.".format(value)
            number_withdraw += 1
            continue
        else:
            print("Invalid operation. Try again!!")

    if option == "3":
        print("\n########## STATEMENT ############")
        print("No movement."if not statement else statement)
        print("Statement: R$ {}".format(balance))
        continue

    if option == "0":
        print("Exit the system.")
        SystemExit(0)
        break
