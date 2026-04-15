# Import modules
import tkinter as tk
from tkinter import messagebox as msgbox
from Account_Info import student_list
from Question_Bank import elec2620_beginner,elec2620_middle,elec2620_advanced,comp2660_beginner,comp2660_middle,comp2660_advanced,comp1080_beginner,comp1080_middle,comp1080_advanced
from Login import DefaultLayout, HomePageLayout, QuizLayout

# Student home page
class StudentHomePage(DefaultLayout, HomePageLayout):
    def __init__(self, username, account_no, phone_no):
        #Inherit from DafaultLayout 
        super().__init__()
        # To get the information from the Login page (refer to line 184 in Login.py)
        self.username = username
        self.__account_no = account_no
        self.__phone_no = phone_no
    #Finish the implementation
    def page_content(self):
        # Frame of the title
        self.title_frame = tk.Frame(self.window, bg="#2F4156")
        self.title_frame.pack()

        # Home label showed on the tile frame
        home_label = tk.Label(self.title_frame, text="Student's Home Page", font=("Verdana", 20, "bold"), bg="#2F4156", fg="white")
        home_label.pack(pady=10)

        # Set a frame for buttons that s used to switch between pages
        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack(pady=5)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=750, height=25)

        # A home button to switch to home page
        self.home_button = tk.Button(self.options_frame, text="Home", command=lambda: self.switch(self.home_button, self.home_page, self.quiz_button, self.practice_button))
        self.home_button.place(x=0, y=0, width=250)

        # A quiz button to switch to quiz page
        self.quiz_button = tk.Button(self.options_frame, text="Quiz", command=lambda: self.switch(self.quiz_button, self.quiz_page, self.home_button, self.practice_button))
        self.quiz_button.place(x=250, y=0, width=250)

        # A practice button to switch to practice page
        self.practice_button = tk.Button(self.options_frame, text="Practice", command=lambda: self.switch(self.practice_button, self.practice_page, self.home_button, self.quiz_button))
        self.practice_button.place(x=500, y=0, width=250)

        # Set home page as default
        self.home_page()
    #command foe quiz_button
    # A page that allows students to choose the course they want to work on
    def quiz_page(self):
        # Remove content of the previous page
        self.clear_page()

        # A frame that can be removed when switching page
        self.quiz_frame = tk.Frame(self.window, bg="#2F4156")
        self.quiz_frame.pack(pady=20)
        
        # Quiz label
        quiz_label = tk.Label(self.quiz_frame, text="Quiz Selection", font=("Times New Roman", 15), bg="#2F4156", fg="white")
        quiz_label.pack(pady=10)
        
        # Get student's registered course
        self.__student_course = student_list[self.username]["courses"]
        
        # Show ELEC26260 SEF button if the student registered this course
        if "2620" in self.__student_course:
            self.button_2620 = tk.Button(self.quiz_frame, text="ELEC2620 SEF", command=lambda: self.quiz_start("2620", self.username), bg="#426E83", fg="white")
            self.button_2620.pack(pady=15)

        # Show COMP2660 SEF button if the student registered this course
        if "2660" in self.__student_course:
            self.button_2660 = tk.Button(self.quiz_frame, text="COMP2660 SEF", command=lambda: self.quiz_start("2660", self.username), bg="#426E83", fg="white")
            self.button_2660.pack(pady=15)

        # Show COMP1080 SEF button if the student registered this course
        if "1080" in self.__student_course:
            self.button_1080 = tk.Button(self.quiz_frame, text="COMP1080 SEF", command=lambda: self.quiz_start("1080", self.username), bg="#426E83", fg="white")
            self.button_1080.pack(pady=15)

    # Move to the quiz of the student pressed of the buttons (ELEC2620 SEF, COMP2660 SEF, or COMP1080 SEF)
    def quiz_start(self, course_no, username):
        # To get student's level of the course
        self.student_level = student_list[self.username]["courses"].get(course_no)
        QuizMode(self.window, course_no, self.student_level, username)
    #command for home_button
    # A home page that show's student's information
    def home_page(self):
        # Clear previous page
        self.clear_page()
        # Create home frame 
        home_frame = tk.Frame(self.window,bg="#2F4156")
        home_frame.pack(pady=5)
        # Create a label with text Personal Information
        home_label = tk.Label(home_frame, text="Personal Information", font=("Times New Roman", 15), bg="#2F4156", fg="white")
        home_label.pack(pady=10)
        # Create a label with text Name
        student_name_label = tk.Label(home_frame, text="Name : " + self.username, bg="#2F4156", fg="white")
        student_name_label.pack(pady=10)
        # Create a label with text Student No
        student_no_label = tk.Label(home_frame, text="Student No: " + self.__account_no, bg="#2F4156", fg="white") 
        student_no_label.pack(pady=5)
        # Create a label with text Phone   
        student_phone_label = tk.Label(home_frame, text="Phone: " + self.__phone_no, bg="#2F4156", fg="white")
        student_phone_label.pack(pady=5)
        # Create a label with text Enrolled Courses
        courses_label = tk.Label(home_frame, text="Enrolled Courses", bg="#2F4156", fg="#9FE7F9")
        courses_label.pack(pady=10)
        # In student_list, take student Max as an example,
        #"Max" : {...,"courses":{"2620":"beginner","2660":"middle","1080":"advanced"},...}
        #                        course:level
        for course, level in student_list[self.username]["courses"].items():
            course_label = tk.Label(home_frame, text=course + " : " + level, bg="#2F4156", fg="white")
            course_label.pack(pady=5)
        # Create a button to return to home page
        # The function self.return_login is in class HomePageLayout
        return_button = tk.Button(home_frame, text="Return to Login Page", command = self.return_login)
        return_button.pack(pady=10)
    #command for the button practice_button
    # A page that allows student to choose the practice 
    # Like an error log
    def practice_page(self):
        self.clear_page()
        # A frame for widget in this practice page
        practice_frame = tk.Frame(self.window, bg="#2F4156")
        practice_frame.pack(pady=5)
        # A label 
        practice_label = tk.Label(practice_frame, text="Practice Selection", font=("Times New Roman", 15), bg="#2F4156", fg="white")
        practice_label.pack(pady=10)
        # To know what course did the student have
        self.__student_course = student_list[self.username]["courses"]

        # If the student have these courses 
        if "2620" in self.__student_course:
            self.button_2620 = tk.Button(practice_frame, text="ELEC2620 SEF", command = lambda: self.practice_start("2620", self.username), bg="#426E83", fg="white")
            self.button_2620.pack(pady=15)

        if "2660" in self.__student_course:
            self.button_2660 = tk.Button(practice_frame, text="COMP2660 SEF", command=lambda: self.practice_start("2660", self.username), bg="#426E83", fg="white")
            self.button_2660.pack(pady=15)

        if "1080" in self.__student_course:
            self.button_1080 = tk.Button(practice_frame, text="COMP1080 SEF", command=lambda: self.practice_start("1080", self.username), bg="#426E83", fg="white")
            self.button_1080.pack(pady=15)

    #Move to Practice Mode
    def practice_start(self, coursecode, username):
        # if there are questions saved into the preactice
        if student_list[self.username]["practice"][coursecode] != []:
            PracticeMode(self.window, coursecode, username)
        else:# if there is no question saved into the practice
            msgbox.showinfo("Error", "No practice questions in this course, please finish the quiz before you come!")

