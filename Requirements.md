The major steps that take place when a patient enters a hospital are:
    
    1. Patient Identification
    2. Patient record Verification
    3. If patient exist, retrieve patient file else, Register new patient
    4. Checks for vitals (Temperature, weight, etc...)
    5. Doctor Consultation for diagnosis and prescription
    6. Drugs + consultation fee payment
    7. Exit

The focus of the following requirement analysis was based on the first three phases, which are: Patient Identification, 
Patient record verification and retrieval or patient records, or the creation of a new patient record (Registration).

Requirement Analysis:
    1. Ability to clearly identify a user (ID card/Hospital Card/Known Witness/Biometric Method)
    2. Easy ways of searching or querying the database
    3. Reducing the queues in the waiting room
    4. Multiple Simultaneous access to patient records (Nurses being able to attend to more patients at the same time)
    5. Make registration based on identification criterias
    6. Special case (buffer) registration for emergency cases for later review and comitting to the patient records
    7. Patient record retrieval based on Identification criteria

Functional Requirements:
    1. Setting up unique criteria for patient identification
    2. facilitate access to records for verification and retrieval
    3. Facilitating patient registration

Non functional requirements:
    1. Ease of use of the system
    2. Incorporating HCI concepts to facilitate nurse interaction with the system
    3. Ability for multiple simultaneous record access
    4. Speed of the system 
    5. Access Control -> Different Levels of access and priviledges
    6. Security -> Records should not be altered by unauthorized personnel

Use cases: Actor -> Nurse
    1. Identify Patient
    2. Verify Patient
    3. Register Patient
    4. Retrieve Patient Record
