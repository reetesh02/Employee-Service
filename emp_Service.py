
def CreateEmp():
    a = str(input('Do you want to Create New Employee?:  '))
    b = ['YES','Yes','yes','Y','y']
    emp_details = {}
     
    if a in b:
        Number_of_Employees = int(input('Number of Employees to be Created:'))
        for i in range(1, Number_of_Employees+1):
          id = int(input('Enter ID:  '))
          name= str(input('Enter Name:  '))
          salary = int(input('Enter Salary:  '))
          age = int(input('Enter Age:  '))
          company = str(input('Enter Company:  '))
          profession = str(input('Enter Profession:  '))
          emp_details[id] ={'id':id,'name':name,'salary':salary,'age':age,'company':company,'profession':profession}
          #print('Employee Details: ' '\nID',emp_details[id]['id'],'\nName',emp_details[id]['name'],'\nSalary',emp_details[id]['salary'],'\nAge',emp_details[id]['age'],'\nCompany',emp_details[id]['company'],'\nProfession',emp_details[id]['profession'])
          #print('Successfully Created')
        DisplayEmp(emp_details)
        return emp_details
    else:print('New Employees not to be created')



def UpdateSalary(emp_details):
    c = str(input('Do you want to update Employee Salary : '))
    d = ['YES','yes','Yes','Y','y']
    if c in d:
        id = int(input('Employee ID for which Salary Update Required:'))
        Updated_Salary = int(input('New Updated Salary:'))
        emp_details[id]['salary'] = Updated_Salary
        print('Updated Salary is:', emp_details[id]['salary'])
        DisplayEmp(emp_details)
    else:
        print('Salary Update not Required')



def DeleteEmp(emp_details):
    e = str(input('Do you want to delete Employee Details: '))
    f= ['YES','Yes','yes','Y','y']
    if e in f:
        id = int(input('Enter Employee ID to be deleted: '))
        emp_details.pop(id)
        return emp_details
    


def DisplayEmp(emp_details):
    for y in emp_details:
        print('ID',y,emp_details[y])
