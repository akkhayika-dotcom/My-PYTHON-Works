
def adding_students():
    print("Adding student details")
    number_of_students = input("\nEnter number of students to be added = ")
    student_lists= []    
    for i in range(int(number_of_students)):  
        d={}      
        name =input(f"Enter Student{i+1} name = ")
        age =int(input(f"Enter Student{i+1} age = "))
        classes=input(f"Enter Student{i+1} class = ")
        try:
            if not name.isalpha():
                print("\nOops, invalid name.\nName should only contain characters A to Z!")
        
            if  age not in range(1,110):
                print("\n Invalid age acceptable age in range is 1 to 109 ")
        
            if  age not in range(1,13):
                print("\n Invalid class  acceptable class  in range is 1 to 12 ")
        except:
            d["name"] = name
            d["age"] = age
            d["class"] = classes


        
        
        print("-------------")
        student_lists.append(d)

    
    return student_lists

def displaying_students(student_details):
    print("display student details")
    for i in student_details:
        for j in i:
            print(f"{j}={i[j]}")


def updating_students(student_details):
    print("updating student details",student_details)
    name=input("Enter the name of the student you want to update=")

    is_found = 0
    for student in student_details:
        if student.get("name")==name:
            print("Student name found!  Enter the updated details.")            
            student["name"]=input("Enter the new name=")
            student["age"]=input("Enter the new age=")
            student["class"]=input("Enter the new class=")
            is_found = 1
        
           
    if is_found == 0:
        print("Name not found!!")
    else:
        print("Student Details Updated = ",student_details)
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

def main():
    print(" ------- WELCOME TO OUR SMS -----------")
    student_data = None
    while True:        
        print("\nPress 1 for Adding student details....")
        print("Press 2 for Displaying student details....")
        print("Press 3 for updating student details....")
        print("Press 4 for deleting student details....")
        print("Press 5 for Exit....")

        user_input = input("\nenter your choice = ")
       
        if user_input == "5":
            print("\n Exiting......")
            break
        elif user_input == "1":
            student_details = adding_students()
            
            student_data = student_details
            print("\n students details = ",student_details)
        elif user_input == "2":
            if student_data:
                print("\n students student_data = ",student_data)
                displaying_students(student_data)
            else:
                print("no students found!!!")
        elif user_input == "3":
            # student_details = [{'name': 'jj', 'age': '88', 'class': '99'},{'name': 'kk', 'age': '99', 'class': '9'}]
            student_data = updating_students(student_details)
        elif user_input == "4":
            #  student_details = [{'name': 'jj', 'age': '88', 'class': '99'},{'name': 'kk', 'age': '99', 'class': '9'}]
             deleting_students(student_details)
        else:
            print("\n Invalid choice !!! Please select valid choice....")
            
           
    




main()

