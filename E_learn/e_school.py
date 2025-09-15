class E_learning:
    total_school = 0
    def __init__(self, name: str, scope_of_study: str, all_courses: list):

        self.name =name
        self.scope_of_study = scope_of_study
        self.total_courses = len(all_courses)
        self.all_courses =all_courses
        E_learning.total_school+=1



class School(E_learning):
    total_student =0
    all_students_email =[]
    def __init__(self, name, scope_of_study, total_courses, student: str):
        E_learning.__init__(self, name,scope_of_study,total_courses)
        self.student = student
        
        
        self.member=False
        self.student_courses =[]

    def subscribe(self, email: str):
        
        for mail in School.all_students_email:
            if mail == email:
                return "User already a member"
            
        School.all_students_email.append(email)
        self.member =True
        School.total_student+=1
        return "subricption sucessful"
    
    
    def get_course(self, course: str):
        if self.member == True:
            for item in self.all_courses:
                
                if course == item:
                   print(f"A Free full tutorial course on {course}")
                   self.student_courses.append(course)
                   return f"{course} Added to {self.student} catalogue"
            else:
                return f"{course} not available in out courses catalogue"    

        else:
            return "Only members are allowed to get a course \nSubricipt to get membership access"
              




