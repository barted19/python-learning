"""program pyta:

username
password

Założenia:

Poprawne dane:

username: admin
password: python123

Logika:

jeśli username i password poprawne → "Login successful"
jeśli username poprawny ale password zły → "Wrong password"
jeśli username zły → "User not found"

Przykłady

Case 1

Username: admin
Password: python123

Login successful

Case 2

Username: admin
Password: 123

Wrong password

Case 3

Username: john
Password: python123

User not found

Wskazówki

Użyj:

if
elif
and
zmienne"""


username = input("Type your username: ")
password = input("Type your password: ")

if username == "admin" and password == "python123":
    print("Login successful")
elif username == "admin" and password != "python123":
    print("Wrong password")
else:
    print("User not found")