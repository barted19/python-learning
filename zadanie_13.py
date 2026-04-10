"""Masz zabezpieczyć program tak, żeby:

jeśli użytkownik wpisze coś, co nie jest liczbą
program nie wywalał się
tylko pokazał komunikat:
Invalid input

i działał dalej"""

balance = 1000
attempts = 0

while attempts < 3:
    pin = input("Type your PIN number: ")
    
    try:
        pin = int(pin)
    except ValueError:
        print("That's not an int.")
        continue

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


