
from django.db import models
from django.utils import timezone

from django.contrib import admin


BACHLOAR_DEGREE = "Bachloar"
MASTER_DEGREE = "Master"

LEVEL = (
    # (LEVEL_COURSE, "Level course"),
    (BACHLOAR_DEGREE, "Bachloar Degree"),
    (MASTER_DEGREE, "Master Degree"),
)


class Pdftool(models.Model):
    author=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    text=models.TextField()

  
class Lyra(models.Model):
    title = models.CharField(max_length=20)
    Name = models.CharField(max_length=20)
    RegNo = models.CharField(max_length=20)
    Department = models.CharField(max_length=20)
    Grade = models.CharField(max_length=20)
    


from django.db import models




class Student(models.Model):
    name = models.CharField(max_length=100, default='None')
    email = models.EmailField(max_length=254, default='null')
    date_of_birth = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=20, default='null')
    name = models.CharField(max_length=100)
    course_id = models.CharField(max_length=10, default='null')
    course_name = models.CharField(max_length=100, default='null')
    course_grade = models.CharField(max_length=10, default='null')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.course_name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)



    def __str__(self):
        return f"{self.student.name} enrolled in {self.course.title}"

