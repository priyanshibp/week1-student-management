# Week 6 - File Handling
# Append Mode

# Add a new line to the existing backup file
with open("student_backup.txt", "a") as file:

    file.write("Backup completed successfully.\n")

print("New information added to the backup file.")


# Read the file again
print("\nUpdated backup file:")
print("====================")

with open("student_backup.txt", "r") as file:

    content = file.read()

    print(content)