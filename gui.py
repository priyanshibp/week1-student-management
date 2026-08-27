import tkinter as tk
from tkinter import messagebox
from tkinter import ttk 

# PostgreSQL imports
import psycopg2
from dotenv import load_dotenv
import os


# ============================================================
# LOAD ENVIRONMENT VARIABLES
# ============================================================

# Load the values from the .env file
load_dotenv()


# ============================================================
# DATABASE CONNECTION
# ============================================================

def connect_database():
    """
    Connect to the PostgreSQL database
    and return the connection.
    """

    connection = psycopg2.connect(
        host="localhost",
        database="student_management",
        user="postgres",
        password=os.getenv("DB_PASSWORD")
    )

    return connection


# ============================================================
# LOGIN FUNCTION
# ============================================================

def login():
    """
    Check the username and password entered by the user.
    """

    # Get the username from the username input box
    username = username_entry.get()

    # Get the password from the password input box
    password = password_entry.get()

    # Check username AND password
    if username == "admin" and password == "1234":

        # If both are correct, open the Home Page
        open_home_page()

    else:

        # If username or password is incorrect
        messagebox.showerror(
            "Login Failed",
            "Invalid username or password"
        )
# ============================================================
# SEARCH STUDENT
# ============================================================

def search_student():
    """
    Search for a student by name.
    Uses SQL WHERE and displays the result in a table.
    """

    # Remove the current Home Page
    for widget in window.winfo_children():
        widget.destroy()

    # --------------------------------------------------------
    # Page Title
    # --------------------------------------------------------

    title_label = tk.Label(
        window,
        text="Search Student",
        font=("Arial", 22, "bold")
    )

    title_label.pack(pady=30)

    # --------------------------------------------------------
    # Name Label
    # --------------------------------------------------------

    name_label = tk.Label(
        window,
        text="Enter Student Name:"
    )

    name_label.pack()

    # --------------------------------------------------------
    # Name Input
    # --------------------------------------------------------

    name_entry = tk.Entry(
        window,
        width=30
    )

    name_entry.pack(pady=10)

    # --------------------------------------------------------
    # Search Function
    # --------------------------------------------------------

    def perform_search():

        # Get the name entered by the user
        name = name_entry.get().strip()

        # Check if the input is empty
        if name == "":
            messagebox.showwarning(
                "Input Required",
                "Please enter a student name."
            )
            return

        try:

            # Connect to PostgreSQL
            connection = connect_database()

            # Create cursor
            cursor = connection.cursor()

            # ------------------------------------------------
            # SQL SEARCH USING WHERE
            # LOWER() makes the search case-insensitive
            # ------------------------------------------------

            query = """
                SELECT student_id, name, age, city, phone
                FROM students
                WHERE LOWER(name) = LOWER(%s)
                ORDER BY student_id ASC
            """

            cursor.execute(query, (name,))

            # Get matching records
            students = cursor.fetchall()

            # Close database connection
            cursor.close()
            connection.close()

            # ------------------------------------------------
            # Remove old search results
            # ------------------------------------------------

            for widget in window.winfo_children():

                # Keep the title, input and buttons
                # We don't need to remove them here.
                pass

            # ------------------------------------------------
            # Check Search Result
            # ------------------------------------------------

            if len(students) == 0:

                messagebox.showinfo(
                    "Search Result",
                    "No student found."
                )

            else:

                # ------------------------------------------------
                # Create Table
                # ------------------------------------------------

                table = ttk.Treeview(
                    window,
                    columns=(
                        "id",
                        "name",
                        "age",
                        "city",
                        "phone"
                    ),
                    show="headings"
                )

                # ------------------------------------------------
                # Table Headings
                # ------------------------------------------------

                table.heading(
                    "id",
                    text="Student ID"
                )

                table.heading(
                    "name",
                    text="Name"
                )

                table.heading(
                    "age",
                    text="Age"
                )

                table.heading(
                    "city",
                    text="City"
                )

                table.heading(
                    "phone",
                    text="Phone"
                )

                # ------------------------------------------------
                # Column Widths
                # ------------------------------------------------

                table.column(
                    "id",
                    width=80,
                    anchor="center"
                )

                table.column(
                    "name",
                    width=120
                )

                table.column(
                    "age",
                    width=60,
                    anchor="center"
                )

                table.column(
                    "city",
                    width=120
                )

                table.column(
                    "phone",
                    width=120
                )

                # ------------------------------------------------
                # Add Student Records
                # ------------------------------------------------

                for student in students:

                    table.insert(
                        "",
                        tk.END,
                        values=student
                    )

                # Display table
                table.pack(
                    pady=20
                )

        except Exception as error:

            # Show database error
            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # --------------------------------------------------------
    # Search Button
    # --------------------------------------------------------

    search_button = tk.Button(
        window,
        text="Search",
        width=20,
        command=perform_search
    )

    search_button.pack(pady=10)


    # --------------------------------------------------------
    # Back Button
    # --------------------------------------------------------

    back_button = tk.Button(
        window,
        text="Back",
        width=20,
        command=open_home_page
    )

    back_button.pack(pady=10)

