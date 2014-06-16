import random

class Patient:

    user = []
    id= 0

    def __init__(self):
        pass


    def autoId(self):
        global id
        startId = 1
        idInterval = 1
        if(id == 0):
            id = startId
        else:
            id = id + idInterval
        return id

    def registerPatient(self, name, age, nextOfkin, contact):
        self.id = Patient
        self.name = name
        self.age = age
        self.nextOfkin = nextOfkin
        self.contact = contact
        Patient.user.append({'id':id(self.id),'name':self.name,'age':self.age,'nextOfkin':self.nextOfkin,"contact":self.contact})




class Person(Patient):


    def searchPersonByName(self,name):
        self.name = name
        search_status = 0
        for i in range(len(Patient.user)):
            if self.name in Patient.user[i]["name"]:
                print("%d %s %d %s %s" %(Patient.user[i]["id"],Patient.user[i]["name"],Patient.user[i]["age"],Patient.user[i]["contact"],Patient.user[i]["nextOfkin"]))
                search_status = 1
            if search_status == 0 and i == len(Patient.user)-1:
                print("Not Found")

    def searchPersonById(self, id):
        self.id = id
        search_status = 0
        for i in range(len(Patient.user)):
            if self.name in Patient.user[i]["name"]:
                print(" %s %d %s %s" %(Patient.user[i]["name"],Patient.user[i]["age"],Patient.user[i]["contact"],Patient.user[i]["nextOfkin"]))
                search_status = 1
            if search_status == 0 and i == len(Patient.user)-1:
                print("Not Found")

    def displayPatient(self):
        for i in range(len(Patient.user)):
             print(" %s %d %s %s" %(Patient.user[i]["name"],Patient.user[i]["age"],Patient.user[i]["contact"],Patient.user[i]["nextOfkin"]))




ptn1 = Person()




ptn1.registerPatient("steve andoh",22,"Stephanie Andoh","0241443624")
ptn1.registerPatient("Michael Okorie",16,"Richard Obiri","0202552663")
ptn1.registerPatient("Michael Okyere",16,"Richard Obiri","0202552663")

#ptn1.displayPatient()

ptn1.searchPersonByName("Michael")


