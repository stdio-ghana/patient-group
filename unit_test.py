# check patients details

'''
test cases
    enter id
        if available :
            display "PATIENT DETAILS"
        else:
            display data not available
'''
id_list = [1,2,3,4,5]

# retrieve patients details
def retrieve_patient_detail():
    return "DISPLAY PATIENT DETAILS"

def check_patient(id):
    if id in id_list:
        return retrieve_patient_detail()
    else:
        return"DATA NOT AVAILABLE PLEASE GIVE YOUR DETAILS"

def test_check_patient_pass():
    assert check_patient(4) == "DISPLAY PATIENT DETAILS"

test_check_patient_pass()

def test_check_patient_fail():
    assert check_patient(7) == "DATA NOT AVAILABLE PLEASE GIVE YOUR DETAILS"

test_check_patient_fail()




# if new patient register patient detail
newPatient= []
def register_patient_detail(detail):
    newPatient.append(detail)
    return newPatient


'''
name
medical history
vitals
'''
patient_details= {}
