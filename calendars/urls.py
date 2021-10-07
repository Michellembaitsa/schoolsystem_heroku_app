from django.conf.urls import url
from django.urls import path
from .import views
from .views import  register_calendars
urlpatterns=[
    path("register/",register_calendars,name="register_calendars"),
    #path("list/",calendar_list,name="calendar_list"),
    url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'),
]
#  path("register/",register_trainer,name="register_trainer"),
#     path("list/", trainer_list, name="trainer_list"),