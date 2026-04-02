"""Program pyta:

wiek
student (yes/no)

Jeśli:

student AND wiek < 26
→ "You get student discount"

Jeśli:

wiek >= 65
→ "You get senior discount"

W przeciwnym razie:

→ "No discount"""

###WERSJA PODSTAWOWA###

# age = int(input("How old are you? : "))
# student_status = input("Are you student? : ").lower()

# if student_status in ["y", "yes"] and age < 26:
#     print("You get student discount")
# elif age >= 65:
#     print("You get senior discount")
# else:
#     print("No discount")

"""Powyższa wersja kodu zadziała poprawnie, ale:

W realnym systemie często senior ma wyższy priorytet.

DLATEGO poniżej jest lepsza wersja. 
"""

###WERSJA LEPSZA###

age =int(input("How old are you? : "))
student_status = input("Are you student? : ").lower()

if age >= 65:
    print("You get senior discount")
elif student_status in ["y", "yes"] and age < 26:
    print("You get student discount")
else:
    print("No discount")

