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



Requirement Analysis
	* Ability to clearly identify a user (ID card/Hospital Card/Known Witness/Biometric Method)
	* Easy ways of searching or querying the database
	* Reducing the queues in the waiting room
	* Multiple Simultaneous access to patient records (Nurses being able to attend to more patients at the same time)
	* Make registration based on identification criterias
	* Special case (buffer) registration for emergency cases for later review and comitting to the patient records
	* Patient record retrieval based on Identification criteria
---------------------------------------------------------------------------
Functional Requirements:
	* Setting up unique criteria for patient identification
	* facilitate access to records for verification and retrieval
	* Facilitating patient registration
---------------------------------------------------------------------------
Non functional requirements:
	* Ease of use of the system
	* Incorporating HCI concepts to facilitate nurse interaction with the system
	* Ability for multiple simultaneous record access
	* Speed of the system 
	* Access Control -> Different Levels of access and priviledges
	* Security - Records should not be altered by unauthorized personnel
---------------------------------------------------------------------------
Use cases: Actor -> Nurse
	* Identify Patient
	* Verify Patient
	* Register Patient
	* Retrieve Patient Record