# ============================================================
# UPDATE STUDENT
# ============================================================

def update_student():
    """
    Page used to update an existing student's information.
    """

    # --------------------------------------------------------
    # Remove the current Home Page
    # --------------------------------------------------------

    for widget in window.winfo_children():
        widget.destroy()

    # --------------------------------------------------------
    # Page Title
    # --------------------------------------------------------

    title_label = tk.Label(
        window,
        text="Update Student",
        font=("Arial", 22, "bold")
    )

    title_label.pack(pady=30)

    # --------------------------------------------------------
    # Student ID Label
    # --------------------------------------------------------

    id_label = tk.Label(
        window,
        text="Enter Student ID:"
    )

    id_label.pack()

    # --------------------------------------------------------
    # Student ID Input
    # --------------------------------------------------------

    id_entry = tk.Entry(
        window,
        width=30
    )

    id_entry.pack(pady=10)

    # --------------------------------------------------------
    # New Name Label
    # --------------------------------------------------------

    name_label = tk.Label(
        window,
        text="New Name:"
    )

    name_label.pack()

    # --------------------------------------------------------
    # New Name Input
    # --------------------------------------------------------

    name_entry = tk.Entry(
        window,
        width=30
    )

    name_entry.pack(pady=10)

    # --------------------------------------------------------
    # New Age Label
    # --------------------------------------------------------

    age_label = tk.Label(
        window,
        text="New Age:"
    )

    age_label.pack()

    # --------------------------------------------------------
    # New Age Input
    # --------------------------------------------------------

    age_entry = tk.Entry(
        window,
        width=30
    )

    age_entry.pack(pady=10)

    # --------------------------------------------------------
    # New City Label
    # --------------------------------------------------------

    city_label = tk.Label(
        window,
        text="New City:"
    )

    city_label.pack()

    # --------------------------------------------------------
    # New City Input
    # --------------------------------------------------------

    city_entry = tk.Entry(
        window,
        width=30
    )

    city_entry.pack(pady=10)

    # --------------------------------------------------------
    # New Phone Label
    # --------------------------------------------------------

    phone_label = tk.Label(
        window,
        text="New Phone:"
    )

    phone_label.pack()

    # --------------------------------------------------------
    # New Phone Input
    # --------------------------------------------------------

    phone_entry = tk.Entry(
        window,
        width=30
    )

    phone_entry.pack(pady=10)
  # --------------------------------------------------------
    # Update Student Function
    # --------------------------------------------------------

    def perform_update():

        print("UPDATE BUTTON CLICKED")
        """
        Update the selected student's information
        in the PostgreSQL database.
        """

        # Get values from the input fields
        student_id = id_entry.get().strip()
        name = name_entry.get().strip()
        age = age_entry.get().strip()
        city = city_entry.get().strip()
        phone = phone_entry.get().strip()

        # ----------------------------------------------------
        # Check that all fields are filled
        # ----------------------------------------------------

        if (
            student_id == ""
            or name == ""
            or age == ""
            or city == ""
            or phone == ""
        ):
            messagebox.showwarning(
                "Input Required",
                "Please fill in all fields."
            )
            return

        # ----------------------------------------------------
        # Check that Student ID and Age are numbers
        # ----------------------------------------------------

        if not student_id.isdigit():
            messagebox.showwarning(
                "Invalid Student ID",
                "Student ID must be a number."
            )
            return

        if not age.isdigit():
            messagebox.showwarning(
                "Invalid Age",
                "Age must be a number."
            )
            return

        try:

            # Convert ID and age to integers
            student_id_number = int(student_id)
            age_number = int(age)

            # ------------------------------------------------
            # Connect to PostgreSQL
            # ------------------------------------------------

            connection = connect_database()

            cursor = connection.cursor()

            # ------------------------------------------------
            # SQL UPDATE
            # ------------------------------------------------

            query = """
                UPDATE students
                SET name = %s,
                    age = %s,
                    city = %s,
                    phone = %s
                WHERE student_id = %s
            """

            cursor.execute(
                query,
                (
                    name,
                    age_number,
                    city,
                    phone,
                    student_id_number
                )
            )

            # ------------------------------------------------
            # Save the changes
            # ------------------------------------------------

            connection.commit()

            # Check whether a student was actually updated
            if cursor.rowcount == 0:

                messagebox.showwarning(
                    "Not Found",
                    "No student found with this ID."
                )

            else:

                messagebox.showinfo(
                    "Success",
                    "Student updated successfully!"
                )

            # Close connection
            cursor.close()
            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # --------------------------------------------------------
    # Update Student Button
    # --------------------------------------------------------

    save_button = tk.Button(
        window,
        text="Update Student",
        width=20,
        command=perform_update
    )

    save_button.pack(pady=15)

    # --------------------------------------------------------
    # Back Button
    # --------------------------------------------------------

    back_button = tk.Button(
        window,
        text="Back",
        width=20,
        command=open_home_page
    )

    back_button.pack(pady=10)
