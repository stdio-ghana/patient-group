def patient_registration( ):

    mydetail = []
    for end in range(3):
        while True:

            if end == 0:
                 try:
                     user_input = raw_input("Enter your name: ") # raw_input in Python 2.x
                     if user_input =="":
                         print "please enter a valid name"
                     break

                 except ValueError:
                     print"Oops!  That was no valid age.  Try again..."

            if end == 1:
                try:
                    user_input= int(raw_input("Please enter age: "))
                    break
                except ValueError:
                    print "Oops!  That was no valid age.  Try again..."

            if end ==2:
                try:
                    user_input= int(raw_input("Enter your phone number: "))
                    break
                except ValueError:
                    print "Oops!  That was no valid age.  Try again..."
        mydetail.append(user_input)

    print mydetail


trial()
