from tkinter import *
from tkinter import messagebox
import re
import mysql.connector


class LoginForm:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")
        self.root.configure(bg="pink")
        self.root.title("FORM")

        self.font_style = ("Arial", 11, "bold")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 400) // 2

        self.root.geometry(f"400x400+{x}+{y}")

        self.root.rowconfigure(0, minsize=70)
        self.root.rowconfigure(5, minsize=70)

        self.heading_label = self.headingto_label("Login Form", 0, 0, columnspan=2, font_size=12, padx_value=17)
        self.label = self.label_create("USERNAME", 3, 0)
        self.label1 = self.label_create("PASSWORD", 4, 0)

        self.ent1 = self.ent_create(22, 5, 3, 1)
        self.ent2 = self.ent_create(22, 5, 4, 1)

        self.ent1.bind("<KeyRelease>", lambda event: self.non_emp_input())
        self.ent2.bind("<KeyRelease>", lambda event: self.non_emp_input())

        self.btn = Button(self.root, text="LOGIN", command=self.fuc1, bg="yellow", state=DISABLED, padx=12, pady=7)
        self.btn.grid(row=5, column=0, columnspan=5, padx=(12, 60), pady=12)

        self.btn1 = Button(self.root, text="Clear", command=self.clear_fields, bg="light blue", padx=12, pady=7)
        self.btn1.grid(row=5, column=1, columnspan=5, padx=(60, 12), pady=12)

    def label_create(self, text, row, column):
        label = Label(self.root, text=text, fg="black", padx=3)
        label.grid(row=row, column=column, sticky="w", padx=15, pady=25)
        return label

    def headingto_label(self, text, row, column, columnspan, font_size, padx_value):
        font_style = ("Times New Roman", font_size, "bold")
        head_label = Label(self.root, text=text, bg="blue", font=font_style, width=36, height=2, padx=padx_value,
                           pady=1)
        head_label.grid(row=row, column=column, columnspan=columnspan)
        head_label.place(x=20, y=20)
        return head_label

    def ent_create(self, width, borderwidth, row, column):
        ent = Entry(self.root, width=width, borderwidth=borderwidth, font=self.font_style, highlightthickness=2, \
                    highlightbackground="red")
        ent.grid(row=row, column=column, padx=15, pady=10, sticky="w")
        return ent

    def ent_create_password(self, width, borderwidth, row, column):
        ent = Entry(self.root, width=width, borderwidth=borderwidth, font=self.font_style, highlightthickness=2, \
                    highlightbackground="red", show="*")
        ent.grid(row=row, column=column, padx=15, pady=10, sticky="w")
        return ent

    def username_check(self):
        My_username = "gk"
        username = self.ent1.get()

        if username == My_username:
            return True
        else:
            return False

    def password_check(self):
        My_password = "******"
        password = self.ent2.get()

        if password == My_password:
            return True
        else:
            return False

    def btn_click(self):
        username = self.ent1.get()
        password = self.ent2.get()

    def non_emp_input(self):
        if self.ent1.get() and self.ent2.get():
            self.btn.config(state=NORMAL)
        else:
            self.btn.config(state=DISABLED)

    def fuc1(self):
        uc = self.username_check()
        pc = self.password_check()

        if uc and pc:
            self.root.withdraw()
            SecondaryGUI(self.root)
        else:
            messagebox.showerror("Incorrect username or password")

    def clear_fields(self):
        self.ent1.delete(0, END)
        self.ent2.delete(0, END)
        self.btn.config(state=DISABLED)


