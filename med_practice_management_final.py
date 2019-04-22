from sys import exit
from pandas import DataFrame
from datetime import datetime

class Provider():
    """ Base class for medical providers """
    
    def __init__(self, first, last):
        """ Initialize with provider name """
        self.first = first.capitalize()
        self.last = last.capitalize()

    def __repr__(self):
        """ Representation of Provider """
        return self.first + ' ' + self.last

    
class Doctor(Provider):
    """ 
    Subclass of Provider 
    Takes in basic demographic information about the doctor
    """
    # can potentially have a list or dict of specialities for checking in scaled up program version

    def __init__(self, first, last, lic_number, specialty):
        """ Initialize with additional information """
        Provider.__init__(self, first, last)
        self.lic_number = lic_number
        self.specialty = specialty

    def __repr__(self):
        """ Representation of Doctor """
        return self.first + ' ' + self.last + ", MD"

    
class Nurse(Provider):
    """ 
    Subclass of Provider 
    Takes in basic demographic information about the nurse
    """
    # This class looks similar to Doctor, but in larger scale program, 
    # there will be differences in provider info and methods

    def __init__(self, first, last, lic_number, specialty):
        """ Initialize with additional information """
        Provider.__init__(self, first, last)
        self.lic_number = lic_number
        self.specialty = specialty

    def __repr__(self):
        """ Representation of Doctor """
        return self.first + ' ' + self.last + ", RN"

    
class Patient():
    """
    Takes in demographic info on the patient
    Generates unique medical record number (MRN) in the system for tracking
    """
    # used to generate a MRN for patients
    start_mrn = 1000
    gender_code = ['M', 'F', 'O']

    def __init__(self, first, last, gender, dob):
        self.first = first.capitalize() 
        self.last = last.capitalize()
        if gender.upper()[0] in Patient.gender_code:
            self.gender = gender.upper()[0]
        else:
            raise Exception("Invalid gender code.")
        self.dob = dob
        self.mrn = Patient.start_mrn + 1
        Patient.start_mrn += 1

    def __repr__(self):
        """ Representation of Patient """
        return ('{} {}, MRN: {}').format(self.first, self.last, self.mrn)
    
    def get_pat_info(self):
        """ Returns a list of inputted demographic info """
        pat_info = [self.mrn, self.first, self.last, self.gender, self.dob]
        return pat_info


