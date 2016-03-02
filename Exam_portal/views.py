from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.core.urlresolvers import reverse

from .forms import RegistrationForm
from .models import Student

def show(request):
    return render(request,'Exam_portal/ajax.html',{})



def register(request):
    form = RegistrationForm()

    # if request.session.get('name'):
    #     return redirect(reverse('Exam_portal:instruction'))

    if request.method == "POST":
        form = RegistrationForm(request.POST or None)
        # print("hello")
        if request.method != "POST":
            raise Http404("Only POST methods are allowed")

        if form.is_valid():
            name = form.cleaned_data['Name']
            email = form.cleaned_data['Email']
            contact = form.cleaned_data['Contact']
            studentno = form.cleaned_data['StudentNo']
            branch = form.cleaned_data['Branch']
            if form.cleaned_data['Hosteler'] == 'y':
                hosteler = True
            else:
                hosteler = False
            skills = form.cleaned_data['Designer']

            data = Student.objects.create(name=name, student_no=studentno,
                                          branch=branch, contact=contact,
                                          skills=skills, email=email,
                                          hosteler=hosteler)
            if data:
                request.session['name'] = name
                return HttpResponseRedirect(reverse('Exam_portal:instruction'))


        print(form.cleaned_data)

        # print (form.errors)
    context = {
        'title': 'SI recruitment',
        'form': form,
    }


    return render(request, 'Exam_portal/register.html', context)


def instruction(request):
    # nothing to do here
    return render(request, "Exam_portal/instruction.html", context={})
