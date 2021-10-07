from django.shortcuts import render
from .forms import TrainerRegistrationForm
from trainer.models import Trainer

# Create your views here.

def register_trainer(request):
    if request.method=="POST":
        form=TrainerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=TrainerRegistrationForm()
        print(form.errors)
    return render(request,"register_trainer.html",{"form":form})
def trainer_list(request):
    trainers=Trainer.objects.all()
    return render(request,"trainer_list.html",{"trainers":trainers})

