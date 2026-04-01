"""Napisz program:

Program pyta użytkownika o:

imię
wiek

Program ma wypisać:

Hello Bart!
You are 30 years old.
Next year you will be 31.
Wymagania

Użyj:

input
print
zmiennych
konwersji int"""


############ PIERWOTNA WERSJA ##############

# name = input("What's your name: ")

# print("Hello " + name + "!")

# age = int(input("How old are you?\n"))

# print("You are " + str(age) + " years old")
# print("Next year you will be " + str(age +1))

############ LEPSZA/DYNAMICZNA WERSJA ##############

# name = input("What's your name?\n")
# print(f"Hello {name}!")

# age = int(input("How old are you?\n"))
# print(f"You are {age} year's old")
# print(f"Next year you will be {age+1}")


############ KRÓTKA/JESZCZE BARDZIEJ DYNAMICZNA WERSJA ##############

# print(f"Hello {input("What's your name: ")}")
# print(f"You are {(age := int(input("How old are you? ")))} \nNext year you will be {age +1}")
# print(age) #tutaj pokaze przed dodaniem +1

#######BRUDNOPIS#######

# age = int(input("Age: "))
# print(age + 1)