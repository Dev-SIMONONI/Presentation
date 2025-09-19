from e_school import E_learning, School

udemy=School("Udemy", "Full-stack developer",["Python3","Java Script", "Rust", "Html","Css"],"Klaus")
free = School("Freecode","Cloud computing",["clod","security"], "sasuke" )


#udemy.create()
#udemy.login("stephen", "onlythefamily1")
#print(udemy.subscribe("simon@gmail.com"))
#print(udemy.get_course("Rust"))

print("*************************************************************")

free.create()
free.login("sasuke", "otf4real")
print(free.subscribe("sasuke@gmail.com"))
print(free.get_course("security"))
print()

print("*************************************************************")

print(udemy.total_student) 
print(udemy.all_students_details)
print(udemy.subscribed_students)


print(udemy.total_school)
