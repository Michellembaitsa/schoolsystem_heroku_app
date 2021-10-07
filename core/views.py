from django.shortcuts import render
from student.models import Student
from courses.models import Courses
from trainer.models import Trainer

from .models import Item


# Create your views here.

def home(request):
    students=Student.objects.count()
    courses=Courses.objects.count()
    trainsers=Trainer.objects.count()
    data={"students":students,"courses":courses,"trainers":trainsers}

    return render(request,"home.html",data)

def video(request):
    obj=Item.objects.all()
    return render(request,'home.html',{'obj':obj})

def dashboard(request):
    students=Student.objects.count()
    courses=Courses.objects.count()
    trainers=Trainer.objects.count()
    data={"students":students,"courses":courses,"trainers":trainers}
    return render(request,'dashboard.html',data)
