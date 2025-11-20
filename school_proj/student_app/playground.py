from student_app.models import Student

new_student = Student(name='John W. Watson', student_email='johnnyBoy@school.com', personal_email='johnnyBoy@gmail.com', locker_number=137, locker_combination='37-68-98', good_student=True)
new_student.save()