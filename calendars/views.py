from calendar import Calendar
from calendars.models import Event
from django.shortcuts import render
from .forms import CalendarsRegistrationform
from django.http import HttpResponse

#new imports start
from datetime import date, datetime, timedelta
from django.views import generic
from django.utils.safestring import mark_safe

from .models import *
from .utils import Calendar
#new imports end

# Create your views here.
def register_calendars(request):
    if request.method=="POST":
        form=CalendarsRegistrationform(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=CalendarsRegistrationform()
        print(form.errors)
    return render(request,"register_calendars.html",{"form":form})


# def calendar_list(request):
#     calendars=Event.objects.all()
#     return render(request,"calendar_list.html",{"calendars":calendars})


def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'calendar.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        d = get_date(self.request.GET.get('day', None))

        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

