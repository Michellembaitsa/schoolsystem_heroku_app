from django.http import response
from student.views import register_student
from django.conf.urls import url
from django.test import TestCase
from .models import Student
import datetime
from django.urls import reverse
# Creating a unit test for student class in student models, we have

class StudentModelTestcase(TestCase):
    def setUp(self):
        self.student=Student(first_name="Michelle",last_name="AkiraChix",age=25)

    #the test function
    def test_full_name_contains_first_name(self):
        self.assertIn(self.student.first_name,self.student.full_name())#assertions help us verify i.e enforcing that something is true.


    def test_full_name_contains_last_name(self):
        self.assertIn(self.student.last_name,self.student.full_name())#assertions help us verify i.e enforcing that something is true.


    def test_year_of_birth(self):
        year=datetime.datetime.now().year-self.student.age
        self.assertEqual(year,self.student.year_of_birth())

    def test_student_registration_view(self):
        self.data={"first_name":self.student.first_name,"last_name":self.student.last_name,"age":self.student.age}
        url=reverse("register_student")
        #client is used to simulate http requests
        response=self.client.post(url,self.data)
        self.assertEqual(response.status_code,200)

    #test_student_list
    #test_student_profile
    #test_edit student
    #course view,trainers and events tests.
    #running tests in the cloud... CI/CD


