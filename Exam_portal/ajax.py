from django.http import HttpResponse
import json
from django.core import serializers
from .models import Student, QuestionChoice, Question, Category


def grid(request):
    if request.is_ajax() or request.method == "POST":
        id = int(request.GET.get('id'))
        print(id)

        choice, query_set = getData(id,request)

        request.session['current'] = int(id)

        return HttpResponse(json.dumps(query_set),
                            content_type="application/json")
    return None

#  next ajax request will also submit the question answer
#  previous will only traverse the question on the page via ajax request
#  viewing a question again will show that it is unmarked but the grid color will indicate whether you have answered the question or not
#  again submitting the answer will update the previuos answer





def getData(pk,request):
    question = Question.objects.get(pk=pk)
    choice = question.questionchoice_set.all()


    choices = []
    color_key = request.session.get('current')


    for i in range(0, len(choice)):
        choices.append(choice[i].choice)

    if request.method == "POST" and request.POST.get('answer')!= '':
        print("True")
        query_set = {
            "question": question.question_text,
            "choices": choices,
            "color":color_key,
        }
    else:
        print("Method not POST or answer not submitted")
        query_set = {
        "question": question.question_text,
        "choices": choices,
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

        choice, query_set = getData(key_list[next],request)

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

        choice, query_set = getData(key_list[previous],request)

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
