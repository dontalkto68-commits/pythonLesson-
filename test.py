"""
name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
salary = float(input("Enter salary: "))
absence = int(input("Enter number of absent days: "))

if absence < 0:
    print("Absent days cannot be negative.")
else:
    if absence > 20:
        print("Absent days cannot exceed 20.")

deduction = absence * 10
net_salary = salary - deduction

absence_rate = (absence / 20) * 100


print(f"Employee Name   :" + (name))
print(f"Employee ID     :" +(employee_id))
print(f"Basic Salary    :" + str(salary))
print(f"Absent Days     :" +str(absence))
print(f"Net Salary      :" + str(net_salary))

if absence >= 15:
    print("Warning: High absence rate of" + str(absence_rate))
elif absence >= 5:
    print("Notice: Moderate absence rate of" + str(absence_rate))
else:
    print("Good: Low absence rate of" + str(absence_rate))
"""
"""
import subprocess
#create a directory named C13_Exam'
subprocess.run("mkdir -p /C13_Exam",shell=True)
print("the folder was created successfully ")
print("-" * 40)
"""
"""
import subprocess
print("copy all files with txt extension from home user to /C13_Exam folder")
subprocess.run("cp ~/*.txt ~/pythonLesson/C13_Exam",shell=True)
print("=" * 100)
print("the files were copied successfully ")
"""
"""
name = input("Enter employee name: ")
employee_id = input("Enter employee ID: ")
salary = float(input("Enter salary: "))
absence = int(input("Enter number of absent days: "))

if absence < 0:
    print("Absent days cannot be negative.")
else:
    if absence > 20:
        print("Absent days cannot exceed 20.")

deduction = absence * 10
net_salary = salary - deduction

absence_rate = (absence / 20) * 100


print(f"Employee Name   :" + (name))
print(f"Employee ID     :" +(employee_id))
print(f"Basic Salary    :" + str(salary))
print(f"Absent Days     :" +str(absence))
print(f"Net Salary      :" + str(net_salary))

if absence >= 15:
    print("Warning: High absence rate of" + str(absence_rate))
elif absence >= 5:
    print("Notice: Moderate absence rate of" + str(absence_rate))
else:
    print("Good: Low absence rate of" + str(absence_rate))
"""
"""
import subprocess
#create a directory named C13_Exam'
subprocess.run("mkdir -p /C13_Exam",shell=True)
print("the folder was created successfully ")
print("-" * 40)
"""
"""
import subprocess
print("copy all files with txt extension from home user to /C13_Exam folder")
subprocess.run("cp ~/*.txt ~/pythonLesson/C13_Exam",shell=True)
print("=" * 40)
print("the files were copied successfully ")
print("-" * 40)
print ("fetching the list of files in C13_Exam folder")


print (subprocess.run("test -d ~/pythonLesson/C13_Exam",shell=True)) == 0:
    subprocess.run("ls -l ~/pythonLesson/C13_Exam",shell=True)
print("=" * 40)
print ("the files were listed successfully ")
    if print("the folder C13_Exam does not exist")
"""
"""
import subprocess
print("create a directory inisde C13_Exam folder named exam")
subprocess.run("mkdir -p ~/pythonLesson/C13_Exam/exam",shell=True)
print("=" * 40)

print("the folder exam_results was created successfully ")
result=subprocess.run("test.d ~/pythonLesson/C13_Exam/exam, && (echo 'file created successfully in exam folder' || echo 'the folder exam was not created successfully'",shell=True)
print("show printed message if the folder exam created successfully")
if result.returncode == 0:
    print("file created successfully in exam folder")   
 else

    print("the folder exam was not created successfully")
 
print("-" * 40)    
print ("file created successfully in exam folder")
"""
"""
#API
import subprocess

#create a directory named C13_Exam
subprocess.run("mkdir -p ~/pythonLesson/C13_Exam",shell=True)
#display message if folder created successfully

var = subprocess.run("ls -l ~/pythonLesson/C13_Exam",shell=True)    
#message if folder created successfully
print("the folder was created successfully ")
var = subprocess.run("test -d ~/pythonLesson/C13_Exam",shell=True)
#message if folder created unsuccessfully
if var.returncode != 0:
    print("the folder C13_Exam was not created successfully")
    exit(1) 
    print("=" * 40)
print ("the folder was created successfully ")  

#make exam folder inside C13_Exam
subprocess.run("mkdir -p ~/pythonLesson/C13_Exam/exam",shell=True)
subprocess.run("echo 'the folder C13_Exam was created successfully'",shell=True)        

#display content of C13_Exam folder
subprocess.run("ls -l ~/pythonLesson/C13_Exam",shell=True)  

#result check if C13_Exam folder created successfully
var = subprocess.run("test -d ~/pythonLesson/C13_Exam",shell=True)

#message if exam folder created successfully
print("=" * 40)
print("the folder exam was created successfully ")
print("=" * 40)
#list of files in C13_Exam folder
print ("fetching the list of files in C13_Exam folder")
var = subprocess.run("ls -l ~/pythonLesson/C13_Exam",shell=True)    

#check  if folder C13_Exam exists
if var.returncode != 0:
    print("the folder C13_Exam does not exist")
    exit(1) 
    print("=" * 40)
print ("the files were listed successfully ")

#if statement to delete
if var.returncode == 0:
    print("=" * 40)
    subprocess.run("ls -l ~/pythonLesson/C13_Exam",shell=True)
    #deltion of C13_Exam folder
    subprocess.run("delete ~/pythonLesson/C13_Exam/exam",shell=True)
    #message if folder deleted successfully
    print("the folder exam was deleted successfully ")
    print("=" * 40)  
#message if folder does not exist   
else:
    print("the folder C13_Exam does not exist")
"""
"""
import subprocess
 
 #in range so 1 2 3
for i in range(1,4):
    subprocess.run(f"touch ~/pythonLesson/C13_Exam/exam/file{i}.txt",shell=True)
print(f"Creating file{i}.txt in exam folder")
#inside loop
print("all files are created successfully")
#answer = file1 file2 file3
"""
"""
import subprocess

for i in range(1,8):
    subprocess.run(f"touch ~/pythonLesson/C13_Exam/exam/testfile{i}.txt",shell=True)
    print(f"Creating testfile{i}.txt in exam folder")
    #output
print("all files are created successfully") 
subprocess.run("ls -l ~/pythonLesson/C13_Exam/exam",shell=True)
"""
import subprocess

for i in range(8,21):
    subprocess.run(f"touch ~/pythonLesson/C13_Exam/exam/samplefile{i}.txt",shell=True)
    print(f"Creating samplefile{i}.txt in exam folder")
    #output
print("all files are created successfully") 
subprocess.run("ls -l ~/pythonLesson/C13_Exam/exam",shell=True)

#creating backup of files
print("copying sample files to C13_Exam folder as backup")  
subprocess.run("mkdir -p ~/pythonLesson/C13_Exam/backup",shell=True)
subprocess.run("cp ~/pythonLesson/C13_Exam/exam/samplefile*.txt ~/pythonLesson/C13_Exam/backup",shell=True)
print("all sample files copied successfully to backup folder")
subprocess.run("ls -l ~/pythonLesson/C13_Exam/backup",shell=True)

#deleting sample files from exam folder
print("deleting sample files from exam folder")
subprocess.run("rm ~/pythonLesson/C13_Exam/exam/samplefile*.txt",shell=True)
print("all sample files deleted successfully from exam folder")
subprocess.run("ls -l ~/pythonLesson/C13_Exam/exam",shell=True)