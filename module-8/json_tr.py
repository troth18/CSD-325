import json

#Prints student data found in student.json in a specific format
def print_student(data):
    for student in data:
        print(f"{student['L_Name']}, {student['F_Name']}: ID = {student['Student_ID']}, Email = {student['Email']}")

def student():
    filename = 'student.json'

    #Opens student.json with read only permission
    with open(filename, 'r') as f:
        data = json.load(f)

        print("This is the original Student List:")
        print("")
        print_student(data)

        #Appends a new student to student data
        new_student = {"F_Name": "Tim",
                        "L_Name": "Roth",
                        "Student_ID": "42972",
                        "Email": "tiroth@my365.bellevue.edu"}
    
        data.append(new_student)

        print("")
        print("This is the updated Student list:")
        print("")
        print_student(data)

    #Writes the updated student data to student.json
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

        print("")
        print("The .json file was updated.")

student()