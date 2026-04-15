# Login.py
# A python file for Login Page and Default layout of the whole system
# import from Python library
import tkinter as tk
from tkinter import messagebox as msgbox
# import from the Python file Acconut_Info.py
from Account_Info import student_list, student_studno, combine_student, teacher_list, combine_teacher, teacher_accname
# Import from ABC for ABT
from abc import ABC, abstractmethod

# Some parent classes
# Default layout -- used in all classes
class DefaultLayout(ABC): 
    def __init__(self, main = None):
        if main == None:
            # Create another main application window
            self.window = tk.Tk()
        else:
            # Create a additional window which is separate from the main application window
            self.window = tk.Toplevel(main)
        
        # Add the GUI on top of the main page
        self.window.title("Educational System")
        #size of the screen
        self.window.geometry("750x500")
        # Set GUI backgroud to color #2F4156
        self.window.configure(bg="#2F4156")

    # Abstraction
    @abstractmethod
    def page_content(self):
        ...
        
    # To make run the GUI
    def run_page(self):
        self.page_content()
        self.window.mainloop()

# Home Page Layout -- used in StudentHomePage and TeacherHomePage
class HomePageLayout(ABC):

    # Details will be shown later
    def hide_switch(self,button, button_a, button_b):
        button.config(bg="white")
        button_a.config(bg="white")
        button_b.config(bg="white")
    
    # The button will turn blue to inform the user's current page
    # page is a function in this case
    def switch(self, button, page, button_a, button_b):
        self.hide_switch(button, button_a, button_b)
        button.config(bg="blue")
        page()

    # Clear the content of the previous page when the switch the page
    def clear_page(self):
        # winfo_childern() is used to get all widgets(buttons,labels,etc) under self.window
        for page in self.window.winfo_children():
            # except for widgets inside self.title_frame and self.options_frame
            if page not in [self.title_frame, self.options_frame]:
                # Destroy the current page content
                page.destroy()
    
    # Details will be shown later
    @abstractmethod
    def home_page(self):
        ...
    
    # Return to login page
    def return_login(self):
        # Destory home page
        self.window.destroy()
        # Active login page
        login_page = LoginPage()
        login_page.run_page()

# Quiz Layout -- used in QuizMode and QuizEdit
class QuizLayout(ABC):
    def back_question(self):
        # If the current question isn't the first question
        if self.current_question_no > 0:
            # Let current quesion number mines 1 in order to move to the previous question when passing the function load_question
            self.current_question_no -= 1
            # Back button available
            self.next_button.config(state = tk.NORMAL)
            # Active the function load_question()
            self.load_question()
            # If the current question is the first question 
            if self.current_question_no == 0:
                # Users are unable to click the back button
                self.back_button.config(state=tk.DISABLED)
            # Current question isn't the first question
            else:
                # Back button available
                self.back_button.config(state = tk.NORMAL)

    @abstractmethod
    def next_question(self):
        pass

    @abstractmethod
    def load_question(self):
        pass

# Child class
# A page for student and teacher to login
# Inheritance
class LoginPage(DefaultLayout):
    def __init__(self):
        # Inherit from DefaultLayout
        super().__init__()
        # To store user name
        self.actual_name = None
        # To see if the user want to show password
        self.__passwd_var = tk.BooleanVar()
    # Finish implementation from DefaultLayout
    def page_content(self):
        # Title of login page
        login_label = tk.Label(self.window, text="Login Page", font=("Verdana", 20, "bold"), bg="#2F4156", fg="white")
        # .pack() means to show the defined label,entry.button,etc.
        login_label.pack(pady=20)  

        # A label showing "Account no : "
        accno_label = tk.Label(self.window, text="Account no : ", bg="#2F4156", fg="white")
        accno_label.pack()

        # A entry for user to type their account number
        self.accno_enter = tk.Entry(self.window)
        self.accno_enter.pack() 

        # A label showing "Password : "
        passwd_label = tk.Label(self.window, text="Password : ", bg="#2F4156", fg="white")
        passwd_label.pack()      

        # A entry for user to type their password and the show text default is * so the password cannot be seen
        self.__password_enter = tk.Entry(self.window, show = "*")
        self.__password_enter.pack()
        
        # A checkbox for users who wants to show their password as what they typed
        self.show_password = tk.Checkbutton(self.window, text = "show password", variable = self.__passwd_var, command = self.password_show, bg="#2F4156", fg = "#6D9CBA")
        self.show_password.pack(pady = 10)

        # A button to confirm if the user typed their login information correctly
        login_button = tk.Button(self.window, text="Confirm", command=self.validation, bg="#567C8D", fg="white")
        login_button.pack()
    #command for the checkbox show_password
    def password_show(self):
        # If the user clicked the checkbox
        if self.__passwd_var.get() == True:
            # Show normal text
            self.__password_enter.config(show = "")
            # set the checkbox as clicked
            self.__passwd_var.set(1)
        else: # User didn't click the checkbox
            # Show "*" to replace typed password
            self.__password_enter.config(show = "*")
            # Set the checkbox as unclicked
            self.__passwd_var.set(0)
    #command for button login_button
    def validation(self):
        # Get the value typed in the entry for account number
        accno = self.accno_enter.get()
        # Get the value typed in the entry for password
        passwd = self.__password_enter.get()
        
        # If typed account number matches with one of the user name
        if accno in combine_student:
            # If the typed password is the password for the account number
            # {accno : passwd} <- this is a dictionary in acc_list
            if combine_student[accno] == passwd:
                # i is the index of the user information in the dictionary student_list
                for i in range(len(student_list) - 1):
                    # Get user name from the dictionary
                    if student_studno.index(accno) == i:
                        self.actual_name = list(student_list.keys())[i]
                        # Add a message box to inform the user that they have successfully logged in
                        msgbox.showinfo("Success", "Login Successful! Welcome " + self.actual_name + "!")
                        # Close the Login page GUI
                        self.window.destroy()
                        self.accno = student_list[self.actual_name]["student_no"]
                        self.phoneno = student_list[self.actual_name]["phone_no"]
                        # Import class 
                        from Student import StudentHomePage
                        home_page = StudentHomePage(self.actual_name, self.accno, self.phoneno)
                        # Show Student Home Page
                        home_page.page_content()
                        break
            else:
                msgbox.showinfo("Error", "Wrong account number or password, please try again")
    
        # Work the same as the above but in teacher version
        elif accno in teacher_accname:
            if combine_teacher[accno] == passwd:
                for i in range(len(teacher_list)):
                    if teacher_accname.index(accno) == i: 
                        self.actual_name = list(teacher_list.keys())[i]
                        msgbox.showinfo("Success", "Login Successful! Welcome Mr/Ms " + self.actual_name + "!")
                        self.window.destroy()
                        self.accno = teacher_list[self.actual_name]["teacher_no"]
                        self.phoneno = teacher_list[self.actual_name]["phone_no"]
                        from Teacher import TeacherHomePage
                        home_page = TeacherHomePage(self.actual_name, self.accno, self.phoneno)
                        home_page.page_content()
                        break
            else:
                msgbox.showinfo("Error", "Wrong account number or password, please try again")
                
        # A message box to show error
        else:
            msgbox.showinfo("Error", "Wrong account number or password, please try again")

# The program will work only if the user run it at this file
if __name__ == "__main__":
    a = LoginPage()
    a.run_page()