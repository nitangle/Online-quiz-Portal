from django.http import HttpResponse
import json
from django.core import serializers
from .models import Student, QuestionChoice, Question, Category,StudentAnswer,CorrectChoice
from django.core.exceptions import ObjectDoesNotExist

def grid(request):
    if request.is_ajax() or request.method == "POST":
        id = int(request.GET.get('id'))
        print(id)

        choice, query_set = getData(id, request)

        request.session['current'] = int(id)

        return HttpResponse(json.dumps(query_set),
                            content_type="application/json")
    return None

def markCalculate(request):
    student = request.session.get('student_id')
    question_keys = request.session.get('key_list')
    
    
    marks = 0
    
    for i in range(len(question_keys)):
        question = Question.objects.get(pk=int(question_keys[i]))
        correct_choice = CorrectChoice.objects.get(question_id = int(question_keys[i]))
        student_answer = StudentAnswer.objects.get(student=student,question = question)
        if (student_answer.answer == correct_choice.correct_choice):
            marks = marks + question.marks

    marks_of_student = MarksOfStudent.objects.create(student = studnet,marks =  marks)

    return None







#  next ajax request will also submit the question answer
#  previous will only traverse the question on the page via ajax request
#  viewing a question again will show that it is unmarked but the grid color will indicate whether you have answered the question or not
#  again submitting the answer will update the previuos answer


def submitAnswer(request):
    # print ("-----")
    # print (request.session.get('current'))
    # print (request.POST.get('answer'))
    # print (request.session.get('student_id'))
    # print ('-----')
    current = request.session.get('current')
    answer = request.POST.get('answer')
    student_id = request.session.get('student_id')


    student = Student.objects.get(pk=student_id)
    question = Question.objects.get(pk=current)
    choice = QuestionChoice.objects.get(pk=answer)

    try:
        data = StudentAnswer.objects.get(question = question, student=student)
        if(data !=None):
            data.answer = choice
            data.save()
    except ObjectDoesNotExist:    
        print("Object does not found")
        print("creating new instance")
        StudentAnswer.objects.create(answer=choice,question=question,student=student)

    return None










def getData(pk, request):
    question = Question.objects.get(pk=pk)
    choice = question.questionchoice_set.all().order_by('id')

    choice_data = []
    color_key = request.session.get('current')

    

    # print("question_no {}".format(request.session.get('key_list').index(color_key)+1))
    # print("Question :{}".format())
    question_no = request.session.get('key_list').index(color_key) + 1

    for i in range(0, len(choice)):
        data = (choice[i].choice,choice[i].id)
        choice_data.append(data)

    if request.method == "POST" and request.POST.get('answer') != '':
        print("True")
        query_set = {
            "question_no":question_no,
            "question": question.question_text,
            "choice_data": choice_data,
            "color": color_key,
        }
    else:
        print("Method not POST or answer not submitted")
        query_set = {
            "question_no":question_no,
            "question": question.question_text,
            "choice_data": choice_data ,
        }



    # query_set = {
    # "question": question.question_text,
    # "choices": choices,
    # }


    return choice, query_set


def ajaxnext(request):
    """
    this will select the number of any data from the database
    serialize it
    start a session
    and send the json on the page and render is using jQuery
    :param request:
    :return:
    """
    if request.is_ajax() or request.method == 'POST':

        if(request.POST.get('answer')!=''):
            submitAnswer(request)

        print(request.POST.get('answer'))

        current = request.session.get('current')
        key_list = request.session.get('key_list')

        if (key_list.index(current) != key_list[-2]):
            print(current)
            print("if is true")
            next = key_list.index(current) + 1

        else:
            next = key_list.index(current)

        print(request.session.get('current'))


        choice, query_set = getData(key_list[next], request)

        if (request.session.get('current') != key_list[-1]):
            request.session['current'] = key_list[next]

        

        return HttpResponse(json.dumps(query_set),
                            content_type="application/json")


def ajaxprevious(request):
    """

    :param request:
    :return:
    """
    if request.is_ajax():
        current = request.session.get('current')
        key_list = request.session.get('key_list')

        if (key_list.index(current) >= 1):
            print(current)
            previous = key_list.index(current) - 1
        else:
            previous = key_list.index(current)

        choice, query_set = getData(key_list[previous], request)

        print(request.session.get('current'))

        if (request.session.get(current) != key_list[0]):
            request.session['current'] = key_list[previous]

        return HttpResponse(json.dumps(query_set),
                            content_type='application/json')

    return None


def postajax(request):
    if request.is_ajax() and request.method == "POST":
        data = request.POST.get("item")

        print (data)
        return HttpResponse(json.dumps("['rupanshu']"),
                            content_type="application/json")
