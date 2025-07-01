dict = {"Alice": 85}
stud_name = input("Enter the student's name: ")
if stud_name in dict:
    print(f"{stud_name}'s marks: {dict[stud_name]}")
else:
    print("Student not found")
