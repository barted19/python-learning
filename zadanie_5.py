"""Program pyta:

wiek
czy masz prawo jazdy (yes/no)

Program sprawdza:

Jeśli:

wiek >= 18
AND ma prawo jazdy

→ "You can drive"

W przeciwnym razie:

→ "You cannot drive"

Przykład:

Age: 25
Do you have a license: yes

You can drive"""

####WERSJA PODSTAWOWA####

# age = int(input("How old are you? : "))
# drive_licence = input("Do you have a drive licence? Type 'y' or 'yes' to confirm : ")

# if (drive_licence == "y" or drive_licence == "yes") and age >= 18:
#     print("You can drive")
# else:
#     print("You cannot drive")

####WERSJA LEPSZA####

# age = int(input("How old are you? : "))
# drive_licence = input("Do you have a drive licence? Type 'y' or 'yes' to confirm : ").lower() #.lower() - zabezpiecza przed mieszaniem wielkości liter

# if(drive_licence == "y" or drive_licence == "yes") and age >= 18:
#     print("You can drive")
# else:
#     print("You cannot drive")

####WERSJA PRO####
age = int(input("How old are you? : "))
drive_licence = input("Do you have a drive licence? Type 'y' or 'yes' to confirm : ").lower()

if drive_licence in ["y", "yes"] and age >= 18:
    print("You can drive")
else:
    print("You cannot drive")
    

