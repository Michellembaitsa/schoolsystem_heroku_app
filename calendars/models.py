from django.db import models

# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=200,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    start_time=models.DateTimeField(null=True,blank=True)
    end_time=models.DateTimeField(null=True,blank=True)
    # event_name=models.CharField(max_length=20)
    # event_date=models.DateTimeField()
    # start_time=models.TimeField()
    # end_time=models.TimeField()
    # event_duration=models.PositiveBigIntegerField()
    # venue=CharField(max_length=10)
    # organizer=CharField(max_length=10)
    # event_goal=CharField(max_length=20)
    # attendees=IntegerField()
    # def __str__(self):
    #     return self.event_name