# ============================================================
# ADD STUDENT
# ============================================================

def add_student():
    # Clear current page
    for widget in window.winfo_children():
        widget.destroy()

    # --------------------------------------------------------
    # Page Title
    # --------------------------------------------------------

    title_label = tk.Label(
        window,
        text="Add Student",
        font=("Arial", 22, "bold")
    )

    title_label.pack(pady=25)

    # --------------------------------------------------------
    # Student ID
    # --------------------------------------------------------

    id_label = tk.Label(
        window,
        text="Student ID:"
    )

    id_label.pack(pady=5)

    id_entry = tk.Entry(
        window,
        width=30
    )

    id_entry.pack(pady=5)

    # --------------------------------------------------------
    # Name
    # --------------------------------------------------------

    name_label = tk.Label(
        window,
        text="Name:"
    )

    name_label.pack(pady=5)

    name_entry = tk.Entry(
        window,
        width=30
    )

    name_entry.pack(pady=5)

    # --------------------------------------------------------
    # Age
    # --------------------------------------------------------

    age_label = tk.Label(
        window,
        text="Age:"
    )

    age_label.pack(pady=5)

    age_entry = tk.Entry(
        window,
        width=30
    )

    age_entry.pack(pady=5)

    # --------------------------------------------------------
    # City
    # --------------------------------------------------------

    city_label = tk.Label(
        window,
        text="City:"
    )

    city_label.pack(pady=5)

    city_entry = tk.Entry(
        window,
        width=30
    )

    city_entry.pack(pady=5)

    # --------------------------------------------------------
    # Phone
    # --------------------------------------------------------

    phone_label = tk.Label(
        window,
        text="Phone:"
    )

    phone_label.pack(pady=5)

    phone_entry = tk.Entry(
        window,
        width=30
    )

    phone_entry.pack(pady=5)

    # --------------------------------------------------------
    # Save Student
    # --------------------------------------------------------

    def save_student():

        student_id = id_entry.get()
        name = name_entry.get()
        age = age_entry.get()
        city = city_entry.get()
        phone = phone_entry.get()

        if not student_id or not name or not age or not city or not phone:
            messagebox.showwarning(
                "Missing Information",
                "Please fill in all fields."
            )
            return

        try:

            student_id = int(student_id)
            age = int(age)

            connection = connect_database()
            cursor = connection.cursor()

            query = """
                INSERT INTO students
                (student_id, name, age, city, phone)
                VALUES (%s, %s, %s, %s, %s)
            """

            values = (
                student_id,
                name,
                age,
                city,
                phone
            )

            cursor.execute(query, values)

            connection.commit()

            cursor.close()
            connection.close()

            messagebox.showinfo(
                "Success",
                "Student added successfully."
            )

            id_entry.delete(0, tk.END)
            name_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)
            city_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)

        except ValueError:

            messagebox.showerror(
                "Invalid Input",
                "Student ID and Age must be numbers."
            )

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    add_button = tk.Button(
        window,
        text="Add Student",
        width=20,
        command=save_student
    )

    add_button.pack(pady=15)

    # --------------------------------------------------------
    # Back Button
    # --------------------------------------------------------

    back_button = tk.Button(
        window,
        text="Back",
        width=20,
        command=open_home_page
    )

    back_button.pack(pady=10)
