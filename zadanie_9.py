"""Program pyta:

PIN

Poprawny PIN:

1234

Logika:

Jeśli PIN poprawny:

Program pyta:

Withdraw
Balance
Exit

Założenia:

Balance = 1000

Jeśli:

Withdraw → zapytaj ile wypłacić
Balance → pokaż saldo
Exit → zakończ program

Przykład

Enter PIN: 1234

1. Withdraw
2. Balance
3. Exit

Choose option: 2

Your balance is 1000"""

pin = int(input("Type your PIN number: "))
balance = 1000



if pin == 1234:
    menu = "1. Withdraw\n2. Balance\n3. Exit\n"
    option = int(input(f"{menu}"))

    if option == 2:
        print(f"Your balance is {balance}")
    elif option == 1:
        print("Funds has been withdrawn from the account")
    else:
        print("Good Bye!")

else:
    print("Wrong PIN number")