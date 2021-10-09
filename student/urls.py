from rest_framework.routers import DefaultRouter
import student.views as student_viewset
from django.urls import path, include

router = DefaultRouter()

router.register(r'student_app', student_viewset.StudentViewSet, basename = 'student')


urlpatterns = [
    path('', include(router.urls))
    ]
