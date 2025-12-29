import json
def adding_details():
    try:
       num_students=int(input("Enter the number of students you want to add: "))
       student_list=[]
       with open("student_data/data.json","r") as f:
            student_list=json.load(f) 
            # student_list= student_list
            print(student_list)

       
       for i in range(num_students):
           
           s={}       
           s["name"]=input(f"student_{i+1} name:")
           s["age"]=input(f"student_{i+1} age:")
           s["class"]=input(f"student_{i+1} class:")
           s["marks"]={}
           s["marks"]["maths"]=int(input(f"Enter student_{i+1} marks in maths:"))
           s["marks"]["science"]=int(input(f"Enter student_{i+1} marks in science:"))
           s["marks"]["english"]=int(input(f"Enter student_{i+1} marks in english:"))
                                                     
           student_list.append(s)
    except Exception as e:
        print(e)     
    return student_list


def viewing_details(student_details):
    try:
     for i in student_details:
        for j in i:
            print(f"{j}={i[j]}")
    except Exception as e:
        print(e)

   


def updating_details(student_details):
    try:
        student_name=input("Enter the name of the student you want to update:")
        for student in student_details:
            x=0
            if student.get("name")==student_name:
                print("Name found!!! Enter the updated details.")
                student["name"]=input("Enter the new name=")
                student["age"]=input("Enter the new age=")
                student["class"]=input("Enter the new class=")
                student["marks"]={}
                student["marks"]["maths"]=int(input(f"Enter student marks in maths:"))
                student["marks"]["science"]=int(input(f"Enter student marks in science:"))
                student["marks"]["english"]=int(input(f"Enter student marks in english:"))
                print("Data updated!!!")
                
                if x==1:
                  print("Name not found!!")
    except Exception as e:
        print(e)
        

    return student_details

def deleting_students(student_details):
    print("deleting student details")
    name=input("Enter the name of the student you want to delete=")
    student_name=0
    for student in student_details:
        
        if student.get("name")==name:
         print("Student name found!! Deleting it....")
         student_details.remove(student)
         print(student_details)
         
         student_name=0

    if student_name==1:
         print("Name not found!!")
    else:
            print("Name deleted successfully....")
    return student_details


def main_func():
    print("********** WELCOME TO EMS**********")
    student_details=None
    while True:
        print("To add student details press----> 1")
        print("To view student details press----> 2")
        print("To update student details press----> 3")
        print("To delete student details press----> 4")
        print("To exit press----> 5")
        user_choice=input("Enter your choice:")

        if user_choice=="5":
            print("EXITING......")
            break

        elif user_choice=="1":
            print("Adding student details....")
            student_details=adding_details()    
            print(student_details)        

            with open("student_data/data.json","w") as f:
                json.dump(student_details ,f,indent=4)
                
        
        elif user_choice=="2":
            print("Viewing student details.....")
            viewing_details(student_details)
            with open("student_data/data.json","r") as f:
                student_details=json.load(f)

        elif user_choice=="3":
            with open("student_data/data.json","r") as f:
                student_details=json.load(f)
            print("updating student details.....")
            student_details =updating_details(student_details)
            print(student_details)
            with open("student_data/data.json","w") as f:
                json.dump(student_details ,f,indent=4)
        elif user_choice == "4":
           with open("student_data/data.json","r") as f:
                student_details=json.load(f)
           deleting_students(student_details)
           with open("student_data/data.json","w") as f:
                json.dump(student_details ,f,indent=4)
        
        else:
            print("INCORRECT CHOICE!!!")

main_func()
