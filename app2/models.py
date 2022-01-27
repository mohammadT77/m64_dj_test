from django.db import models


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=10)
    credit = models.IntegerField()


class StudentCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    final_grade = models.IntegerField()
    mid_grade = models.IntegerField()


class Student(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    courses = models.ManyToManyField(Course, through=StudentCourse)


class Profile(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    total_credits = models.IntegerField()
    ...


