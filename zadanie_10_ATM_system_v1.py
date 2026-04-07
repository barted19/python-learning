"""KONTYNUACJA ZADANIA 9

Dodaj:

Jeśli withdraw:

Program pyta:

How much to withdraw?

Jeśli kwota > balance:

Insufficient funds

W przeciwnym razie:

odejmij z balance
pokaż nowe saldo

"""

####WERSJA PODSTAWOWA####

# pin = int(input("Type your PIN number: "))
# balance = 1000

# if pin == 1234:
#     menu = "1. Withdraw\n2. Balance\n3. Exit\n"
#     option = int(input(f"\nChoose option\n\n{menu}\n"))

#     if option == 1:
#         withdraw = int(input("How much to withdraw? : "))

#         if withdraw <= balance:
#            balance_after_withraw = balance - withdraw
#            print(f"{withdraw} has been withdrawn from the account.\nBalance after withdraw: {balance_after_withraw}")
#         else:
#             print("Insufficient funds")   

#     elif option == 2:
#         print(f"Your balance is {balance}")

#     else:
#         print("Good Bye!")

# else:
#     print("Wrong PIN number")


####WERSJA LEPSZA####

pin = int(input("Type your PIN number: "))
balance = 1000

if pin == 1234:
    menu = "1. Withdraw\n2. Balance\n3. Exit\n"
    option = int(input(f"\nChoose option\n\n{menu}\n"))

    if option == 1:
        withdraw = int(input("How much to withdraw? : "))

        if withdraw <= balance:
           balance -= withdraw ##tutaj byla zamiana skladni/updatu balance. Zamiast tworzyc nowa zmianna, po prostu dokonalismy updatu zmiannej "balance"
           print(f"{withdraw} has been withdrawn")
           print(f"Balance after withdraw: {balance}")
        else:
            print("Insufficient funds")   

    elif option == 2:
        print(f"Your balance is {balance}")

    else:
        print("Good Bye!")

else:
    print("Wrong PIN number")

