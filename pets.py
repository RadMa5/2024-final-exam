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
        db.query("""SELECT idmansfriends, name, species FROM pets.mansfriends""")
        r = db.store_result()
        print(r.fetch_row(maxrows = 0, how = 0))
    elif (inp == 2):
        nm = input("Input pet's name: ")
        sp = input("Input pet's species: ")
        cls = input("What class this pet belongs to? Enter 1 for domestic animals or 2 for pack animals: ")
        year = input("Input year of birth: ")
        mnth = input("Input month of birth: ")
        day = input("Input day of birth: ")
        dob = str(year + "-" + mnth + "-" + day)
        print(dob)
        db.query("""INSERT INTO pets.mansfriends (name, species, classid, DOB) VALUES('%s', '%s', %s, '%s')""" % (nm, sp, cls, dob))
    elif (inp == 3):
        i = input("Input the ID of a pet you wish to see: ")
        db.query("""SELECT * FROM pets.mansfriends WHERE idmansfriends = """ + i)
        r = db.store_result()
        print(r.fetch_row(maxrows = 0, how = 1))
    elif (inp == 4):
        i = input("Input ID of pet you want to teach: ")
        com = input("Input the new list of commands: ")
        db.query("""UPDATE pets.mansfriends SET commands = '%s' where (idmansfriends = %s)""" % (com, i))
    elif (inp == 5):
        isRunning = False
    else:
        a = input("Incorrect input. Press Enter to continue\n")
    
        