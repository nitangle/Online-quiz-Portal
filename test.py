from Exam_portal.models import Test, Category, QuestionChoice

t1 = Test.objects.filter(name='Test1').first()

qs = t1.questions.all()

tempdata = {}
qdata = data = dict()

qlist = []

print(qs)


def create_list(qlist):
    for q in qs:
        list = q.choices.all()
        qlist = []
        print(list)
        for i in range(len(list)):
            qlist.append(list[i].choice)
        qdata = {}
        qdata[q.text] = qlist
        if data.get(q.category.name):
            data[q.category.name].append(qdata)
        else:
            data[q.category.name] = [qdata, ]
    return data

data = create_list(qlist)

print(data)
# for q in qs:
#     if tempdata.get(q.category.name):
#         tempdata[q.category.name].append(str(q))
#     else:
#         tempdata[q.category.name] = [str(q), ]
#
# print(tempdata)
# # qlist = create_list(qlist)
# # print(qlist)
# print(qdata)




# print(data)
# for key in data.keys():
#   print(key)

# qcdict = {}
# for q in qs:
#   if q.choices.all():
#       qcdict[q].append([q.choices.all()])

# print(qcdict)
