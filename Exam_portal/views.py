from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, Http404
from django.core.urlresolvers import reverse
import json
from .forms import RegistrationForm
from .models import Student,Question,QuestionChoice,Category,Test


def examend(request):
    return render(request,'Exam_portal/examend.html')


def timer(request):
    time = Test.objects.get(name='Test1').time
    hours = time.hour
    minutes = time.minute
    seconds = time.second
    data={'time': [hours,minutes,seconds]}
    return HttpResponse(json.dumps(data),content_type='application/json')

def show(request):
    # Number_of_stundents = Student.objects.count()
    # query_set = Student.objects.get(pk=1)
    # Category1 =  Category.objects.all()
    # print(Category1)
    # question = Category1[0].question_set.all().order_by('id')
    # print("hello")
    # # print(question[0])
    # print(len(question))
    # print(question[0].id)
    # question_key = []
    # for i in range(0,len(question)):
    #     question_key.append(question[i].id)
    # print(question_key)
    # print(question_key.index(2))
    # i = question_key.index(2)
    # print(question_key[i+1])
    # print(question_key[i-1])
    # print(question.get(pk=i).question_text)



    category1 = Category.objects.all()
    question = category1[0].question_set.all().order_by('id')
    # print(question[0])
    question_object_list = list(question)
    # print(list(question))
    choice = question[0].questionchoice_set.all()
    choice_set = []

    for i in range(0,len(choice)):
        choice_set.append(choice[i].choice)

    question_key =[]
    for i in range(0,len(question_object_list)):
        question_key.append(question_object_list[i].id)

    print(question_key)

    # for i in range(len(choice)):
    #     print (choice.choice)
    query_set = {"question":question[0].question_text,"choice":choice_set}

    request.session['key_list'] = question_key
    request.session['current'] = question[0].id

    # when the first question is displayed, we first have to store its pk in a session for further submittion of the user/student answer
    #on the ajax call function again a list of pk for the corresponding question will be generated and on next button the index of the list will be incremented for next question fetch

    context_variable = {
        "keys":question_key,
        "Number":range(1,len(question)+1),
        "instance":query_set
    }



    return render(request,'Exam_portal/ajax.html',context_variable)



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
                request.session['student_id'] = data.id
                #same data can be used to get the corrsponding did associate with the students

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
