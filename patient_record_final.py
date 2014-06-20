import csv

"""
patient record app
it can :
    register new Patient
    search patient;
        By Id
        By Name
data are stored into a csv file

"""

#Class Patient register patient
class Patient:

    user = []

    F = open('datafile.txt')
    line = F.readline()
    F.close()

    def __init__(self):
        pass

    def registerPatient(self, name, age, contact):
        self.id = int(self.line)
        self.id = str(self.id + 1)
        self.name = name
        self.age = age
        self.contact = contact
        f = open('patient.csv', 'a', newline='')
        writer = csv.writer(f)
        writer.writerow((self.id,self.name,self.age,self.contact))
        f.close()
        k = open('datafile.txt', 'w')
        k.write(self.id)
        k.close()




#Class person inherit form Patient contain method searchPersonByName and searchPersonById
class Person(Patient):


    def searchPersonByName(self,name):
        self.name = name
        g = open('patient.csv','rt')
        reader = csv.reader(g,delimiter=',')
        test = ""
        test1 = ''
        for i in reader:

            if self.name == i[1]:
                test1 = "found"
                print(i)


            else:
                test = "Not Found"
        if test1 != "found":
            print(test)
        g.close()

    def searchPersonById(self, idx):
        self.idx = idx
        g = open('patient.csv','rt')
        reader = csv.reader(g,delimiter=',')
        test = ""
        test1 = ''
        for i in reader:

            if self.idx == i[0]:
                test1 = "found"
                print(i)


            else:
                test = "Not Found"
        if test1 != "found":
            print(test)
        g.close()

    def displayPatient(self):print(open('patient.csv', 'r').read())

ptn1 = Person()

# Function use to add a new patient to the database
def add_new_patient():

    mydetail = []
    for end in range(3):
                while True:

                    if end == 0:
                        try:
                            user_input = input("Enter your name: ")
                            if user_input =="":
                                print ("please enter a valid name")
                            else:
                                mydetail.append(user_input)
                            break

                        except ValueError:
                            print("Oops!  That was no valid age.  Try again...")

                    if end == 1:
                        try:
                            user_input= int(input("Please enter age: "))
                            mydetail.append(user_input)
                            break
                        except ValueError:
                            print ("Oops!  That was no valid age.  Try again...")

                    if end == 2:
                        try:
                            user_input= int(input("Enter your phone number: "))
                            mydetail.append(user_input)
                            break
                        except ValueError:
                            print("Oops!  That was no valid number.  Try again...")

    ptn1.registerPatient(mydetail[0],mydetail[1],mydetail[2])


    ptn1.displayPatient()

ptn1.searchPersonByName("solo")

#ptn1.searchPersonById("1000")


# Display the possible options available in the app
def menu_option():
    ans=True
    while ans:
        print ("""
        1.Register a patient
        2.Search for a patient by id
        3.Search for a patient by name
        4.Exit/Quit
        """)
        ans=input("What would you like to do? " )
        if ans=="1":
             add_new_patient()

        elif ans=="2":
            ans=input("Please enter an id " )

            ptn1.searchPersonById(ans)

        elif ans=="3":
          ans=input("Please enter a name " )

          ptn1.searchPersonByName(ans)
        elif ans=="4":
          print("\n Goodbye")
        elif ans !="":
          print("\n Not Valid Choice Try again")


menu_option()