# ============================================================
# DELETE STUDENT
# ============================================================

def delete_student():
    """
    Page used to delete a student from the database.
    """

    # --------------------------------------------------------
    # Remove the current Home Page
    # --------------------------------------------------------

    for widget in window.winfo_children():
        widget.destroy()

    # --------------------------------------------------------
    # Page Title
    # --------------------------------------------------------

    title_label = tk.Label(
        window,
        text="Delete Student",
        font=("Arial", 22, "bold")
    )

    title_label.pack(pady=40)

    # --------------------------------------------------------
    # Student ID Label
    # --------------------------------------------------------

    id_label = tk.Label(
        window,
        text="Enter Student ID:"
    )

    id_label.pack(pady=5)

    # --------------------------------------------------------
    # Student ID Input
    # --------------------------------------------------------

    id_entry = tk.Entry(
        window,
        width=30
    )

    id_entry.pack(pady=10)

    # --------------------------------------------------------
    # Delete Function
    # --------------------------------------------------------

    def perform_delete():
        """
        Delete the selected student from PostgreSQL.
        """

        # Get Student ID from the input box
        student_id = id_entry.get().strip()

        # ----------------------------------------------------
        # Check if Student ID was entered
        # ----------------------------------------------------

        if student_id == "":
            messagebox.showwarning(
                "Input Required",
                "Please enter a Student ID."
            )
            return

        # ----------------------------------------------------
        # Check if Student ID is a number
        # ----------------------------------------------------

        if not student_id.isdigit():
            messagebox.showwarning(
                "Invalid Student ID",
                "Student ID must be a number."
            )
            return

        # Convert Student ID to integer
        student_id_number = int(student_id)

        # ----------------------------------------------------
        # Confirmation message
        # ----------------------------------------------------

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete student ID {student_id_number}?"
        )

        # If user selects No, stop here
        if not confirm:
            return

        try:

            # ------------------------------------------------
            # Connect to PostgreSQL
            # ------------------------------------------------

            connection = connect_database()

            cursor = connection.cursor()

            # ------------------------------------------------
            # SQL DELETE
            # ------------------------------------------------

            query = """
                DELETE FROM students
                WHERE student_id = %s
            """

            cursor.execute(
                query,
                (student_id_number,)
            )

            # ------------------------------------------------
            # Save the changes
            # ------------------------------------------------

            connection.commit()

            # ------------------------------------------------
            # Check whether a student was deleted
            # ------------------------------------------------

            if cursor.rowcount == 0:

                messagebox.showwarning(
                    "Not Found",
                    "No student found with this ID."
                )

            else:

                messagebox.showinfo(
                    "Success",
                    "Student deleted successfully!"
                )

                # Clear the input after successful deletion
                id_entry.delete(0, tk.END)

            # Close database connection
            cursor.close()
            connection.close()

        except Exception as error:

            messagebox.showerror(
                "Database Error",
                str(error)
            )

    # --------------------------------------------------------
    # Delete Student Button
    # --------------------------------------------------------

    delete_button = tk.Button(
        window,
        text="Delete Student",
        width=20,
        command=perform_delete
    )

    delete_button.pack(pady=15)

    # --------------------------------------------------------
    # Back Button
    # --------------------------------------------------------

    back_button = tk.Button(
        window,
        text="Back",
        width=20,
        command=open_home_page
    )

    back_button.pack(pady=10)

