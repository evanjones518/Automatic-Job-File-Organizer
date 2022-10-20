import os
import csv
import docx


def add_application(position, employer, date_applied):

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

    with open('jobs_applied.csv', 'w') as csvfile:
        field_names = ["Jobs", 'Employer', 'Phone Number', 'Applied?', 'Contacted?', 'Interview?', 'Offer?']
        writer = csv.DictWriter(csvfile, field_names)
        writer.writerow({'Jobs': position, 'Employer': employer, 'Phone Number': None, 'Applied?': date_applied, 'Contacted?': None, 'Interview?': None, 'Offer?': None})
    

#Boolean for program continuation in a while loop.
cont_program = True
file_path = os.path.dirname(__file__)
print(file_path)
os.chdir(file_path)

#Checks if job applications folder is present
if not os.path.exists(os.getcwd() + "\job applications"):
    print('Creating "Job Applications" folder.')
    os.mkdir('job applications')

#Checks if resumes folder is present
if not os.path.exists(os.getcwd() + '\\resumes'):
    print('Creating "Resumes" folder.')
    os.mkdir('resumes')
#Checks to see if jobs_applied csv is present and creates one if not.
#***UNDER CONSTRUCTION***
if not os.path.isfile(os.getcwd() + "\\jobs_applied.csv"):
    print("Creating new jobs applied csv.")
    with open('jobs_applied.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Jobs", 'Employer', 'Phone Number', 'Applied?', 'Contacted?', 'Interview?', 'Offer?'])


#Main body of the UX
while cont_program == True:
    user_in = input("What would you like to do?\n[A] Add Application\n[B] View Job Applications Folder\n[C] View Resume Folder\n[D] View Application Spreadsheet\n[X] Exit Program\n>>> ")
    

    if user_in.lower() == 'a':
        position = input("What is the position called?\n>>> ")
        employer = input("What is the employer called?\n>>> ")
        date_applied = input("What is the application date?\n>>> ")
        add_application(position, employer, date_applied)

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
    
    #This always prints unless x is typed. I need to replace the above ifs with elifs.
    else:
        print('Invalid input!\n')