"""Napisz program:

Program pyta:

imię
wiek

Program sprawdza:

Jeśli użytkownik ma:

mniej niż 18 → "You are a minor"
18-65 → "You are an adult"
więcej niż 65 → "You are a senior"

Przykład:

Name: Bart
Age: 30

Hello Bart
You are an adult"""

####WERSJA PODSTAWOWA####

# name = input("Name: ")
# age = int(input("Age: "))

# if age < 18:
#     print(f"Hello {name} \nYou are a minor")
# elif 18 <= age <= 65: #WCZESNIEJ TUTAJ MIAŁEM "elif age >= 18 and age <= 65:" - tez działało ale obecne jest czytelniejsze
#     print(f"Hello {name} \nYou are an adult")
# else:
#     print(f"Hello {name} \nYou are a senior")


####WERSJA CLEAN CODE####
name = input("Name: ")
age = int(input("Age: "))

print(f"Hello {name}")

if age < 18:
    print("You are a minor")
elif 18 <= age <= 65:
    print("You are an adult")
else:
    print("You are a senior")

