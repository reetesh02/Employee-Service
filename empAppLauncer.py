import emp_Service as empLauncer

#import empService as emps


 

#if __name__=="__main__":
 #   emp_details = emps.creatEmp()



if __name__ == "__main__":

    emp_details = empLauncer.CreateEmp()
    
    empLauncer.UpdateSalary(emp_details)

    empLauncer.DeleteEmp(emp_details)

    empLauncer.DisplayEmp(emp_details)



