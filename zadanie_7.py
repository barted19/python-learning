"""Zapytaj użytkownika:

wiek
czy ma konto premium (yes/no)

Logika:

premium → "Full access"
wiek < 18 → "Limited access"
w przeciwnym razie → "Standard access"

Przykład:

Age: 16
Premium: no

Limited access"""

age = int(input("How old are you? : "))
accontType = input("Do you have premium account? Type 'yes'/'y' or 'no'/'n' : ")

if accontType in ["yes", "y"]:
    print("Full access")
elif age < 18:
    print("Limited access")
else:
    print("Standard access")