class Schedule():
    """
    Takes in a Provider object and creates Mon - Fri, 9 am - 5 pm schedule for them.
    Appointments are in 30 minute blocks, denoted by the time at the start of the appointment.    
    """
    # class attributes for error checking
    day_dict = {2:'Monday', 3:'Tuesday', 4:'Wednesday', 5:'Thursday', 6:'Friday'}
    time_list = ['09:00 AM', '09:30 AM', '10:00 AM', '10:30 AM', '11:00 AM', '11:30 AM', '12:00 PM',
                '12:30 PM', '01:00 PM', '01:30 PM', '02:00 PM', '02:30 PM', '03:00 PM', '03:30 PM',
                 '04:00 PM', '04:30 PM']

    def __init__(self, provider):
        # provider as a provider object (either doctor or nurse)
        self.provider = provider
        self.__schedule = {'Monday':{'09:00 AM':['patient', 'appt_type'], '09:30 AM': ['patient', 'appt_type'],
                 '10:00 AM':['patient', 'appt_type'], '10:30 AM':['patient', 'appt_type'],
                  '11:00 AM':['patient', 'appt_type'], '11:30 AM':['patient', 'appt_type'],
                  '12:00 PM':['patient', 'appt_type'], '12:30 PM':['patient', 'appt_type'],
                 '01:00 PM':['patient', 'appt_type'], '01:30 PM':['patient', 'appt_type'],
                  '02:00 PM':['patient', 'appt_type'], '02:30 PM':['patient', 'appt_type'],
                  '03:00 PM':['patient', 'appt_type'], '03:30 PM':['patient', 'appt_type'],
                 '04:00 PM':['patient', 'appt_type'], '04:30 PM':['patient', 'appt_type']},
        'Tuesday':{'09:00 AM':['patient', 'appt_type'], '09:30 AM': ['patient', 'appt_type'],
                 '10:00 AM':['patient', 'appt_type'], '10:30 AM':['patient', 'appt_type'],
                  '11:00 AM':['patient', 'appt_type'], '11:30 AM':['patient', 'appt_type'],
                  '12:00 PM':['patient', 'appt_type'], '12:30 PM':['patient', 'appt_type'],
                 '01:00 PM':['patient', 'appt_type'], '01:30 PM':['patient', 'appt_type'],
                  '02:00 PM':['patient', 'appt_type'], '02:30 PM':['patient', 'appt_type'],
                  '03:00 PM':['patient', 'appt_type'], '03:30 PM':['patient', 'appt_type'],
                 '04:00 PM':['patient', 'appt_type'], '04:30 PM':['patient', 'appt_type']},
        'Wednesday':{'09:00 AM':['patient', 'appt_type'], '09:30 AM': ['patient', 'appt_type'],
                 '10:00 AM':['patient', 'appt_type'], '10:30 AM':['patient', 'appt_type'],
                  '11:00 AM':['patient', 'appt_type'], '11:30 AM':['patient', 'appt_type'],
                  '12:00 PM':['patient', 'appt_type'], '12:30 PM':['patient', 'appt_type'],
                 '01:00 PM':['patient', 'appt_type'], '01:30 PM':['patient', 'appt_type'],
                  '02:00 PM':['patient', 'appt_type'], '02:30 PM':['patient', 'appt_type'],
                  '03:00 PM':['patient', 'appt_type'], '03:30 PM':['patient', 'appt_type'],
                 '04:00 PM':['patient', 'appt_type'], '04:30 PM':['patient', 'appt_type']},
        'Thursday':{'09:00 AM':['patient', 'appt_type'], '09:30 AM': ['patient', 'appt_type'],
                 '10:00 AM':['patient', 'appt_type'], '10:30 AM':['patient', 'appt_type'],
                  '11:00 AM':['patient', 'appt_type'], '11:30 AM':['patient', 'appt_type'],
                  '12:00 PM':['patient', 'appt_type'], '12:30 PM':['patient', 'appt_type'],
                 '01:00 PM':['patient', 'appt_type'], '01:30 PM':['patient', 'appt_type'],
                  '02:00 PM':['patient', 'appt_type'], '02:30 PM':['patient', 'appt_type'],
                  '03:00 PM':['patient', 'appt_type'], '03:30 PM':['patient', 'appt_type'],
                 '04:00 PM':['patient', 'appt_type'], '04:30 PM':['patient', 'appt_type']},
        'Friday':{'09:00 AM':['patient', 'appt_type'], '09:30 AM': ['patient', 'appt_type'],
                 '10:00 AM':['patient', 'appt_type'], '10:30 AM':['patient', 'appt_type'],
                  '11:00 AM':['patient', 'appt_type'], '11:30 AM':['patient', 'appt_type'],
                  '12:00 PM':['patient', 'appt_type'], '12:30 PM':['patient', 'appt_type'],
                 '01:00 PM':['patient', 'appt_type'], '01:30 PM':['patient', 'appt_type'],
                  '02:00 PM':['patient', 'appt_type'], '02:30 PM':['patient', 'appt_type'],
                  '03:00 PM':['patient', 'appt_type'], '03:30 PM':['patient', 'appt_type'],
                 '04:00 PM':['patient', 'appt_type'], '04:30 PM':['patient', 'appt_type']}}
    
    def __repr__(self):
        return "{}'s schedule".format(self.provider)

    ##### DAY will be entered as an int (see day_dict) and converted into named string
    ##### TIME SLOT will be entered as HH:MM PM/AM (checked against time_list)
    def is_available(self, day, time_slot):
        """ Returns true if a time_slot is available for booking for specified day"""
        
        convert_day = ''

        if day in Schedule.day_dict.keys():
            convert_day = Schedule.day_dict[day]
        else:
            raise Exception("Please enter a valid integer that corresponds with a weekday.")

        return self.__schedule[convert_day][time_slot] == ['patient', 'appt_type']

    def pull_avail(self, day):
        """ Returns the available time slots as tuples for specified day in a list"""
        
        convert_day = ''
        avail_appts = []

        if day in Schedule.day_dict.keys():
            convert_day = Schedule.day_dict[day]
        else:
            raise Exception("Please enter a valid integer that corresponds with a weekday.")

        for slot in self.__schedule[convert_day]:
            if self.is_available(day, slot):
                avail_appts.append((convert_day, slot))

        return avail_appts

    def book_appt(self, day, time_slot , mrn, appt_type):
        """ Book a time slot for a patient via MRN and appointment type """

        convert_day = ''
        if day in Schedule.day_dict.keys():
            convert_day = Schedule.day_dict[day]
        else:
            raise Exception("Please enter a valid integer that corresponds with a weekday.")
        
        if time_slot in Schedule.time_list:
            if self.is_available(day, time_slot):
                self.__schedule[convert_day][time_slot][0] = mrn
                self.__schedule[convert_day][time_slot][1] = appt_type
                print("{} appointment booked for MRN# {}!".format(appt_type, mrn))
            else:
                raise Exception("That time slot is not available for that day.")
        else:
            raise Exception("Not a valid time slot. Please enter appointment times in HH:MM AM/PM format.")
 
    def get_appt_mrn(self, mrn):
        """ Takes MRN as input returns a list of appts associated with MRN as tuples"""
        # not used in the Menu class currently
        appts = []
        
        for day in self.__schedule:
            for time in schedule[day]:
                if schedule[day][time][0] == mrn:
                    appts.append((day, time))
                    
        return appts

    def cancel_appt(self, day, time_slot):
        """ Cancel an appointment by specifying day and time slot """

        convert_day = ''

        if day in Schedule.day_dict.keys():
            convert_day = Schedule.day_dict[day]
        else:
            raise Exception("Please enter number the corresponds with a day!")
        
        if time_slot in Schedule.time_list:
            # checks there there's an actual appointment and that it's not blocked
            if self.is_available(day, time_slot):
                print("There's no appointment in that slot. Try again.")
            elif (self._Schedule__schedule[convert_day][time_slot] != ['patient', 'appt_type'] 
                and self.__schedule[convert_day][time_slot] != ['BLOCKED', 'BLOCKED']):
                self.__schedule[convert_day][time_slot][0] = 'patient'
                self.__schedule[convert_day][time_slot][1] = 'appt_type'
                
                print("Appointment canceled for {} at {}.".format(convert_day, time_slot))
        else:
            raise Exception("Not a valid time slot. Please enter appointment times in HH:MM AM/PM format.")

    def block_schedule(self, day, time_slot):
        """ Blocks off a particular day and time block on the schedule """

        convert_day = ''

        if day in Schedule.day_dict.keys():
            convert_day = Schedule.day_dict[day]
        else:
            raise Exception("Please enter number the corresponds with a day!")
                                
        if time_slot in Schedule.time_list:
            # checks to see if there's already an appt or block there. If so, it will not block.
            if self.is_available(day, time_slot):                    
                self.__schedule[convert_day][time_slot][0] = 'BLOCKED'
                self.__schedule[convert_day][time_slot][1] = 'BLOCKED'

                print("{} at {} has been blocked.".format(convert_day, time_slot))
            else:
                raise Exception("This slot has an appointment or is already blocked. Cancel and rebook the appointment to block.")        
        else:
            raise Exception("Not a valid time slot. Please enter appointment times in HH:MM AM/PM format.")

    def print_schedule(self, print_type = 'all'):
        """ 
        Prints either the weekly or daily schedule. 
        The default is weekly, but can pull daily schedule by inputting int from day_dict. 
        """
        
        print("This is {}'s schedule:".format(self.provider))
        
        if print_type == 'all':
            weekday = [day for day in self.__schedule]
            times = Schedule.time_list
            data = []
            # puts all the appt data into lists for the DataFrame
            for day in self.__schedule:
                day_data = []
                for time in self.__schedule[day]:

                    if self.__schedule[day][time] == ['patient', 'appt_type']:
                        day_data.append("OPEN")
                    elif self.__schedule[day][time] == ['BLOCKED', 'BLOCKED']:
                        day_data.append("BLOCKED")
                    else:
                        day_data.append("MRN: " + str(self.__schedule[day][time][0]) + " " + self.__schedule[day][time][1])
                data.append(day_data)
            # to print the week, we need to flip the data into rows of 16 (time_slot) instead of rows of 5 (days)
            flip_data = []

            for i in range(16):
                row_data = []
                for item in data:
                    row_data.append(item[i])
                flip_data.append(row_data)

            return DataFrame(flip_data, times, weekday)
                                
        elif print_type in Schedule.day_dict.keys():
            print_day = Schedule.day_dict[print_type]
            weekday = [day for day in self.__schedule if day == print_day]
            times = Schedule.time_list
            data = []

            for day in self.__schedule:
                if day == print_day:
                    for time in self.__schedule[day]:
                        if self.__schedule[day][time] == ['patient', 'appt_type']:
                            data.append("OPEN")
                        elif self.__schedule[day][time] == ['BLOCKED', 'BLOCKED']:
                            data.append("BLOCKED")
                        else:
                            data.append("MRN: " + str(self.__schedule[day][time][0]) + " " + self.__schedule[day][time][1])
            return DataFrame(data, times, weekday)
        else:
            raise Exception("Invalid input. Print either the weekly or daily schedule.")

            
