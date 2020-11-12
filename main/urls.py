from django.urls import path
from main import views


urlpatterns = [
    path('addstudent', views.addstudent),
    path('students', views.students),
    path('', views.index)
]