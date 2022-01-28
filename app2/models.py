from django.db import models


# Create your models here.
from core.models import BaseModel


class Course(BaseModel):
    name = models.CharField(max_length=10)
    credit = models.IntegerField()


class StudentCourse(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    final_grade = models.IntegerField()
    mid_grade = models.IntegerField()


class Student(BaseModel):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    courses = models.ManyToManyField(Course, through=StudentCourse)


class Profile(BaseModel):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    total_credits = models.IntegerField()
    ...
