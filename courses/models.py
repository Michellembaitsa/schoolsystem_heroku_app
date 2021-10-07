from django.db import models

# Create your models here.
class Courses(models.Model):
    course_name=models.CharField(max_length=30)
    course_trainer=models.CharField(max_length=10)
    course_code=models.CharField(max_length=5)
    course_description=models.CharField(max_length=20)
    duration_of_lesson=models.CharField(max_length=10)
    notes=models.FileField(null=True,blank=True,upload_to="images/")
    def __str__(self):
        return self.course_name
