import tkinter as tk
from tkinter import messagebox
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="student_app",
    password="StudentApp@123",
    database="college"
)

cursor = db.cursor()
root = tk.Tk()
root.title("Student Management System")
root.geometry("400x350")

tk.Label(
    root,
    text="STUDENT MANAGEMENT SYSTEM",
    font=("Arial", 14, "bold")
).pack(pady=15)

tk.Label(root, text="Student ID").pack()
entry_id = tk.Entry(root)
entry_id.pack()

tk.Label(root, text="Student Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Marks").pack()
entry_marks = tk.Entry(root)
entry_marks.pack()


def add_student():
    sid = entry_id.get()
    name = entry_name.get()
    marks = entry_marks.get()

    if not sid or not name or not marks:
        messagebox.showerror("Error", "Fill all fields!")
        return

    try:
        cursor.execute(
            "INSERT INTO student (sid, name, marks) VALUES (%s, %s, %s)",
            (int(sid), name, int(marks))
        )
        db.commit()

    messagebox.showinfo(
        "Success",
        "Student added successfully!"
    )
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_marks.delete(0, tk.END)

    except mysql.connector.Error as error:
        db.rollback()
        messagebox.showerror("Database Error", str(error))

    except ValueError:
        messagebox.showerror(
            "Input Error",
            "Student ID and marks must be numbers!"
        )


tk.Button(
    root,
    text="Add Student",
    command=add_student
).pack(pady=15)

root.mainloop()