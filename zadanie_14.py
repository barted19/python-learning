"""Masz zabezpieczyć program tak, żeby:

jeśli użytkownik wpisze coś, co nie jest liczbą
program nie wywalał się
tylko pokazał komunikat:
Invalid input

i działał dalej"""

###PODSTAWOWA WERSJA###

# balance = 1000
# attempts = 0

# def show_menu():
#     print("1. Withdraw")
#     print("2. Balance")
#     print("3. Exit")

# while attempts < 3:
#     pin = input("Type your PIN number: ")
    
#     try:
#         pin = int(pin)
#     except ValueError:
#         print("\nInvalid input. Please enter a number.\n")
#         continue

#     if pin == 1234:

#         print("Access granted")

#         while True:
           
#             show_menu()
#             option = input(f"\nChoose option:\n\n")
            
#             try:
#                 option = int(option)
#             except ValueError:
#                 print("\nInvalid input. Please enter a number.\n")
#                 continue

#             if option == 1:

#                 while True:

#                     withdraw = input("How much to withdraw? ")

#                     try:
#                         withdraw = int(withdraw)
#                         break
#                     except ValueError:
#                         print("\nInvalid input. Please enter a number.\n")
                        
#                 if withdraw <= balance:
#                     balance -= withdraw
#                     print(f"{withdraw} has been withdrawn")
#                     print(f"Balance after withdraw: {balance}")
#                 else:
#                     print("Insufficient funds")
                        

#             elif option == 2:
#                 print(f"Your balance is {balance}")
                
#             elif option == 3:
#                 print("Good Bye!")
#                 break
#             else:
#                 print("\nInvalid option. Please choose 1, 2, or 3.\n")
#         break
    
#     else:
#         attempts += 1
#         attempts_left = 3 - attempts

#         if attempts_left > 0:
#             print(f"Wrong PIN number. Attempts left {attempts_left}") 
#         else:
#             print(f"Account blocked")       


###LEPSZE WERSJA### - z "return" w funkcji show_menu()    

# balance = 1000
# attempts = 0

# def show_menu():
#     return "\nChoose option:\n\n1. Withdraw\n2. Balance\n3. Exit\n\n"

# def check_pin(pin):

#     if pin == 1234:
#         return True
#     else:
#         return False
    

# while attempts < 3:
#     pin = input("Type your PIN number: ")
    
#     try:
#         pin = int(pin)
#     except ValueError:
#         print("\nInvalid input. Please enter a number.\n")
#         continue

#     if pin == 1234:

#         print("Access granted")

#         while True:
           
#             option = input(show_menu())
            
#             try:
#                 option = int(option)
#             except ValueError:
#                 print("\nInvalid input. Please enter a number.\n")
#                 continue

#             if option == 1:

#                 while True:

#                     withdraw = input("How much to withdraw? ")

#                     try:
#                         withdraw = int(withdraw)
#                         break
#                     except ValueError:
#                         print("\nInvalid input. Please enter a number.\n")
                        
#                 if withdraw <= balance:
#                     balance -= withdraw
#                     print(f"{withdraw} has been withdrawn")
#                     print(f"Balance after withdraw: {balance}")
#                 else:
#                     print("Insufficient funds")
                        

#             elif option == 2:
#                 print(f"Your balance is {balance}")
                
#             elif option == 3:
#                 print("Good Bye!")
#                 break
#             else:
#                 print("\nInvalid option. Please choose 1, 2, or 3.\n")
#         break
    
#     else:
#         attempts += 1
#         attempts_left = 3 - attempts

#         if attempts_left > 0:
#             print(f"Wrong PIN number. Attempts left {attempts_left}") 
#         else:
#             print(f"Account blocked")  


###KROK 2###

balance = 1000
attempts = 0

def show_menu():
    return "\nChoose option:\n\n1. Withdraw\n2. Balance\n3. Exit\n\n"

# def check_pin(pin):

#     if pin == 1234:
#         return True
#     else:
#         return False

##Można jak wyżej ale lepiej jest zapisać to w poniższy sposób##

def check_pin(pin):
    return pin == 1234

def is_valid_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False
    

while attempts < 3:
    pin = input("Type your PIN number: ")
    
    if not is_valid_number(pin):
        print("Invalid input")
        continue

    pin = int(pin)

    if check_pin(pin):

        print("Access granted")

        while True:
           
            option = input(show_menu())
            
            try:
                option = int(option)
            except ValueError:
                print("\nInvalid input. Please enter a number.\n")
            

            if option == 1:

                def withdraw_money(balance):
                
                    while True:

                        withdraw = input("How much to withdraw? ")

                        if not is_valid_number(withdraw):
                            print("Invalid input")
                            continue

                        withdraw = int(withdraw)
                            
                        if withdraw <= balance:
                            balance -= withdraw
                            print(f"{withdraw} has been withdrawn")
                            print(f"Balance after withdraw: {balance}")
                            return balance
                        else:
                            print("Insufficient funds")

            elif option == 2:
                print(f"Your balance is {balance}")
                
            elif option == 3:
                print("Good Bye!")
                break
            else:
                print("\nInvalid option. Please choose 1, 2, or 3.\n")
        break
    
    else:
        attempts += 1
        attempts_left = 3 - attempts

        if attempts_left > 0:
            print(f"Wrong PIN number. Attempts left {attempts_left}") 
        else:
            print(f"Account blocked")  