class SecondaryGUI:
    def __init__(self, root):
        self.root = root
        self.sec_gui1 = Toplevel(root)
        self.sec_gui1.title("FORM")
        self.sec_gui1.configure(bg="light blue")

        self.sec_gui1.rowconfigure(0, minsize=70)
        self.sec_gui1.rowconfigure(9, minsize=70)

        self.label1 = Label(self.sec_gui1, text="Full Name", font=("Arial", 12), fg="black", padx=5)
        self.label1.grid(row=0, column=0, padx=10, pady=15, sticky="w")

        self.entry1 = Entry(self.sec_gui1, font=("Arial", 12), highlightthickness=2, highlightbackground="red")
        self.entry1.grid(row=0, column=1, padx=20, pady=10)
        self.entry1.bind("<KeyRelease>", lambda event: self.validate_fields_and_mobile_number())

        self.label2 = Label(self.sec_gui1, text="Gender", font=("Arial", 12), fg="black", padx=5)
        self.label2.grid(row=1, column=0, padx=10, pady=15, sticky="w")

        self.male_var = IntVar(value=0)
        self.female_var = IntVar(value=0)

        Checkbutton(self.sec_gui1, text="Male", variable=self.male_var).grid(row=1, column=1, padx=15, pady=5,
                                                                             sticky="w")
        Checkbutton(self.sec_gui1, text="Female", variable=self.female_var).grid(row=2, column=1, padx=15, pady=5,
                                                                                 sticky="w")

        self.label3 = Label(self.sec_gui1, text="Age", font=("Arial", 12), fg="black", padx=5)
        self.label3.grid(row=4, column=0, padx=10, pady=15, sticky="w")

        self.entry3 = Entry(self.sec_gui1, font=("Arial", 12), highlightthickness=2, highlightbackground="red")
        self.entry3.grid(row=4, column=1, padx=20, pady=10)
        self.entry3.bind("<KeyRelease>", lambda event: self.validate_age())
        self.entry3.bind("<KeyRelease>", lambda event: self.validate_fields_and_mobile_number())

        self.label4 = Label(self.sec_gui1, text="Mobile Number", font=("Arial", 12), padx=5)
        self.label4.grid(row=6, column=0, padx=10, pady=15, sticky="w")

        self.entry4 = Entry(self.sec_gui1, font=("Arial", 12), highlightthickness=2, highlightbackground="red")
        self.entry4.grid(row=6, column=1, padx=20, pady=10)
        self.entry4.bind("<KeyRelease>", lambda event: self.validate_fields_and_mobile_number())

        self.label5 = Label(self.sec_gui1, text="City", font=("Arial", 12), padx=5)
        self.label5.grid(row=8, column=0, padx=10, pady=15, sticky="w")

        self.entry5 = Entry(self.sec_gui1, font=("Arial", 12), highlightthickness=2, highlightbackground="red")
        self.entry5.grid(row=8, column=1, padx=20, pady=10)
        self.entry5.bind("<KeyRelease>", lambda event: self.validate_fields_and_mobile_number())

        self.button = Button(self.sec_gui1, text="Submit", bg="yellow", state=DISABLED, padx=12, pady=7,
                             command=self.save_data)
        self.button.grid(row=9, column=0, columnspan=10, padx=30, pady=12)

        self.button1 = Button(self.sec_gui1, text="Clear", bg="red", command=self.clear_fields, padx=12, pady=7)
        self.button1.grid(row=9, column=1, columnspan=10, padx=30, pady=12)

        root_geometry = root.geometry()
        self.sec_gui1.geometry(root_geometry)
        self.sec_gui1.mainloop()

    def validate_age(self):
        age = self.entry3.get()

        if age.isdigit():
            self.button.config(state=NORMAL)
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid age (integer value only).")
            self.button.config(state=DISABLED)

    def validate_fields_and_mobile_number(self):
        full_name = self.entry1.get()
        age = self.entry3.get()
        mobile_number = self.entry4.get()
        city = self.entry5.get()

        if full_name and age and mobile_number and city:
            if len(mobile_number) == 10 and mobile_number.isdigit():
                self.button.config(state=NORMAL)
            else:
                self.button.config(state=DISABLED)
                messagebox.showerror("Invalid Input", "Please enter a valid 10-digit mobile number.")
        else:
            self.button.config(state=DISABLED)

    def clear_fields(self):
        self.entry1.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        self.button.config(state=DISABLED)

    def save_data(self):
        full_name = self.entry1.get()
        gender = "Male" if self.male_var.get() == 1 else "Female"
        age = self.entry3.get()
        mobile_number = self.entry4.get()
        city = self.entry5.get()

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="lucifer*7812",
            database=" form_data"
        )

        cursor = connection.cursor()

        insert_query = "INSERT INTO mytable (full_name, gender, age, mobile_number, city) VALUES (%s, %s, %s, %s, %s)"

        cursor.execute(insert_query, (full_name, gender, age, mobile_number, city))

        connection.commit()

        cursor.close()
        connection.close()

        messagebox.showinfo("Success", "Data saved successfully!")
        self.sec_gui1.destroy()


if __name__ == "__main__":
    root = Tk()
    login_form = LoginForm(root)
    root.mainloop()
