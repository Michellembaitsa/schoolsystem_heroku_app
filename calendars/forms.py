from django import forms
from django.db.models.base import Model
from.models import Event

class CalendarsRegistrationform(forms.ModelForm):
    class Meta:
        model=Event
        fields="__all__"