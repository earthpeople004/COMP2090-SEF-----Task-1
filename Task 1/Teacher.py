#Teacher.py
# Import modules
import tkinter as tk
from tkinter import messagebox as msgbox
# ttk allows more widget e.g.Combobox for QuizEdit
from tkinter import ttk
from Account_Info import student_list,teacher_list
from Question_Bank import elec2620_beginner,elec2620_middle,elec2620_advanced,comp2660_beginner,comp2660_middle,comp2660_advanced,comp1080_beginner,comp1080_middle,comp1080_advanced
from Login import DefaultLayout, HomePageLayout, QuizLayout

# Almost the same as StudentHomePage with slightly different content
class TeacherHomePage(DefaultLayout, HomePageLayout):
    def __init__(self,username, accno, phoneno):
        super().__init__()
        # refer to line 202 from Login.py
        self.username = username
        self.__accno = accno
        self.__phone_no = phoneno
        self.edit_course = teacher_list[self.username]["courses"]
    #Finish the implementation
    def page_content(self):
        self.title_frame = tk.Frame(self.window, bg="#2F4156")
        self.title_frame.pack()

        home_label = tk.Label(self.title_frame, text="Teacher's Home Page", font=("Verdana", 20, "bold"), bg="#2F4156", fg="white")
        home_label.pack(pady=10)

        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack(pady=5)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=750, height=25)

        self.home_button = tk.Button(self.options_frame, text="Home", command=lambda: self.switch(self.home_button,self.home_page, self.edit_button, self.studinfo_button))
        self.home_button.place(x=0, y=0, width=250)

        # Show a button with text Quiz Edit
        self.edit_button = tk.Button(self.options_frame, text="Quiz Edit", command=lambda: self.switch(self.edit_button,self.quizedit_page, self.home_button, self.studinfo_button))
        self.edit_button.place(x=250, y=0, width=250)
        # Show a button with text Student Level Adjustment
        self.studinfo_button = tk.Button(self.options_frame, text="Student Level Adjustment", command=lambda: self.switch(self.studinfo_button,self.studentinfo_page, self.home_button, self.edit_button))
        self.studinfo_button.place(x=500, y=0, width=250)

        # Home page is the default subpage 
        self.home_page()
    # Similar to quiz_page() in StudentHomePage with different label on the button
    def quizedit_page(self):
        self.clear_page()

        self.edit_frame = tk.Frame(self.window, bg="#2F4156")
        self.edit_frame.pack(pady=20)
        
        edit_label = tk.Label(self.edit_frame, text="Quiz Edit", font=("Times New Roman", 15), bg="#2F4156", fg="white")
        edit_label.pack(pady=10)
        
        # the buttons with relative courses will appear only if the teacher is in chage of the course
        if "2620" in self.edit_course:
            self.button_2620 = tk.Button(self.edit_frame, text="ELEC2620 SEF", command=lambda: self.quiz_edit("2620"), bg="#426E83", fg="white")
            self.button_2620.pack(pady=15)

        if "2660" in self.edit_course:
            self.button_2660 = tk.Button(self.edit_frame, text="COMP2660 SEF", command=lambda: self.quiz_edit("2660"), bg="#426E83", fg="white")
            self.button_2660.pack(pady=15)

        if "1080" in self.edit_course:
            self.button_1080 = tk.Button(self.edit_frame, text="COMP1080 SEF", command=lambda: self.quiz_edit("1080"), bg="#426E83", fg="white")
            self.button_1080.pack(pady=15)

    def quiz_edit(self,coursecode):
        #Move to quiz edit
        QuizEdit(self.window, coursecode)

    def diffadj(self,studname, code):
        # Move to level adjustment
        LevelAdjust(self.window, studname, code)
    # Similar to home_page() in StudentHomePage
    def home_page(self):
        self.clear_page()
        home_frame = tk.Frame(self.window,bg="#2F4156")
        home_frame.pack(pady=5)

        home_label = tk.Label(home_frame, text="Personal Information", font=("Times New Roman", 15), bg="#2F4156", fg="white")
        home_label.pack(pady=10)

        student_name_label = tk.Label(home_frame, text="Surname : " + self.username, bg="#2F4156", fg="white")
        student_name_label.pack(pady=10)

        self.teacher_info = teacher_list[self.username]
                
        teacher_no_label = tk.Label(home_frame, text="Teacher No: " + self.__accno, bg="#2F4156", fg="white") 
        teacher_no_label.pack(pady=5)
                
        teacher_phone_label = tk.Label(home_frame, text="Phone: " + self.__phone_no, bg="#2F4156", fg="white")
        teacher_phone_label.pack(pady=5)
                
        # Show enrolled courses
        courses_label = tk.Label(home_frame, text="Courses in Charge", bg="#2F4156", fg="#9FE7F9")
        courses_label.pack(pady=10)
                
        for course in self.teacher_info["courses"]:
            course_label = tk.Label(home_frame, text="Course : " + course, bg="#2F4156", fg="white")
            course_label.pack(pady=5)

        return_button = tk.Button(home_frame, text="Return to Login Page", command=self.return_login)
        return_button.pack(pady=10)
    
    def studentinfo_page(self):
        self.clear_page()
        self.stud_frame = tk.Frame(self.window, bg="#2F4156")
        self.stud_frame.pack(pady=20)
        # a list to store buttons
        self.stud_button = []
        
        diff_label = tk.Label(self.stud_frame, text = "Adjust level for :", font=("Times New Roman", 15), bg="#2F4156", fg="white")
        diff_label.pack(pady = 15)
        # name = studet's name(key), info = information(value) in student_list
        for name, info in student_list.items():
            for code in self.edit_course:
                # If the student studies the course that the teacher is in charge of 
                if code in info["courses"]:
                    # create a button with label "student's name : course code"
                    self.button = tk.Button(self.stud_frame, text = name + " : " + code, command = lambda n = name, c = code : self.diffadj(n, c))
                    self.button.pack(pady = 10)
                    # append to the button list
                    self.stud_button.append(self.button)

 # A page to edit the content of the quizzes   

