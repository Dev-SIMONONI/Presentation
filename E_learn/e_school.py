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
    all_students_details ={}
    subscribed_students = []
    def __init__(self, name, scope_of_study, total_courses, student: str):
        E_learning.__init__(self, name,scope_of_study,total_courses)
        self.student = student
        
        self.Login= False
        self.member=False
        self.student_courses =[]
        



    def checkPassword (self, password):
     password.strip()
     passLen = len(password)
     digit = False
     if passLen < 6:
          print("Weak password strength")
     elif passLen >= 6 and passLen <= 10:
          print("Medium password strength")
     elif passLen > 10:
          for char in password:
               if char.isdigit():
                    digit =True
                    break
     
     if digit == True:
          print("Strong password")
     else:
          print("Add number to password to make it strong")

     

    def create(self):
        print(f'''
             *----------------------------------------*
             |      {self.name}: REGISTER             |
             |________________________________________|
             

            ''')

        print("Enter all informations below to Register")
                
        while True:
            name = input("enter fullname >>> ")
            email=input("enter email address >>> ")
            password = input ("enter your password >>> ")
            if name.isalpha():
                break
            else:
                print("name should be only alphabetic letters try again")
                    
        self.checkPassword(password)
        School.total_student+=1
        School.all_students_details[name]={"name": name, "email": email, "password":password}
        print("Register sucessful login to access account")



    def login (self, name, password):
        print(f'''
             *----------------------------------------*
             |      {self.name}: LOGIN                |
             |________________________________________|
             

            ''')
        
        
        for details in School.all_students_details:
           if School.all_students_details[details]["name"] == name:
                if School.all_students_details[details]["password"] == password:
                    self.Login = True
                    break

        if self.Login: 
          print("Login sucessful")
          
        else:
            print("wrong details try again")
               

                       
    def subscribe(self, email: str):
        if self.Login == True:
            for mail in School.subscribed_students:
                if mail == email:
                    return "User already a member"
            
            School.subscribed_students.append(email)
            self.member =True
            
            return "subricption sucessful"
        else:
            print("Login to subscribe")

    

    def get_course(self, course: str):
        if self.Login == True:
            if self.member == True:
                for item in self.all_courses:
                
                    if item == course:
                        print(f"A Free full tutorial course on {course}")
                        self.student_courses.append(course)
                        return f"{course} Added to {self.student} catalogue"
                else:
                    return f"{course} not available in out courses catalogue"    

            else:
                return "Only members are allowed to get a course \nSubricipt to get membership access"
        else:
            print("Login to get a course")
              




