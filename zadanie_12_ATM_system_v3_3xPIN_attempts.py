"""
dalsza KONTYNUACJA ATM - 3 próby podania poprawnego PINu.

Założenia:

poprawny PIN: 1234
użytkownik ma maksymalnie 3 próby
jeśli poda dobry PIN → "Access granted"
jeśli poda zły PIN:
program pokazuje ile prób zostało
po 3 błędnych próbach:
"Account blocked"
Przykład
Enter PIN: 1111
Wrong PIN. Attempts left: 2

Enter PIN: 2222
Wrong PIN. Attempts left: 1

Enter PIN: 3333
Account blocked

albo:

Enter PIN: 1111
Wrong PIN. Attempts left: 2

Enter PIN: 1234
Access granted
Wskazówki

Użyj:

while
licznika prób, np. attempts = 0
break"""



balance = 1000
attempts = 0

while attempts < 3:
    pin = int(input("Type your PIN number: "))

    if pin == 1234:
        print("Access granted")

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
        break

    else:
        attempts +=1
        attempts_left = 3 - attempts

        if attempts_left > 0:
            print(f"Wrong PIN number. Attempts left {attempts_left}") 
        else:
            print(f"Account blocked")            


