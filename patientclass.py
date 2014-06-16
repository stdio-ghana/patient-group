class Patient:

    user = []

    def __init__(self, name, age, nextOfkin, contact):
        self.name = name
        self.age = age
        self.nextOfkin = nextOfkin
        self.contact = contact
        Patient.user.append({'name':self.name,'age':self.age,'nextOfkin':self.nextOfkin,"contact":self.contact})


    def displayPatient(self):
        print("Total Patient Record ",  Patient.user)



class Person(Patient):


    def searchPerson(self,name):
        self.name = name
        for i in range(len(Patient.user)):
            if self.name in Patient.user[i]["name"]:
                print (" %s %d %s %s" %(Patient.user[i]["name"],Patient.user[i]["age"],Patient.user[i]["contact"],Patient.user[i]["nextOfkin"]))


            else:
                print("Not Found")


    def displayPatient(self):
        for i in range(len(Patient.user)):
             print(" %s %d %s %s" %(Patient.user[i]["name"],Patient.user[i]["age"],Patient.user[i]["contact"],Patient.user[i]["nextOfkin"]))






ptn1 = Person("steve andoh",22,"Stephanie Andoh","0241443624")
ptn2 = Person("stone andoh",21,"Richard Obiri","0202552663")

#ptn1.displayPatient()

ptn1.searchPerson("andoh")