# ============================================================
# REPORTS
# ============================================================

def reports_page():
    """
    Display student reports using SQL aggregate functions,
    GROUP BY, and HAVING.
    """

    # --------------------------------------------------------
    # Clear current page
    # --------------------------------------------------------

    for widget in window.winfo_children():
        widget.destroy()

    # --------------------------------------------------------
    # Page Title
    # --------------------------------------------------------

    title_label = tk.Label(
        window,
        text="Student Reports",
        font=("Arial", 22, "bold")
    )

    title_label.pack(pady=25)

    # --------------------------------------------------------
    # Get Overall Statistics
    # COUNT, AVG, MIN, MAX
    # --------------------------------------------------------

    try:

        connection = connect_database()
        cursor = connection.cursor()

        query = """
            SELECT
                COUNT(*),
                AVG(age),
                MIN(age),
                MAX(age)
            FROM students
        """

        cursor.execute(query)

        result = cursor.fetchone()

        total_students = result[0]
        average_age = result[1]
        youngest_age = result[2]
        oldest_age = result[3]

        cursor.close()
        connection.close()

        # ----------------------------------------------------
        # Total Students
        # ----------------------------------------------------

        total_label = tk.Label(
            window,
            text=f"Total Students: {total_students}",
            font=("Arial", 15)
        )

        total_label.pack(pady=5)

        # ----------------------------------------------------
        # Average Age
        # ----------------------------------------------------

        if average_age is not None:
            average_label = tk.Label(
                window,
                text=f"Average Age: {average_age:.2f}",
                font=("Arial", 15)
            )
        else:
            average_label = tk.Label(
                window,
                text="Average Age: No data",
                font=("Arial", 15)
            )

        average_label.pack(pady=5)

        # ----------------------------------------------------
        # Youngest Age
        # ----------------------------------------------------

        youngest_label = tk.Label(
            window,
            text=f"Youngest Age: {youngest_age}",
            font=("Arial", 15)
        )

        youngest_label.pack(pady=5)

        # ----------------------------------------------------
        # Oldest Age
        # ----------------------------------------------------

        oldest_label = tk.Label(
            window,
            text=f"Oldest Age: {oldest_age}",
            font=("Arial", 15)
        )

        oldest_label.pack(pady=5)

    except Exception as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )

        return

    # --------------------------------------------------------
    # Students By City
    # GROUP BY
    # --------------------------------------------------------

    city_title = tk.Label(
        window,
        text="Students By City",
        font=("Arial", 17, "bold")
    )

    city_title.pack(pady=(20, 5))

    try:

        connection = connect_database()
        cursor = connection.cursor()

        query = """
            SELECT city, COUNT(*)
            FROM students
            GROUP BY city
            ORDER BY city
        """

        cursor.execute(query)

        city_results = cursor.fetchall()

        cursor.close()
        connection.close()

        if len(city_results) == 0:

            city_label = tk.Label(
                window,
                text="No city data available.",
                font=("Arial", 13)
            )

            city_label.pack(pady=5)

        else:

            for city, count in city_results:

                city_label = tk.Label(
                    window,
                    text=f"{city}: {count} student(s)",
                    font=("Arial", 13)
                )

                city_label.pack(pady=2)

    except Exception as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )

    # --------------------------------------------------------
    # Cities With More Than 1 Student
    # HAVING
    # --------------------------------------------------------

    having_title = tk.Label(
        window,
        text="Cities With More Than 1 Student",
        font=("Arial", 17, "bold")
    )

    having_title.pack(pady=(15, 5))

    try:

        connection = connect_database()
        cursor = connection.cursor()

        query = """
            SELECT city, COUNT(*)
            FROM students
            GROUP BY city
            HAVING COUNT(*) > 1
            ORDER BY city
        """

        cursor.execute(query)

        having_results = cursor.fetchall()

        cursor.close()
        connection.close()

        if len(having_results) == 0:

            having_label = tk.Label(
                window,
                text="No cities have more than 1 student.",
                font=("Arial", 13)
            )

            having_label.pack(pady=5)

        else:

            for city, count in having_results:

                having_label = tk.Label(
                    window,
                    text=f"{city}: {count} student(s)",
                    font=("Arial", 13)
                )

                having_label.pack(pady=2)

    except Exception as error:

        messagebox.showerror(
            "Database Error",
            str(error)
        )

    # --------------------------------------------------------
    # Back Button
    # --------------------------------------------------------

    back_button = tk.Button(
        window,
        text="Back",
        width=20,
        command=open_home_page
    )

    back_button.pack(pady=20)

  
