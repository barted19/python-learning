"""KONTYNUACJA ZADANIA 9 oraz 10. 

Użycie pętli WHILE

"""

pin = int(input("Type your PIN number: "))
balance = 1000

if pin == 1234:

    while True:
        menu = "1. Withdraw\n2. Balance\n3.Exit\n"
        option = int(input(f"\nChoose option:\n\n{menu}"))

        if option == 1:
            withdraw = int(input("How much to withdraw? "))

            if withdraw <= balance:
                balance -= withdraw
                print(f"{withdraw} has been withdrawn")
                print(f"Balance after withdraw: {balance}")
            else:
                print("Insufficient funds")

        elif option == 2:
            print(f"Your balance is {balance}")
            
        elif option == 3:
            print("Good Bye!")
            break

else:
    print("Wrong PIN number")    