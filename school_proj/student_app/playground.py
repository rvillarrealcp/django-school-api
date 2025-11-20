from student_app.models import Student

new_student = Student(1, 'John W. Watson', 'johnnyBoy@school.com', 'johnnyBoy@gmail.com', 137, '37-68-98', True)
new_student.save()