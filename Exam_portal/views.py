from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import  render,get_object_or_404,redirect

from .forms import RegistrationForm

def register(request):
    form  = RegistrationForm()

    context = {
        'title':'SI recruitment',
        'form':form,
    }
    return render(request,'Exam_portal/registration.html',context)