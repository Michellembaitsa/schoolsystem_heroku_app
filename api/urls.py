from django import urls
from django.urls import path,include
from rest_framework import routers
from .views import StudentViewSet
from .views import TrainerViewSet
from .views import CourseViewSet

router= routers.DefaultRouter()
router.register("students/", StudentViewSet)
router.register("trainers/", TrainerViewSet)
router.register("courses/", CourseViewSet)

# router.urls compaines all the urls together and send the reply.

urlpatterns=[
    path('', include(router.urls)),
    path('',include(router.urls)),
    path('', include(router.urls))
]