# ============================================================
# HOME PAGE
# ============================================================

def open_home_page():
    """
    Display the main Home Page after successful login.
    """

    # Remove all widgets from the current page
    for widget in window.winfo_children():
        widget.destroy()

    # --------------------------------------------------------
    # Home Page Title
    # --------------------------------------------------------

    title_label = tk.Label(
        window,
        text="Student Management System",
        font=("Arial", 22, "bold")
    )

    title_label.pack(pady=30)

    # --------------------------------------------------------
    # Welcome Message
    # --------------------------------------------------------

    welcome_label = tk.Label(
        window,
        text="Welcome, Admin!",
        font=("Arial", 14)
    )

    welcome_label.pack(pady=10)

    # --------------------------------------------------------
    # View Students Button
    # --------------------------------------------------------

    view_button = tk.Button(
        window,
        text="View Students",
        width=25,
        command=view_students
    )

    view_button.pack(pady=5)

    # --------------------------------------------------------
    # Search Student Button
    # --------------------------------------------------------
    search_button = tk.Button(
    window,
    text="Search Student",
    width=25,
    command=search_student
)

    search_button.pack(pady=5)

    # --------------------------------------------------------
    # Add Student Button
    # --------------------------------------------------------

    add_button = tk.Button(
        window,
        text="Add Student",
        width=25,
        command=add_student
    )

    add_button.pack(pady=5)

    # --------------------------------------------------------
    # Update Student Button
    # --------------------------------------------------------

    update_button = tk.Button(
        window,
        text="Update Student",
        width=25,
         command=update_student
    )

    update_button.pack(pady=5)

    # --------------------------------------------------------
    # Delete Student Button
    # --------------------------------------------------------

    delete_button = tk.Button(
        window,
        text="Delete Student",
        width=25,
         command=delete_student
    )

    delete_button.pack(pady=5)


    # --------------------------------------------------------
    # Reports Button    
    # --------------------------------------------------------

    reports_button = tk.Button(
    window,
    text="Reports",
    width=25,
    command=reports_page
    )

    reports_button.pack(pady=5)

    # --------------------------------------------------------
    # Logout Button
    # --------------------------------------------------------

    logout_button = tk.Button(
        window,
        text="Logout",
        width=25,
        command=show_login_page
    )

    logout_button.pack(pady=20)


# ============================================================
# VIEW STUDENTS
# ============================================================

