# Week 5 - Lists and Dictionaries

students = [
    {
        "student_id": 1,
        "name": "Priya",
        "age": 21,
        "city": "London"
    },
    {
        "student_id": 2,
        "name": "Rahul",
        "age": 22,
        "city": "London"
    },
    {
        "student_id": 3,
        "name": "Anjali",
        "age": 20,
        "city": "Birmingham"
    }
]

# Display all students
print("All Students:")

for student in students:
    print(student)


# Search student
search_name = input("\nEnter student name to search: ")

found = False

for student in students:
    if student["name"].lower() == search_name.lower():
        print("\nStudent Found:")
        print(student)
        found = True
        break

if not found:
    print("\nStudent not found.")


# Update student
update_name = input("\nEnter student name to update: ")

found = False

for student in students:
    if student["name"].lower() == update_name.lower():

        new_city = input("Enter new city: ")

        student["city"] = new_city

        print("\nStudent updated successfully!")
        print(student)

        found = True
        break

if not found:
    print("\nStudent not found.")


# Display final records
print("\nFinal Student Records:")

for student in students:
    print(student)

    