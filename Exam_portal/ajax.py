from django.http import HttpResponse
import json
from django.core import serializers
from .models import Student


def ajax(request):
    if request.is_ajax():
        q = Student.objects.get(name="Satvik")
        print(q)
        print(type(q))

        data = serializers.serialize('json',[q,])
        print(data)
        print(type(data))

        jdata = json.dumps(data)
        print(type(jdata))
        #
        detail = {'name':'hello','work':'This is ajax'}
        #
        # # data = json.dumps(json_data)
        # print(data)
        # json_data = ['hello', 'rupanshu']
        # data = json.dumps(q)
        # print(data)

        return HttpResponse(data, content_type='application/json')


