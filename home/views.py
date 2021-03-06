from django.shortcuts import render
#from django.http import HttpResponse
from .forms import FeedbackForm
from .forms import StudentForm
from .models import Student
from django.core.mail import send_mail
# Create your views here.
def index(request):
        return render(request, "home.html", [])


def register(request):
    form = StudentForm(request.POST or None)
    context = {
        "hello_message": "Register new student",
        "form" : form
    }
    
    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get('full_name')
        if full_name == "Jacob":
            full_name= "Developer"
        instance.full_name = full_name
        instance.save()
        context = {
            "hello_message": "Student saved!"
        }
    print (request.POST)
    return render(request, "index.html", context)
    
def feedback(request):

    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        from_email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        message= form.cleaned_data.get('message')
        prepared_message = "you have feedback from {} saying '{}'".format(full_name,message)
        send_mail('New feedback given', prepared_message,from_email ,
    ['bmnenz@gmail.com'], fail_silently=False)
    context = {
        "form": form
    }
    return render(request, 'feedback.html', context)

def students(request):
    search_term = request.GET.get('search', default='')
    students = Student.objects.all().order_by('-last_update').filter(full_name__contains = search_term)
    context = {"students" : students

    }
    return render(request, "students.html", context)