class QuizMode(DefaultLayout, QuizLayout):
    def __init__(self, parent_window, coursecode, level, username):
        # Call main constructor with parent_window to create Toplevel
        super().__init__(main = parent_window)
        self.window.title("Quiz Mode - " + coursecode)
        self.window.geometry("600x550")
        # The current question is the question at index 0 in the list
        self.current_question_no = 0
        # No score was gained by the student yet
        self.__score = 0
        # refer to line 83 of this Python file
        self.username = username
        self.course = coursecode
        self.level = level
        # To store student's choices
        self.__user_ans = []
        # for record if the student clicked on the checkbox
        self.check_var = tk.IntVar(value=0)
        # To prevent the user from saving the same question twice
        self.saved_success = False
        # Get questions from question bank
        self.question = self.get_course()
        
        # Setup UI and load first question
        self.page_content()
        self.load_question()
    # Finish the implementation
    def page_content(self):
        # Title frame
        self.title_frame = tk.Frame(self.window, bg="#2F4156")
        self.title_frame.pack(pady=10)
        
        quiz_label = tk.Label(self.title_frame, text="Quiz on " + self.course,font=("Verdana", 16, "bold"), bg="#2F4156", fg="white")
        quiz_label.pack()
        
        # Main quiz frame
        self.quiz_frame = tk.Frame(self.window, bg="#2F4156")
        self.quiz_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        # Question number
        self.question_no = tk.Label(self.quiz_frame, text="", font=("Arial", 12),bg="#2F4156", fg="white")
        self.question_no.pack(pady=5)
        
        # Question label
        self.question_text = tk.Label(self.quiz_frame, text="", font=("Arial", 12),bg="#2F4156", fg="white", wraplength=500)
        self.question_text.pack(pady=20)
        
        # Choice frame for buttons
        self.choice_frame = tk.Frame(self.quiz_frame, bg="#2F4156")
        self.choice_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        # Button frame for navigation
        self.button_frame = tk.Frame(self.window, bg="#2F4156")
        self.button_frame.pack(pady=20)
        
        self.back_button = tk.Button(self.button_frame, text = "Back", command = self.back_question,state = tk.DISABLED, bg="#567C8D", fg="white")
        self.back_button.pack(side=tk.LEFT, padx=10)
        
        self.next_button = tk.Button(self.button_frame, text = "Next", command = self.next_question,bg = "#567C8D", fg="white")
        self.next_button.pack(side=tk.LEFT, padx=10)
        
        self.submit_button = tk.Button(self.button_frame, text = "Submit", command = self.submit_quiz,bg = "light blue", fg="white")
        self.submit_button.pack(side=tk.LEFT, padx=10)

        self.quiz_checkbox = tk.Checkbutton(self.quiz_frame, text = "Add to Practice", variable = self.check_var, command = self.save_quiz_quest, bg="#2F4156")
        self.quiz_checkbox.pack(padx = 20)

        self.checkbox_state = tk.Label(self.quiz_frame, text = "", bg="#2F4156")
        self.checkbox_state.pack()
    # To determine which quiz question should the student do
    def get_course(self):
        # reffering to the student_list in Account_Info.py
        if self.course == "2620":
            if self.level == "beginner":
                # return the suitable quiz question
                return elec2620_beginner
            elif self.level == "middle":
                return elec2620_middle
            else:
                return elec2620_advanced
            
        elif self.course == "2660":
            if self.level == "beginner":
                return comp2660_beginner
            elif self.level == "middle":
                return comp2660_middle
            else:
                return comp2660_advanced
        
        elif self.course == "1080":
            if self.level == "beginner":
                return comp1080_beginner
            elif self.level == "middle":
                return comp1080_middle
            else:
                return comp1080_advanced
     
    def load_question(self):
        # Remove previous widget under choice_frame
        for widget in self.choice_frame.winfo_children():
            widget.destroy()

        # To store choice buttons
        self.choice_buttons = []
        
        #get one question from the list
        #if self.current_question_no < len(self.question):
        self.question_data = self.question[self.current_question_no]

        # Replace the text in question_no and question_text from "" 
        self.question_no.config(text="Question " + str(self.current_question_no + 1) + " of " + " " + str(len(self.question)))
        self.question_text.config(text = self.question_data["question"])
            
        
        #i = index number, choice = selections in text
        for i, choice in enumerate(self.question_data["choices"]):
            # Create button for each choice
            btn = tk.Button(self.choice_frame,text=choice,bg="#426E83",fg="white",font=("Arial", 10),wraplength=450,command=lambda idx=i, ans=choice: self.save_answer(idx, ans))
            btn.pack(fill=tk.X, pady=5, padx=20)
            # append the choice buttons into the list choice_buttons
            self.choice_buttons.append(btn)
                
            # Highlight previously selected answer
            if self.current_question_no < len(self.__user_ans):
                if self.__user_ans[self.current_question_no] == choice:
                    btn.config(bg="green")
        # active the function that show checkbox_state
        self.checkbox_state_update()
     
    def checkbox_state_update(self):
        # If the current question has been saved
        if self.question_data in student_list[self.username]["practice"][self.course]:
            self.check_var.set(1)
            self.checkbox_state.config(text = "Question saved")
        else:
            self.check_var.set(0)
            self.checkbox_state.config(text = "")
    
    # command of the checkbox quiz_checkbox
    def save_quiz_quest(self):
        # if the user active the checkbox
        if self.check_var.get() == 1:
            # if the question hasn't been saved before
            if self.question_data not in student_list[self.username]["practice"][self.course]:
                # save the question to the student_list
                student_list[self.username]["practice"][self.course].append(self.question_data)
                # Update the checkbox label
                self.checkbox_state.config(text = "Question saved")

            else:
                # if question has been saved before
               self.checkbox_state.config(text = "Question has already been saved")
        # if the user clicked on the checkbox when the checkbox has already been actived
        else:
            # if the question is being stored in student_list
            if self.question_data in student_list[self.username]["practice"][self.course]:
                # remove the question from student_list
                student_list[self.username]["practice"][self.course].remove(self.question_data)
                self.checkbox_state.config(text = "Question removed")
        
        # the message after clicking the checkbox will disappear after 3 seconds
        self.window.after(3000, lambda : self.checkbox_state_update())
    
    # to save the choices selected by the user before sumbitting the quiz
    def save_answer(self, idx, answer):
        # Reset all buttons to default color
        for btn in self.choice_buttons:
            btn.config(bg="#426E83")

        # Highlight the selected button
        if idx < len(self.choice_buttons):
            self.choice_buttons[idx].config(bg="green")
        
        # Save the answer to the list __user_ans
        # if the length of the list is smaller than or equals to the current question number
        if self.current_question_no >= len(self.__user_ans):
            # add the current choices to the list
            self.__user_ans.append(answer)
        else:
            # replace the previous choices to the current one
            self.__user_ans[self.current_question_no] = answer
    
    # command of the button next_button
    # finish the implementation of QuizLayout
    def next_question(self):
        # If the current question is not the first question
        if self.current_question_no < len(self.question) - 1:
            self.current_question_no += 1
            self.back_button.config(state = tk.NORMAL)
            self.load_question()
            # If the current question is the last question
            if self.current_question_no == len(self.question) - 1:
                self.next_button.config(state = tk.DISABLED)
            else: #if not
                self.next_button.config(state = tk.NORMAL)
    # command for the button sumbit_button  
    def submit_quiz(self):
        # Check if last question is answered
        # If not :
        if self.current_question_no >= len(self.__user_ans):
            msgbox.showwarning("Warning", "Please finish the quiz in order to submit it.")
            return
        
        # i = index of the list question, question = questions return in get_course
        for i, question in enumerate(self.question):
            #if i < len(self.__user_ans) and 
            if self.__user_ans[i] == question["answer"]:
                self.__score += 1
            #else save to error log
            else:
                # if the question hasn't been saved with the checkbox
                if question not in student_list[self.username]["practice"][self.course]:
                    # save the question to student_list
                    student_list[self.username]["practice"][self.course].append(question)
        
        # Show results
        self.percentage = round((self.__score / len(self.question)) * 100, 2)
        
        # Create detailed result message
        # if the student score between 40 and 60
        if self.percentage >=40 and self.percentage < 60 :
            comment = "\nYou can do better! Work harder next time!"
        # if the student score less than 40
        elif self.percentage < 40:
            comment = "\nPlease work hard on this course, you may fail the course if your score is lower than the passing mark."
        # if the student score between 60 and 99
        elif self.percentage >= 60 and self.percentage <= 99:
            comment = "\nGood job! Keep it up!"
        # if the student gets full marks
        else:
            comment = "\nExcellent performance!!"
        # save student's score to student_list
        student_list[self.username]["score"][self.course] = self.percentage
        # a message box to show student's result
        msgbox.showinfo("Quiz Complete","Your scored " + str(self.__score) + " out of " + str(len(self.question)) + " " + comment)
        # close the current window after closing the message box
        self.window.destroy()

