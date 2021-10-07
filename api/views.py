
# from django.shortcuts import render
from rest_framework import serializers, viewsets
from student.models import Student
from .serializers import ForAllSerializer
from trainer.models import Trainer
from courses.models import Courses

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializers_class=ForAllSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=ForAllSerializer
    
class CourseViewSet(viewsets.ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=ForAllSerializer