import os
import csv
import docx


def add_application(position, employer, phone_number, date_applied):

    os.chdir(os.getcwd() + '\job applications')
    if not os.path.exists(os.getcwd() + '\\' + employer):
        print("Adding employer folder for: " + employer)
        os.mkdir(employer)
    os.chdir(os.getcwd() + '\\' + employer)
    
    cv_file_name = 'CV, ' + position + ', ' + employer + '.docx'
    #Checks if the position document already exists.
    if not os.path.isfile(os.getcwd() + '\\' + cv_file_name):
        print('Creating new CV document.')
        cv = docx.Document()
        cv.save(cv_file_name)
    
    #This returns the CWD to the home directory of the program once the additions are made.
    os.chdir(file_path)

    #Checks to see if jobs_applied csv is present and creates one if not.
    if not os.path.isfile(os.getcwd() + "\\jobs_applied.csv"):
        print("Creating new jobs applied csv.")
        with open('jobs_applied.csv', 'w', newline="") as file:
            writer = csv.DictWriter(file, header_names)
            writer.writeheader()
    try:
        with open('jobs_applied.csv', 'a', newline="") as csv_file:
            writer = csv.DictWriter(csv_file, header_names)
            writer.writerow({"Jobs": position, 'Employer': employer, 'Phone Number': phone_number, 'Date': date_applied, 'Contacted?': None, 'Interview?': None, 'Offer?': None})
    except PermissionError:
        print('You must close the excel file before adding a new entry!\n')

#Boolean for program continuation in a while loop.
cont_program = True
file_path = os.path.dirname(__file__)
print(file_path)
os.chdir(file_path)
header_names = ["Jobs", 'Employer', 'Phone Number', 'Date', 'Contacted?', 'Interview?', 'Offer?']

#Checks if job applications folder is present
if not os.path.exists(os.getcwd() + "\job applications"):
    print('Creating "Job Applications" folder.')
    os.mkdir('job applications')

#Checks if resumes folder is present
if not os.path.exists(os.getcwd() + '\\resumes'):
    print('Creating "Resumes" folder.')
    os.mkdir('resumes')


#Main body of the UX
while cont_program == True:
    user_in = input("What would you like to do?\n[A] Add Application\n[B] View Job Applications Folder\n[C] View Resume Folder\n[D] View Application Spreadsheet\n[X] Exit Program\n>>> ")
    

    if user_in.lower() == 'a':
        print('\nAny information which you do not have can be entered manually by entering "D" in the main menu.')
        print("Ensure that Excel is closed before entering a new application!\n")
        position = input("What is the position called?\n>>> ")
        employer = input("What is the employer called?\n>>> ")
        phone_number = input("What is the employer's phone number?\n>>> ")
        date_applied = input("What is the application date?\n>>> ")
        add_application(position, employer, phone_number, date_applied)

    elif user_in.lower() == 'b':
        print('Opening Job Applications folder...\n')
        os.startfile(os.getcwd() + '\\job applications')

    elif user_in.lower() == 'c':
        print('Opening Resumes folder...\n')
        os.startfile(os.getcwd() + '\\resumes')

    elif user_in.lower() == 'd':
        print('Opening jobs_applied.csv...\n')
        os.startfile('jobs_applied.csv')

    elif user_in.lower() == 'x':
        cont_program = False
        break
    
    else:
        print('Invalid input!\n')