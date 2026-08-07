import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

connection = psycopg2.connect(
    host="localhost",
    database="student_management",
    user="postgres",
    password=os.getenv("DB_PASSWORD")
)

print("Database connection successfully!!")

connection.close()