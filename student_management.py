import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Connect to PostgreSQL
connection = psycopg2.connect(
    host="localhost",
    database="student_management",
    user="postgres",
    password=os.getenv("DB_PASSWORD")
)

print("Database connection successfully!!")

cursor = connection.cursor()

# Get student information
name = input("Enter student name: ")
age = int(input("Enter student age: "))
height = float(input("Enter student height in meters: "))
city = input("Enter student city: ")

# Insert student into the existing table
query = """
    INSERT INTO students (name, age, height, city)
    VALUES (%s, %s, %s, %s)
"""

cursor.execute(query, (name, age, height, city))

connection.commit()

print("Student added successfully!!!")

# Display all students
cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("\nStudents:")

for student in students:
    print(student)

# Close database connection
cursor.close()
connection.close()