# ============================================================
# VIEW STUDENTS
# ============================================================

def view_students():
    """
    Get all student records from PostgreSQL
    and display them in a table.
    """

    try:

        # Connect to the database
        connection = connect_database()

        # Create a cursor
        cursor = connection.cursor()

        # Get all students
        cursor.execute("""
            SELECT student_id, name, age, city, phone
            FROM students
            ORDER BY student_id ASC
        """)

        # Store all student records
        students = cursor.fetchall()

        # Close database connection
        cursor.close()
        connection.close()

        # Remove Home Page widgets
        for widget in window.winfo_children():
            widget.destroy()

        # ----------------------------------------------------
        # Page Title
        # ----------------------------------------------------

        title_label = tk.Label(
            window,
            text="Student Records",
            font=("Arial", 22, "bold")
        )

        title_label.pack(pady=20)

        # ----------------------------------------------------
        # Create Student Table
        # ----------------------------------------------------

        table = ttk.Treeview(
            window,
            columns=("id", "name", "age", "city", "phone"),
            show="headings"
        )

        # ----------------------------------------------------
        # Table Headings
        # ----------------------------------------------------

        table.heading("id", text="Student ID")
        table.heading("name", text="Name")
        table.heading("age", text="Age")
        table.heading("city", text="City")
        table.heading("phone", text="Phone")

        # ----------------------------------------------------
        # Set Column Widths
        # ----------------------------------------------------

        table.column("id", width=80, anchor="center")
        table.column("name", width=120)
        table.column("age", width=60, anchor="center")
        table.column("city", width=120)
        table.column("phone", width=120)

        # ----------------------------------------------------
        # Add Student Records to Table
        # ----------------------------------------------------

        for student in students:

            table.insert(
                "",
                tk.END,
                values=student
            )

        # Display the table
        table.pack(pady=10)

        # ----------------------------------------------------
        # Back Button
        # ----------------------------------------------------

        back_button = tk.Button(
            window,
            text="Back",
            width=20,
            command=open_home_page
        )

        back_button.pack(pady=20)

    except Exception as error:

        # Show database error
        messagebox.showerror(
            "Database Error",
            str(error)
        )


# ============================================================
# LOGIN PAGE
# ============================================================

def show_login_page():
    """
    Display the Login Page.
    """

    # Remove all existing widgets
    for widget in window.winfo_children():
        widget.destroy()

    # --------------------------------------------------------
    # Login Title
    # --------------------------------------------------------

    title_label = tk.Label(
        window,
        text="Student Login",
        font=("Arial", 22, "bold")
    )

    title_label.pack(pady=30)

    # --------------------------------------------------------
    # Username Label
    # --------------------------------------------------------

    username_label = tk.Label(
        window,
        text="Username"
    )

    username_label.pack()

    # --------------------------------------------------------
    # Username Input
    # --------------------------------------------------------

    global username_entry

    username_entry = tk.Entry(
        window,
        width=30
    )

    username_entry.pack(pady=5)

    # --------------------------------------------------------
    # Password Label
    # --------------------------------------------------------

    password_label = tk.Label(
        window,
        text="Password"
    )

    password_label.pack()

    # --------------------------------------------------------
    # Password Input
    # --------------------------------------------------------

    global password_entry

    password_entry = tk.Entry(
        window,
        width=30,
        show="*"
    )

    password_entry.pack(pady=5)

    # --------------------------------------------------------
    # Login Button
    # --------------------------------------------------------

    login_button = tk.Button(
        window,
        text="Login",
        width=20,
        command=login
    )

    login_button.pack(pady=25)


# ============================================================
# MAIN WINDOW
# ============================================================

# Create the main Tkinter window
window = tk.Tk()

# Set the window title
window.title("Student Management System")

# Set the window size
window.geometry("500x500")


# ============================================================
# START APPLICATION
# ============================================================

# Show the Login Page when the program starts
show_login_page()

# Keep the GUI application running
window.mainloop()