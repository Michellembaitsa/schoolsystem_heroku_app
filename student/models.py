from django.db import models
import datetime

# from django.db.models.enums import Choices

# Create your models here.
class Student(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    age=models.PositiveSmallIntegerField()
    gender_choices=(
        ('F','Female'),
        ('M','Male'),
        ('O','Other'))
    gender=models.CharField(max_length=1,choices=gender_choices)
    email=models.EmailField()
    phone_number=models.PositiveIntegerField()
    student_national_id=models.CharField(max_length=12)
    nationality_choices=(
        ('Kenya','Kenya'),
        ('Uganda','Uganda'),
        ('Rwanda','Rwanda'),
    )
    nationality=models.CharField(max_length=10,choices=nationality_choices)
    registration_number=models.PositiveSmallIntegerField(null=True,blank=True)
    guardian_name=models.CharField(max_length=10,null=True,blank=True)
    guardian_contact=models.PositiveIntegerField()
    medical_report=models.FileField(null=True,blank=True,upload_to="images/")
    class_name=models.CharField(max_length=10,null=True,blank=True)
    room_number=models.CharField(max_length=13,null=True,blank=True)
    mentors_name=models.CharField(max_length=10)
    big_sister_name=models.CharField(max_length=10)
    language_choices=(
        ('E','English'),
        ('K','Kiswahili'),
        ('F','French'),
        ('O','Others'))
    languages=models.CharField(max_length=1,choices=language_choices)
    passport_photo=models.ImageField(null=True,blank=True,upload_to="images/")
    def __str__(self):
        return self.first_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def year_of_birth(self):
        return datetime.datetime.now().year- self.age