# A page to edit quiz content
class QuizEdit(DefaultLayout, QuizLayout):
    def __init__(self, parent_window, coursecode):
        # inherited from DefaultLayout
        # in this case, a additional window will appear on top of the main application window(teacher page)
        super().__init__(main = parent_window)
        # page title
        self.window.title("Quiz Edit - " + coursecode)
        # page size
        self.window.geometry("705x600")

        # course code
        self.course = coursecode
        # current question number
        self.current_question_no = 0
        # Default display level
        self.level = "beginner"

        # Direct access to the data instead of editing the copies
        self.question_lists = {
                                "2620": {"beginner": elec2620_beginner,
                                        "middle": elec2620_middle,
                                        "advanced": elec2620_advanced},
                                
                                "2660": {"beginner": comp2660_beginner,
                                        "middle": comp2660_middle,
                                        "advanced": comp2660_advanced},
            
                                "1080": {"beginner": comp1080_beginner,
                                        "middle": comp1080_middle,
                                        "advanced": comp1080_advanced}
                                }
        
        # Get reference to current question list
        self.question = self.question_lists[self.course][self.level]

        # For editing
        # to store new choices
        self.choice_entries = []
        # to track the correct answer 
        self.answer_var = tk.StringVar()

        self.page_content()
        self.load_question()

    def hide_switch(self):
        # set the level button colour to #426E83 when the button wasn't being clicked
        self.button_b.config(bg="#426E83")
        self.button_m.config(bg="#426E83")
        self.button_a.config(bg="#426E83")
    
    def switch(self, button, level):
        self.hide_switch()
        # the level button chosen will turn blue
        button.config(bg="blue")
        # move to the first question whenever the teacher changes the level
        self.current_question_no = 0
        self.level = level
        # set question
        self.question = self.question_lists[self.course][self.level]
        self.load_question()

    def clear_page(self):
        # remove widget that are not under title_frame or options_frame when switch between questions
        for page in self.window.winfo_children():
            if page not in [self.title_frame, self.options_frame]:
                page.destroy()
        
    def page_content(self):
        self.title_frame = tk.Frame(self.window, bg="#2F4156")
        self.title_frame.pack()
        
        title_label = tk.Label(self.title_frame, text="Edit Questions for " + self.course,font=("Verdana", 16, "bold"), bg="#2F4156", fg="white")
        title_label.pack(pady=10)

        self.options_frame = tk.Frame(self.window)
        self.options_frame.pack(pady=5)
        self.options_frame.pack_propagate(False)
        self.options_frame.configure(width=705, height=25)
        # level buttons
        self.button_b = tk.Button(self.options_frame, text="Beginner", command=lambda: self.switch(self.button_b, "beginner"), bg="#426E83")
        self.button_b.place(x=0, y=0, width=235)

        self.button_m = tk.Button(self.options_frame, text="Middle", command=lambda: self.switch(self.button_m, "middle"), bg="#426E83")
        self.button_m.place(x=235, y=0, width=235)

        self.button_a = tk.Button(self.options_frame, text="Advanced", command=lambda: self.switch(self.button_a, "advanced"), bg="#426E83")
        self.button_a.place(x=470, y=0, width=235)

    def load_question(self):
        self.clear_page()

        self.edit_frame = tk.Frame(self.window, bg="#2F4156")
        self.edit_frame.pack(pady = 20, fill = tk.BOTH, expand = True)

        self.question_no_label = tk.Label(self.edit_frame, text = "Question " + str(self.current_question_no + 1) + " out of " + str(len(self.question)), bg="#2F4156", fg="white")
        self.question_no_label.pack(pady = 10, padx = 20, anchor = tk.W)

        self.question_label = tk.Label(self.edit_frame, text = "Question : ", bg="#2F4156", fg = "White")
        self.question_label.pack(padx = 10, pady = 10, anchor = tk.W)
        # Use text (multiple lines)  instead of entry (single line)
        #  allowing the question to have a longer length
        self.question_text = tk.Text(self.edit_frame, height = 4, width = 60, wrap = tk.WORD)
        self.question_text.pack(pady = 5, padx = 10, fill = tk.X)

        self.question_data = self.question[self.current_question_no]
        # insert the text in the question_text
        # 1.0 = line 1, character 0
        self.question_text.insert("1.0",self.question_data["question"])

        self.choice_label = tk.Label(self.edit_frame, text="Choices :", bg="#2F4156", fg="white")
        self.choice_label.pack(pady = 10, padx = 20, anchor=tk.W)

        self.choice_entries = []
        
        self.choice_frame = tk.Frame(self.edit_frame, bg="#2F4156")
        self.choice_frame.pack(pady = 10,padx = 20, fill=tk.X)

        self.choice_no = len(self.question_data["choices"])
        # add entry for existing choice in the question
        for i in range(len(self.question_data["choices"])):

            self.choice_frame_sm = tk.Frame(self.choice_frame, bg="#2F4156")
            self.choice_frame_sm.pack(pady = 5, fill = tk.X)

            choice_label = tk.Label(self.choice_frame_sm, text="Choice " + str(i + 1) + " : ", bg="#2F4156", fg="white", width = 10)
            choice_label.pack(side = tk.LEFT)

            self.choice_entry = tk.Entry(self.choice_frame_sm, width = 45)
            self.choice_entry.pack(side = tk.LEFT, padx = 5, fill = tk.X, expand = True)
            # insert the text in the first index (0) of the entry
            self.choice_entry.insert(0, self.question_data["choices"][i])

            self.choice_entries.append(self.choice_entry)

        self.answer_frame = tk.Frame(self.edit_frame, bg="#2F4156")
        self.answer_frame.pack(pady = 10, padx = 20, fill = tk.X)
        
        self.answer_label = tk.Label(self.answer_frame, text = "Answer : ", bg="#2F4156", fg = "white")
        self.answer_label.pack(side = tk.LEFT)
        # set the value for diaplaying in combobox
        self.answer_var = tk.StringVar(value = self.question_data["answer"])
        # only ttk supports combobox
        self.answer_combo = ttk.Combobox(self.answer_frame, textvariable=self.answer_var, values=self.question_data["choices"], width=47)
        self.answer_combo.pack(pady = 5, padx = 20)
        # Similar to QuizMode in Student.py
        self.button_frame = tk.Frame(self.window, bg="#2F4156")
        self.button_frame.pack(pady = 20)

        self.add_button = tk.Button(self.button_frame,text = "Add Choices",command = self.add_choice)
        self.add_button.pack(side = tk.LEFT, padx = 10)
        
        self.back_button = tk.Button(self.button_frame, text = "Back", command = self.back_question, bg="#567C8D", fg="white")
        self.back_button.pack(side = tk.LEFT, padx = 10)
        
        self.next_button = tk.Button(self.button_frame, text = "Next", command = self.next_question,bg = "#567C8D", fg="white")
        self.next_button.pack(side = tk.LEFT, padx = 10)

        self.save_button = tk.Button(self.button_frame,text = "Save Changes",command = self.save_changes)
        self.save_button.pack(side = tk.LEFT, padx = 10)

        # Update answer combo values when choices change
        for entry in self.choice_entries:
            # To Trigger the function self.update_answer_choices ever time the user presses the key
            entry.bind('<KeyRelease>', self.update_answer_choices)


    def update_answer_choices(self, event = None):
        current_choices = []
        for entry in self.choice_entries:
            ety = entry.get().strip()
            # Only add non empty choices to the combobox
            if ety != "":
                current_choices.append(ety)

        # Update dropdown list
        self.answer_combo['values'] = current_choices

    def add_choice(self):
        
        self.choice_frame_sm = tk.Frame(self.choice_frame, bg="#2F4156")
        self.choice_frame_sm.pack(pady = 5, fill = tk.X)

        choice_label = tk.Label(self.choice_frame_sm, text="Choice " + str(self.choice_no + 1) + " : ", bg="#2F4156", fg="white", width = 10)
        choice_label.pack(side = tk.LEFT)

        self.choice_entry = tk.Entry(self.choice_frame_sm, width = 45)
        self.choice_entry.pack(side = tk.LEFT, padx = 5, fill = tk.X, expand = True)
        # add a empty entry for a new choice
        self.choice_entry.insert(0, "")
        # append the list
        self.choice_entries.append(self.choice_entry)

        for entry in self.choice_entries:
            # To Trigger the function self.update_answer_choices ever time the user presses the key
            entry.bind('<KeyRelease>', self.update_answer_choices)
        
        self.choice_no += 1

    # works the same as QuizMode from Student.py
    def next_question(self):
        if self.current_question_no < len(self.question) - 1:
            self.current_question_no += 1
            self.back_button.config(state = tk.NORMAL)
            self.load_question()
        
            if self.current_question_no == len(self.question) - 1:
                self.next_button.config(state = tk.DISABLED)
            else:
                self.next_button.config(state = tk.NORMAL)

    def save_changes(self):
        # "1" refers to the first row and " .0 " refers to the zeroth character
        # ("1.0" <- starting index, tk.END <- ending index)
        new_question = self.question_text.get("1.0", tk.END).strip()

        new_choices = []
        for entry in self.choice_entries:
            new = entry.get().strip()
            if new != "" :
                new_choices.append(new)

        # new correct answer will be the answer selected in the combobox
        new_answer = self.answer_var.get().strip()

        # if question entry field is empty
        if new_question == "":
            # warn the teacher by a message box
            msgbox.showwarning("Warning", "Question cannot be empty!")
            return
        
        # Update the question in the bank
        self.question[self.current_question_no] = {
                                                    "question": new_question,
                                                    "choices": new_choices,
                                                    "answer": new_answer
                                                                        }
        # a message box to inform the user teacher that they have successfully editted the question
        msgbox.showinfo("Success","Question " + str(self.current_question_no + 1) + " has been updated successfully!")
        
        # Refresh the display
        self.load_question()

