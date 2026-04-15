# Account_Info.py
# Student's information
student_list = {"Max" : {"student_no":"12345678","password": "84bif023","phone_no":"13460839","courses":{"2620":"beginner","2660":"middle","1080":"advanced"},"practice":{"2620":[],"2660":[],"1080":[]},"score":{"2620":"No grading","2660":"No grading","1080":"No grading"}}
                ,"Tom" : {"student_no":"24681012","password":"4iod349","phone_no":"75039843","courses":{"2620":"middle","2660":"advanced","1080":"beginner"},"practice":{"2620":[],"2660":[],"1080":[]},"score":{"2620":"No grading","2660":"No grading","1080":"No grading"}}
                ,"Mia" : {"student_no":"13579111","password":"b5t675rf","phone_no":"62346364","courses":{"2620":"beginner","2660":"middle","1080":"advanced"},"practice":{"2620":[],"2660":[],"1080":[]},"score":{"2620":"No grading","2660":"No grading","1080":"No grading"}}}

student_studno = [s["student_no"] for s in student_list.values() if s and "student_no" in s]
student_password = [s["password"] for s in student_list.values() if s and "password" in s]
combine_student = dict(zip(student_studno,student_password))


# Teacher's information
teacher_list = {"White":{"teacher_no":"45637587","password":"n9844iw0","phone_no":"92348034","courses":["2620","1080"]},
                "James":{"teacher_no":"18393924","password":"i909ei4r","phone_no":"90384003","courses":["1080","2660"]},
                "Scott":{"teacher_no":"34820304","password":"849ru05t","phone_no":"60394540","courses":["2660","2620"]}}

teacher_name = list(teacher_list.keys())
teacher_accname = [t["teacher_no"] for t in teacher_list.values() if t and "teacher_no" in t]
teacher_password = [t["password"] for t in teacher_list.values() if t and "password" in t]
combine_teacher = dict(zip(teacher_accname,teacher_password))
