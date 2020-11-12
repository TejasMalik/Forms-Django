from django.shortcuts import render
from django.http import HttpResponseRedirect
from main import (
    forms,
    models
)

# Create your views here.
def index(request):
    context = {
        'form': forms.ExampleForm
    }
    return render(request, 'main/index.html', context)

def students(request):
    students = models.Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'main/students.html', context)


def addstudent(request):
    

    if request.method == 'GET':
        studentform = forms.StudentForm()
    else:
        studentform = forms.StudentForm(request.POST)
        if studentform.is_valid():
            student = studentform.save()
            return HttpResponseRedirect('/students')


    context = {
        'studentform': studentform
    }
    return render(request, 'main/addstudent.html', context)


