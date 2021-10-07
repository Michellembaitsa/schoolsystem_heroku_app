from django.db import models
#from rest_framework import serializers
from rest_framework import serializers
from student.models import Student
from trainer.models import Trainer
from courses.models import Courses
class ForAllSerializer(serializers.ModelSerializer):
    # class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("first_name","last_name","age",)
        model=Trainer
        fields=("first_name","last_name","age",)
        model=Courses
        fields=("course_code","course_duration","course_name")