class PracticeMode(DefaultLayout):
    def __init__(self, parent_window, coursecode, username):
        # Call main constructor with parent_window to create Toplevel
        super().__init__(main = parent_window)
        self.window.title("Practice Mode - " + coursecode)
        self.window.geometry("600x550")

        # Source code and user name will be the information from line 148
        self.coursecode = coursecode
        self.username = username
        # get question from the list student_list
        self.practice = student_list[self.username]["practice"][self.coursecode]
        # call functions
        self.page_content()
        self.load_question()
    # Similar to page_content() in QuizMode but without back_button
    def page_content(self):
        self.title_frame = tk.Frame(self.window, bg="#2F4156")
        self.title_frame.pack(pady=10)
        
        practice_label = tk.Label(self.title_frame, text="Practice on " + self.coursecode, font=("Verdana", 16, "bold"), bg="#2F4156", fg="white")
        practice_label.pack()

        self.practice_frame = tk.Frame(self.window, bg="#2F4156")
        self.practice_frame.pack(pady=20, fill=tk.BOTH, expand=True)
        
        # Question number
        self.question_no = tk.Label(self.practice_frame, text="", font=("Arial", 12),bg="#2F4156", fg="white")
        self.question_no.pack(pady=5)
        
        # Question label
        self.question_text = tk.Label(self.practice_frame, text="", font=("Arial", 12),bg="#2F4156", fg="white", wraplength=500)
        self.question_text.pack(pady=20)
        
        # Choice frame for buttons
        self.choice_frame = tk.Frame(self.practice_frame, bg="#2F4156")
        self.choice_frame.pack(pady=10, fill=tk.BOTH, expand=True)
        
        self.check_ans_label = tk.Label(self.practice_frame, bg="#2F4156")
        self.check_ans_label.pack(pady = 5)
        # Button frame for navigation
        self.button_frame = tk.Frame(self.window, bg="#2F4156")
        self.button_frame.pack(pady=20)
        
        self.next_button = tk.Button(self.button_frame, text = "Next", command = self.next_question,bg = "#567C8D", fg="white")
        self.next_button.pack(side=tk.LEFT, padx=10)

    #first in first out
    def load_question(self):
        # Remove previous choice buttons
        for widget in self.choice_frame.winfo_children():
            widget.destroy()
        # students are not allowed to move on before the answered the current question correctly
        self.next_button.config(state = tk.DISABLED)
        
        #get one question from the list
        #if self.current_question_no < len(self.question):
        self.practice_data = self.practice[0]
        # Replace the text in question_no and question_text from "" 
        self.question_no.config(text=str(len(self.practice)) + " questions remaining")
        self.question_text.config(text = self.practice_data["question"])
            
        # Create button for each choice
        self.choice_btn = []
        for i, choice in enumerate(self.practice_data["choices"]):
            # create choice buttons for each choices
            btn = tk.Button(self.choice_frame,text=choice,bg="#426E83",fg="white",font=("Arial", 10),wraplength=450,command = lambda idx = i, ans = choice : self.check_ans(idx,ans))
            btn.pack(fill=tk.X, pady=5, padx=20)
            # add choice buttons to the list
            self.choice_btn.append(btn)
    # command for the button btn 
    def check_ans(self, button_idx, select_choice):
        # refer to line 458
        self.button_idx = button_idx
        self.select_choice = select_choice
        # if the student answered the question correctly
        if self.select_choice == self.practice_data["answer"]:
            self.check_ans_label.config(text = "Correct!")
            # selected button turn green
            self.choice_btn[self.button_idx].config(bg="green")
            # the next_button becomes available
            self.next_button.config(state = tk.NORMAL)
                
        else: # if the student answered the question incorrectly
            # the selected turn red and student cannot interact with the button
            self.choice_btn[self.button_idx].config(bg="red",state = tk.DISABLED)
            self.check_ans_label.config(text = "Try again!")

    # command of the button next_button
    # finish the implementation of QuizLayout
    def next_question(self):
        # remove the current question from the list
        student_list[self.username]["practice"][self.coursecode].remove(self.practice_data)
        # if the student answered all questions in the practice
        if student_list[self.username]["practice"][self.coursecode] == []:
            msgbox.showinfo("Done!", "You have finished all practice questions! Hope you can get enough practice before the next quiz!")
            #close the practice window
            self.window.destroy()

        else: # if not
            # continue the practice
            self.practice = student_list[self.username]["practice"][self.coursecode]
            self.load_question()

