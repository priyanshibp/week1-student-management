import psycopg2
connection =psycopg2.connect(

    host="localhost",
    database="student_management",
    user="postgres",
    password="Priyanshi@123"
)

print("Database connection successfully!!")

connection.close()
