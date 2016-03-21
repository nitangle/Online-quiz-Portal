from django.http import HttpResponse
import json
from django.core import serializers
from .models import Student,QuestionChoice,Question,Category

def grid(request):
    if request.is_ajax() or request.method=="POST":
        id = int(request.POST.get('id'))
        print(type(id))

        choice,query_set = getData(id)

        request.session['current'] = int(id)

        return HttpResponse(json.dumps(query_set),content_type="application/json")
    return None



def getData(pk):

    question = Question.objects.get(pk=pk)
    choice = question.questionchoice_set.all()

    choices = []
    for i in range(0,len(choice)):
        choices.append(choice[i].choice)
    query_set = {
        "question":question.question_text,
        "choices":choices,
    }
    return choice,query_set



def ajaxnext(request):
    """
    this will select the number of any data from the database
    serialize it
    start a session
    and send the json on the page and render is using jQuery
    :param request:
    :return:
    """
    if request.is_ajax() or request.method == 'POST' :

        print(request.POST.get('answer'))


        current = request.session.get('current')
        key_list = request.session.get('key_list')

        if(key_list.index(current)<len(key_list)):
            print(current)
            next = key_list.index(current) + 1
        else:
            next = key_list.index(current)

        print(request.session.get('current'))


        choice,query_set = getData(key_list[next])



        if(request.session.get('current')!=key_list[-1]):
            request.session['current'] = key_list[next]

        return HttpResponse(json.dumps(query_set), content_type="application/json")



def ajaxprevious(request):
    """

    :param request:
    :return:
    """
    if request.is_ajax():
        current = request.session.get('current')
        key_list = request.session.get('key_list')

        if(key_list.index(current)>=1):
            print(current)
            previous = key_list.index(current) - 1
        else:
            previous = key_list.index(current)


        choice,query_set = getData(key_list[previous])

        print(request.session.get('current'))

        if(request.session.get(current)!=key_list[0]):
            request.session['current'] = key_list[previous]


        return HttpResponse(json.dumps(query_set), content_type='application/json')

    return None




def postajax(request):
    if request.is_ajax() and request.method == "POST":
        data = request.POST.get("item")

        print (data)
        return HttpResponse(json.dumps("['rupanshu']"),content_type="application/json")


