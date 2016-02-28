from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import RegistrationForm
from .models import Student


def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST or None)
        print("hello")
        if form.is_valid():
            name = form.cleaned_data['Name']
            email = form.cleaned_data['Email']
            contact = form.cleaned_data['Contact']

            print("hello" + name)

        print (form.errors)
    context = {
        'title': 'SI recruitment',
        'form': form,
    }
    return render(request, 'Exam_portal/register.html', context)