class Menu():
    """
    Med Practice Management is operated through the Menu class. Has methods that utilize the Provider, 
    Patient, and Schedule objects that guide the user through setup and using the system. 
    Schedule and Patient objects are stored in class dictionaries after creation for later use.
    """
    schedules = {}
    patients = {}
    
    def __init__(self):
        """ Creates dict of the user methods """
        self.options = {
        "1":self.create_schedule,
        "2":self.create_patient,
        "3":self.patient_list,
        "4":self.prov_avail,
        "5":self.view_schedule,
        "6":self.book_appt,
        "7":self.cancel_appt,
        "8":self.block_appt,
        "9":self.quit
        }

    def display_menu(self):
        print(""" 
 __  __          _   ____                 _   _            __  __                                                   _   
|  \/  | ___  __| | |  _ \ _ __ __ _  ___| |_(_) ___ ___  |  \/  | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_ 
| |\/| |/ _ \/ _` | | |_) | '__/ _` |/ __| __| |/ __/ _ \ | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|
| |  | |  __/ (_| | |  __/| | | (_| | (__| |_| | (_|  __/ | |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_ 
|_|  |_|\___|\__,_| |_|   |_|  \__,_|\___|\__|_|\___\___| |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|
                                                                                     |___/                               
        """)
        
        print("""
        Welcome to Med Practice Management--just what you need to have your medical office running smoothly! This system 
        will help you set up provider schedules, view schedules, maintain and modify schedules, and input patient information.
        
        Just getting started? First, select 1 or 2 to create a schedule or patient.
        
        1. Create a schedule for a provider
        2. Create a new patient
        3. Get list of all patients
        4. Get provider schedule availability
        5. View a schedule
        6. Book an appointment
        7. Cancel an appointment
        8. Block a time slot on a schedule
        9. Quit program
        """)

    def run(self):
        """ 
        Loops through the menu until the user quits. Calls Menu methods based on the options the user inputs.
        Users must create at least one schedule and patient before performing other actions.
        """
        while True:
            self.display_menu()
            option = input("Please select an option from the menu: ")
            action = self.options.get(option)
            if option in ['1', '2', '9']:
                action()     
            elif option in [str(num) for num in range(3, 9)] and len(Menu.schedules) > 0 and len(Menu.patients) > 0:
                action()
            elif len(Menu.schedules) == 0 or len(Menu.patients) == 0:
                print("Can't perform that operation until you create at least one schedule and one patient!")
            else:
                print("Not a valid option from the menu. Try again.")

    def create_schedule(self):
        """ 
        Takes user input to create a Provider and Schedule object. 
        Stores the provider and schedule object as key-value pairs in schedules dict
        """       
        print("Let's create a schedule for a provider. Follow the prompts below.")
        
        while True:
            provider_type = input("What kind of provider? Enter the corresponding number. 1) Doctor 2) Nurse ")
            if provider_type == "1":
                first = input("What is their first name? ")
                last = input("What is their last name? ")
                # currently no restrictions or error checking on license or specialty, 
                # but can be added in future iterations of program
                license = input("What is their license? ")
                specialty = input("What is their specialty? ")
                
                doctor = Doctor(first, last, license, specialty)
                doctor_schedule = Schedule(doctor)
                
                Menu.schedules[doctor] = doctor_schedule
                
                print("{}'s schedule has successfully been created.".format(doctor))
                print("Taking you back to the main menu...")
                break
                
            elif provider_type == "2":
                first = input("What is their first name? ")
                last = input("What is their last name? ")
                # currently no restrictions or error checking on license or specialty, 
                # but can be added in future iterations of program
                license = input("What is their license? ")
                specialty = input("What is their specialty? ")
                
                nurse = Nurse(first, last, license, specialty)
                nurse_schedule = Schedule(nurse)
                
                Menu.schedules[nurse] = nurse_schedule
                print("{}'s schedule has successfully been created.".format(nurse))
                print("Taking you back to the main menu...")
                break
                
            else:
                print("Not a valid option. Try again.")

    def create_patient(self):
        """ 
        Takes user input tto create Patient object. 
        Stores Patient MRN and Patient object in patients dict
        """
        while True:
            print("To create a patient, you'll need to enter demographic information...")

            first = input("What is the patient's first name? ")
            last = input("What is the patient's last name? ")
            gender = input("What is the patient's gender? F) Female M) Male O) Other ").upper()
            # checks for valid birthdate
            while True:
                try:
                    dob = input("What is the patient's date of birth (DOB)? Please enter in MM/DD/YYYY ")
                    temp = datetime.strptime(dob, '%m/%d/%Y')
                    break
                except ValueError:
                    print("Not a valid date. Try again.")
            try:
                patient = Patient(first, last, gender, dob)
                Menu.patients[patient.mrn] = patient
                print("Patient was successfully created in the system. MRN is:", patient.mrn)
                print("Taking you back to the main menu...")
                break
            except Exception as e:
                print("Error:" + str(e))
            
      
    def make_dict_options(self, a_dict):
        """ 
        Creates another dictionary with a number key and the value is the key of the inputted dictionary 
        (either Menu.schedules or Menu.patients in current program)                
        """
        # polymorphism? doesn't care if it's a schedule or patient dict
        options_dict = {}
        
        i = 1

        for key in a_dict:
            options_dict[str(i)] = key
            i += 1
        
        return options_dict
    
    def print_dict_options(self, a_dict):
        # polymorphism? doesn't care if it's a schedule or patient dict
        """ 
        Takes in a dictionary and prints the options in a string. Used to help the user 
        select options for schedules and patients.
        """             
        for num, key in a_dict.items():
            print(str(num) + ") " + str(key))
        
    def patient_list(self):
        """ 
        Prints a table of patient information by looping through patients dict 
        and calling get_pat_info method to get lists of the demo info
        """
        
        print("These patients are in the system: ")
        print("(Hint: patient MRNs are required for appointment booking.)")
        
        pat_data = []
        header = ['MRN', 'First Name', 'Last Name', 'Gender', 'DOB']
        number = [num for num in range(1, len(Menu.patients) + 1)]
                                
        for pat in Menu.patients.values():
            pat_data.append(pat.get_pat_info())
        
        print(DataFrame(pat_data, number, header))
                                                                                  
    def view_schedule(self):
        """ Takes user input to show a provider's weekly or daily schedule using Schedule methods """
               
        while True:
            
            while True:
                schedule_dict = self.make_dict_options(Menu.schedules)
        
                print("These schedules are in the system: ")
                self.print_dict_options(schedule_dict)
                
                select_provider = input("Whose schedule would you like to view? Please input a number only. ")
            
                if select_provider in schedule_dict.keys():
                    break
                else:
                    print("Not a valid option.")
            while True:
                schedule_type = input("What kind of schedule? Please input a number only. 1) Weekly 2) Daily ")
                
                if schedule_type in ["1", "2"]:
                    break
                else:
                    print("Not a valid option.")
            
            convert_provider = schedule_dict[select_provider]
            
            if schedule_type == "1":
                print(Menu.schedules[convert_provider].print_schedule())
                break
            elif schedule_type == "2":
                while True:
                    daily = input("What day would you like to view? 2) Monday 3) Tuesday 4) Wednesday 5) Thursday 6) Friday ")
                    
                    if daily in ['2', '3', '4', '5', '6']:
                        print(Menu.schedules[convert_provider].print_schedule(int(daily)))
                        break
                    else:
                        print("Not a valid option")
                break
                
    def prov_avail(self):
        """ Takes user input to print a list of available time slots on specified day for specified provider """
        
        print(""" 
        Let's see what time slots are available for a certain provider. Follow the prompts to get a provider's availability.
        """)
        
        while True:
            
            while True:              
                schedule_dict = self.make_dict_options(Menu.schedules)
        
                print("These schedules are in the system: ")
                self.print_dict_options(schedule_dict)
                
                select_provider = input("Whose availability do you want to check? Please input a number only. ")
            
                if select_provider in schedule_dict.keys():
                    break
                else:
                    print("Not a valid option.")
            
            convert_provider = schedule_dict[select_provider]
            
            while True:
                day = input("Which day do you want to check? 2) Monday 3) Tuesday 4) Wednesday 5) Thursday 6) Friday ")
                
                try:
                    avail = Menu.schedules[convert_provider].pull_avail(int(day))
                    print("{} is available for the following time slots:".format(convert_provider))
                                       
                    for appt in avail:
                        print(appt)
                    break
                except Exception as e:
                    print("Try again. Error:" + str(e))
            break
        
    def book_appt(self):
        """ Takes user input to book an appointment via Schedule method """
        
        print("""
        Let's book an appointment...Med Practice Management schedules are Monday - Friday, 09:00 AM - 05:00 PM. 
        Appointments are 30 mins each and defined by the start time. Follow the prompts to book an appointment.
        """)
        book_status = True
        
          
        while book_status:
            sched_status = True
            mrn_status = True
            pass_status = True
            
            while sched_status:                
                schedule_dict = self.make_dict_options(Menu.schedules)
        
                print("These schedules are in the system: ")
                self.print_dict_options(schedule_dict)
                
                provider = input("\nWhich provider is the appointment for? Please enter the number only. ")
            
                if provider in schedule_dict.keys():
                    day = int(input("Enter appointment day via number: 2) Monday 3) Tuesday 4) Wednesday 5) Thursday 6) Friday "))
                    time = input("Enter appointment time in HH:MM AM/PM format. (Examples: 09:30 AM or 12:00 PM) ")
                    sched_status = False
                    mrn_status = True
                    pass_status = True
                else:
                    print("Not a valid option. Try again.")          
            
            while mrn_status:
                mrn = input("Enter the patient's MRN: ")
                if int(mrn) in Menu.patients.keys():
                    mrn_status = False
                    pass_status = True
                else:
                    print("Not a valid MRN. If you're not sure of the MRN, look up the patient list.")
                    response = input("Do you want to go back to the menu to get the patient list? Y/N ")
                    if response.upper() == "Y":
                        self.run()
                    else:
                        print("\nOkay, let's try booking again.")
                        mrn_status = False
                        sched_status = True
                        pass_status = False
                        
            while pass_status:        
                appt_type = input("Enter appointment type such as Sick Visit, Physical Exam, Labwork: ")
            
                convert_provider = schedule_dict[provider]
                try:
                    Menu.schedules[convert_provider].book_appt(day, time.upper(), mrn, appt_type)
                    pass_status = False
                    book_status = False
                except Exception as e:
                    print("Couldn't book appointment. Error: " + str(e))
                    pass_status = False
                    
        
    def cancel_appt(self):
        """ Takes user input to cancel an appointment via Schedule method """

        print("Follow the prompts to cancel an appointment.")
        
        while True:
            
            while True:
                schedule_dict = self.make_dict_options(Menu.schedules)
        
                print("These schedules are in the system: ")
                self.print_dict_options(schedule_dict)
                provider = input("\nWhich provider are you canceling for? Please enter the number only. ")
            
                if provider in schedule_dict.keys():
                    break
                else:
                    print("Not a valid option. Try again.")
            
            day = int(input("Enter appointment day via number: 2) Monday 3) Tuesday 4) Wednesday 5) Thursday 6) Friday "))
            time = input("Enter appointment time in HH:MM AM/PM format. (Examples: 09:30 AM or 12:00 PM) ")
            
            convert_provider = schedule_dict[provider]
            
            try: 
                Menu.schedules[convert_provider].cancel_appt(day, time.upper())
                
                response = input("Would you like to rebook an appointment for this patient? Y/N ")
                
                if response.upper() == "Y":
                    self.book_appt()
                    break
                else:
                    print("\nTaking you back to the main menu...")
                    break               
            except Exception as e:
                print("\nCouldn't cancel appointment. Error: " + str(e))
                       

    def block_appt(self):
        """ Takes user input to block a time slot on schedule via Schedule method """
        print("""
        Let's block off a time slot...
        Med Practice Management schedules are Monday - Friday, 09:00 AM - 05:00 PM. 
        Time slots are 30 mins each and defined by the start time. Follow the prompts to block a time slot.
        """)
        
        while True:
            
            while True:
                
                schedule_dict = self.make_dict_options(Menu.schedules)
        
                print("These schedules are in the system: ")
                self.print_dict_options(schedule_dict)
                
                print("\nYou can block off one time slot at a time.")
                provider = input("Which provider are blocking off for? Please enter the number only. ")
            
                if provider in schedule_dict.keys():
                    break
                else:
                    print("Not a valid option. Try again.")
                    
            day = int(input("Enter day to block off via number: 2) Monday 3) Tuesday 4) Wednesday 5) Thursday 6) Friday "))
            time = input("Enter time slot in HH:MM AM/PM format. (Examples: 09:30 AM or 12:00 PM) ")
            
            convert_provider = schedule_dict[provider]
            
            try:
                Menu.schedules[convert_provider].block_schedule(day, time.upper())
                break
            except Exception as e:
                print("Couldn't block time slot. Error: " + str(e))

    
    def quit(self):
        print("Thank you for using Med Practice Management!")
        exit(0)

##### running the program
test_menu = Menu()
test_menu.run()