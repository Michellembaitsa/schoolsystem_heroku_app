from django.db import models

# Create your models here.
class Trainer(models.Model):
    trainer_image=models.ImageField(null=True,blank=True,upload_to="images/")
    first_name=models.CharField(max_length=10,null=True)
    last_name=models.CharField(max_length=10,null=True)
    course_name=models.CharField(max_length=30,null=True)
    id_number=models.CharField(max_length=8,null=True)
    gender_choices=(
        ('F','Female'),
        ('M','Male'),
        ('O','Other'))
    gender=models.CharField(max_length=1,choices=gender_choices)
    email=models.EmailField(default=None)
    curriculum_vitae=models.FileField(null=True,blank=True,upload_to="images/")
    proffession=models.CharField(max_length=10,null=True)
    company=models.CharField(max_length=10,null=True)
    work_title=models.CharField(max_length=10,null=True)
    contract=models.FileField(null=True,blank=True,upload_to="images/")
    def __str__(self):
        return self.last_name
