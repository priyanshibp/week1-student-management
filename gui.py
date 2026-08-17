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
        width=25
    )

    add_button.pack(pady=5)

    # --------------------------------------------------------
    # Update Student Button
    # --------------------------------------------------------

    update_button = tk.Button(
        window,
        text="Update Student",
        width=25
    )

    update_button.pack(pady=5)

    # --------------------------------------------------------
    # Delete Student Button
    # --------------------------------------------------------

    delete_button = tk.Button(
        window,
        text="Delete Student",
        width=25
    )

    delete_button.pack(pady=5)

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