# Question_Bank.py
# Questions for quizzes
import random
elec2620_beginner = [
                        {"question" : "How to use a linux command is depicted in the following section of man page?",
                        "choices" : ["Options","Name","Synopsis","Description"],
                        "answer" : "Synopsis"},

                        {"question" : "Which of the following will not provide information about linux command?",
                        "choices" : ["whoami","whatis","man","None of the above"],
                        "answer" : "whoami"},

                        {"question" : "To save changes and exit vim, the following is not appropriate?",
                        "choices" : [":q!",":wq",":x","None of the above"],
                        "answer" : ":q!"}]
random.shuffle(elec2620_beginner)

elec2620_middle = [
                        {"question" : "What section of manpage will the execution of \"$man 5 passwd\" show? ",
                        "choices" : ["System command","File format","User command","Library command"],
                        "answer" : "File format"},

                        {"question" : "Which of the following may NOT be the output of \"$vim pass\"?",
                        "choices" : ["Create user password","Open pass file for editing","Create pass file","None of the above"],
                        "answer" : "Create user password"},

                        {"question" : "Which of the following command will make a script \"fly.sh\" executable by the owner?",
                        "choices" : ["chmod u+x fly.sh","chmod 755 fly.sh","chmod 744 fly.sh","All of the above"],
                        "answer" : "All of the above"}]
random.shuffle(elec2620_middle)
            
elec2620_advanced = [
                        {"question" : "What section of manpage will the execution of \"$man 5 passwd\" show? ",
                        "choices" : ["System command","User command","Library command", "File format"],
                        "answer" : "File format"},

                        {"question" : "Which of the following may NOT be the output of \"$vim pass\"?",
                        "choices" : ["Create user password","Open pass file for editing","Create pass file"],
                        "answer" : "Create user password"},

                        {"question" : "Which of the following command will make a script \"fly.sh\" executable by the owner?",
                        "choices" : ["chmod u+x fly.sh","chmod 755 fly.sh","chmod 744 fly.sh","All of the above"],
                        "answer" : "All of the above"}]
random.shuffle(elec2620_advanced)


comp2660_beginner = [
                        {"question": "Which of the following components is designed for data storage inside CPU?",
                        "choices": ["Accumulator", "Main Memory", "Register", "All of the choices"],
                        "answer": "Register"},
        
                        {"question": "Which of the following components performs storage after an arithmetic operaton inside ALU?",
                        "choices": ["Accumulator", "Memory address register", "Memory data register"],
                        "answer": "Accumulator"},
                        
                        {"question": "Which of the LMC instruction is the best describe if the LMC machine code is 301?",
                        "choices": ["BRA 01", "LDA 01", "STO 01", "None of the other choices"],
                        "answer": "STO 01"}]
random.shuffle(comp2660_beginner)

comp2660_middle = [
                        {"question": "Which of th following components provide the capability for moving data between components? ",
                        "choices": ["Data port", "Data bus", "Controller", "Read/Write Line"],
                        "answer": "Data bus"},
                        
                        {"question": "What is the LMC machine code for SUB 24?",
                        "choices": ["124", "224", "324", "524"],
                        "answer": "224"},
                        
                        {"question": "With the \"ADD XX\" instruction in LMC program, the content stored in ___________ will be added with the content stored in mailbox \"XX\" .",
                        "choices": ["accumulator", "instruction register", "memory address registor", "memory data registor"],
                        "answer": "accumulator"}]
random.shuffle(comp2660_middle)

comp2660_advanced = [
                        {"question": "Which of th following components provide the capability for moving data between components? ",
                        "choices": ["Controller", "Read/Write Line", "Data port", "Data bus"],
                        "answer": "Data bus"},
                        
                        {"question": "What is the LMC machine code for SUB 24?",
                        "choices": ["224","324","624","824"],
                        "answer": "224"},
                        
                        {"question": "Which of the LMC instruction is the best describe if the LMC machine code is 301?",
                        "choices": ["ADD 01","SUB 01","HLT","STO 01"],
                        "answer": "STO 01"}]
random.shuffle(comp2660_advanced)



comp1080_beginner = [
                        {"question": "Which symbol marks the beginning of comment in Python?",
                        "choices": ["&", "#", "**",],
                        "answer": "#"},
        
                        {"question": "The symbols >, <, and == are all _________ operators.",
                        "choices": ["Relational", "Logical", "Conditional", "Ternary"],
                        "answer": "Relational"},
                        
                        {"question": "Which of the following statements requires importing the math module beforhead?",
                        "choices": ["math.ceil(2.3)", "round(2.3)", "\"hi\" * 3"],
                        "answer": "math.ceil(2.3)"}]
random.shuffle(comp1080_beginner)

comp1080_middle = [
                        {"question": "Which of th following variable names are invalid in Python? ",
                        "choices": ["__value", "$total", "____", "var_2"],
                        "answer": "$total"},
                        
                        {"question": "Which description of the statement print(\"Hi\\t7\\n8\") is correct?",
                        "choices": ["The last character of the first line is 8", "Exactly 2 lines are printed", "The screen will literally show Hi\\t7\\n8", "None of the above"],
                        "answer": "Exactly 2 lines are printed"},
                        
                        {"question": "Which one is not a built-in data type in Python",
                        "choices": ["Integer", "Float", "String", "Character","Boolean"],
                        "answer": "Character"}]
random.shuffle(comp1080_middle)

comp1080_advanced = [
                        {"question": "The symbols >, <, and == are all _________ operators.",
                        "choices": ["Logical", "Conditional", "Ternary", "Relational", "Bitwise"],
                        "answer": "Relational"},
                        
                        {"question": "What is the output for the statement print(bool([])) ?",
                        "choices": ["True","False","None","An error"],
                        "answer": "False"},
                        
                        {"question": "How many arthmetic operators (+ - * / % // **) appear in the statement total = (a + 1) * 3 ** 2 // 4 - b % 2 ?",
                        "choices": ["4", "5","6","7","None of the above"],
                        "answer": "6"}]
random.shuffle(comp1080_advanced)



