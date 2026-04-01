"""Napisz program:

Program pyta:

imię
rok urodzenia

Program oblicza:

wiek
wiek za 10 lat

Przykład:

What's your name: Bart
Year of birth: 1994

Hello Bart
You are 30 years old
In 10 years you will be 40

Wskazówka:

Musisz użyć:

int
obliczenia matematyczne
zmienne"""


####PODSTAWOWA WERSJA####

# name = input("What's your name? : ")
# birth = int(input("Year of birth: "))

# current_year = 2026
# age = (current_year - birth)

# print(f"Hello {name}!")
# print(f"You are {age} years old.")
# print(f"In 10 years you will be {age + 10}.")


####BARDZIEJ PROFESJONALNA WERSJA - Z UŻYCIEM IMPORTU####

from datetime import datetime

name = input("What's your name? : ")
birth = int(input("Year of birth: "))

current_year = datetime.now().year
age = (current_year - birth)

print(f"Hello {name}!")
print(f"You are {age} years old.")
print(f"In 10 years you will be {age + 10}.")