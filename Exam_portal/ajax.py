from django.http import HttpResponse
import json
from django.core import serializers
from .models import Student,QuestionChoice,Question,Category

# #  a new key list will be generated
#  question_key =[]
#     for i in range(0,len(question)):
#         question_key.append(question[i].id)




def ajaxnext(request):
    """
    this will select the number of any data from the database
    serialize it
    start a session
    and send the json on the page and render is using jQuery
    :param request:
    :return:
    """
    # category = Category.objects.all()
    # question = category[0].question_set.all().order_by('id')
    # question_key = []
    # for i in range(len(question)):
    #     question_key.append(question[i].id)



    if request.is_ajax():
        # print(type(request.session.get('next')))
        # request.session['previous'] = request.session.get('next')
        # pk = request.session['next'] = request.session.get('next') + 1

        current = request.session.get('current')
        key_list = request.session.get('key_list')
        # print(current)
        # print(key_list)
        if(current!=key_list[-1]):
            next = key_list.index(current) + 1
        else:
            next = key_list.index(current)

        print(request.session.get('current'))

        question = Question.objects.get(pk=key_list[next])
        choice = question.questionchoice_set.all()

        choices = []
        for i in range(0,len(choice)):
            choices.append(choice[i].choice)


        query_set = {
            "question":question.question_text,
            "choices":choices,
        }
        if(request.session.get('current')!=key_list[-1]):
            request.session['current'] = key_list[next]

        # object_list = request.session.get('object_list')
        # index = object_list.index(current)
        # question = object_list(index+1)
        # request.session['current'] = question

        # print(pk)
        # q = Student.objects.get(pk=pk)
        # print(q)
        # data = serializers.serialize('json', [query_set])
        # print(data)

        # print(" next = {} previous = {} ".format(request.session.get('next'),
        #                                          request.session.get(
        #                                              'previous')))

        return HttpResponse(json.dumps(query_set), content_type="application/json")



def ajaxprevious(request):
    """

    :param request:
    :return:
    """
    # category = Category.objects.all()
    # question = category[0].question_set.all().order_by('id')
    # question_key = []
    # for i in range(len(question)):
    #     question_key.append(question[i].id)




    if request.is_ajax():
        current = request.session.get('current')
        key_list = request.session.get('key_list')

        previous = key_list.index(current) - 1

        print(current)
        question = Question.objects.get(pk=key_list[previous])
        choice = question.questionchoice_set.all()

        choices = []
        for i in range(0,len(choice)):
            choices.append(choice[i].choice)

        query_set = {
            "question":question.question_text,
            "choices":choices,
        }
        print(request.session.get('current'))
        if(request.session.get('current')==key_list[0]):
            request.session['current'] = key_list[0]
        if(request.session.get('current')!=key_list[0]):
            request.session['current'] = key_list[previous]



        # pk =request.session['previous'] = request.session.get('next') - 1
        # request.session['next'] -=1
        # pk = request.session.get('previous')
        #
        # if(request.session.get('next')>=2):
        #     request.session['previous'] -= 1
        #     request.session['next'] -= 1
        # request.session['previous'] -= 1

        # q = Student.objects.get(pk=pk)
        # data = serializers.serialize('json', [query_set, ])
        # print(
        #     " next = {} previous = {} ".format(request.session.get('next'),
        #                                        request.session.get(
        #                                            'previous')))

        return HttpResponse(json.dumps(query_set), content_type='application/json')

    return None




# def postajax(request):
#     if request.is_ajax() and request.method == "POST":
#         data = request.POST.get("item")
#
#         print (data)
#         return HttpResponse(json.dumps("['rupanshu']"),content_type="application/json")



# # def ajax(request):
# #
#     category = Category.objects.all()
#     question = category[0].question_set.all().order_by('id')
#     question_key = []
#     for i in range(len(question)):
#         question_key.append(question[i].id)
#     #
#     #
#     #
#     #
#     # if request.is_ajax():
#     #
#     #
#     #     q = Student.objects.get(name="Satvik")
#         print(q)
#         print(type(q))
#
#         data = serializers.serialize('json', [q, ])
#         print(data)
#         print(type(data))
#
#         jdata = json.dumps(data)
#         print(type(jdata))
#         #
#         detail = {'name': 'hello', 'work': 'This is ajax'}
#         #
#         data = json.dumps(json_data)
#         print(data)
#         json_data = ['hello', 'rupanshu']
#         data = json.dumps(q)
#         print(data)
#
#         return HttpResponse(data, content_type='application/json')
