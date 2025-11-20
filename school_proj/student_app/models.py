from django.db import models

class Student(models.Model):
    name:str = models.CharField(max_length=100, blank=False, null=False, unique=False)
    student_email:str = models.EmailField(blank=False, null=False, unique=True)
    personal_email:str = models.EmailField(unique=True)
    locker_number:int = models.IntegerField(blank=False, null=False, unique=True, default=110)
    locker_combination:str = models.CharField(blank=False, null=False, unique=False, default='12-12-12')
    good_student:bool = models.BooleanField(blank=False, null=False, unique=False, default=True)

# Create your models here.
    def __str__(self):
        return f'{self.name}-{self.student_email}-{self.locker_number}'
    
    def locker_reassignment(self, new_num:int):
        self.locker_number = new_num
        self.save()
    
    def student_status(self, honors:bool):
        self.good_student = honors
        self.save()