from MySQLdb import _mysql

isRunning = True
print("Hello")
print("In order to work with your database you first need to log in.")
host = input("Input the adress of the host. Leave blank to access the server on localhost: ")
if (len(host) == 0):
    host = "localhost"
port = int(input("Input the port: "))
user = input("Input the username: ")
pswrd = input("Input the password: ")
db = _mysql.connect(host = host, port = port, user = user, password = pswrd)

while (isRunning):
    print("Menu:\n1. Show all pets\n2. Add a new pet\n3. Show specific pet\n4. Teach a pet new commands\n5. Exit\n")
    inp = int(input("Input your choice: "))
    if (inp == 1):
        print("All pets")
    elif (inp == 2):
        print("Added a pet")
    elif (inp == 3):
        print("Showed a pet")
    elif (inp == 4):
        print("Taught a pet")
    elif (inp == 5):
        isRunning = False
    else:
        a = input("Incorrect input. Press Enter to continue\n")
    
        