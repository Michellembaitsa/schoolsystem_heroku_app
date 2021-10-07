from django import forms
from django.db.models import Model
from django.forms import fields
from.models import Courses

class CoursesRegistrationForm(forms.ModelForm):
    class Meta:
        model=Courses
        fields="__all__"