# A page to change student's quiz difficulty
class LevelAdjust(DefaultLayout):
    def __init__(self, parent_window, studname, code):
        # Create a additional window which is separate from the main application window
        super().__init__(main = parent_window)
        # studname = student's name
        self.window.title("Difficulty Adjust - " + studname)
        # Size of screen
        self.window.geometry("600x300")

        # Get the course code
        self.course = code
        # Get student's name
        self.studname = studname
        # Get student's current difficulty
        self.level = student_list[self.studname]["courses"][self.course]
        # Get student's current score on their difficulty
        self.score = str(student_list[self.studname]["score"][self.course])
        
        # Set StringVar() to hold string data from the buttons
        # self.btn_var has no initial string 
        self.btn_var = tk.StringVar()
        # Active the function self.page_content()
        self.page_content()

    def page_content(self):
        # showing labels
        self.current_label = tk.Label(self.window, text = "Current level of " + self.studname + " : " + self.level, font=("Times New Roman", 15), bg="#2F4156")
        self.current_label.pack(pady = 15)

        self.score_label = tk.Label(self.window, text = "Current score : "+ self.score, font=("Times New Roman", 15), bg="#2F4156")
        self.score_label.pack(pady = 15)

        self.adjust_label = tk.Label(self.window, text = "Which level do you want to change to?", bg="#2F4156")
        self.adjust_label.pack(pady = 15)
        
        # A button frame
        self.button_frame = tk.Frame(self.window, bg="#2F4156")
        self.button_frame.pack()
        
        # showing buttons under a button frame
        self.button_b = tk.Button(self.button_frame, text = "Beginner", command = lambda : self.adjusted("beginner"))
        self.button_b.pack(side = tk.LEFT, padx = 20)

        self.button_m = tk.Button(self.button_frame, text = "Middle", command = lambda : self.adjusted("middle"))
        self.button_m.pack(side = tk.LEFT, padx = 20)

        self.button_a = tk.Button(self.button_frame, text = "Advanced", command = lambda : self.adjusted("advanced"))
        self.button_a.pack(side = tk.LEFT, padx = 20)

    def adjusted(self, level):
        # get the value(level) from the button
        self.btn_var.set(level)
        if self.btn_var.get() == "beginner":
            # change course difficulty to beginner based on the course
            student_list[self.studname]["courses"][self.course] = "beginner"
            # change course difficulty to middle based on the course
        elif self.btn_var.get() == "middle":
            student_list[self.studname]["courses"][self.course] = "middle"
            # change course difficulty to advanced based on the course
        elif self.btn_var.get() == "advanced":
            student_list[self.studname]["courses"][self.course] = "advanced"
        
        # a message box to inform the teacher that the level has benn changed successfully
        msgbox.showinfo("Adjusted Successfully","Level of " + self.studname + " has changed from " + self.level + " to " + student_list[self.studname]["courses"][self.course])
        self.window.destroy()