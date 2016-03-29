from Exam_portal.models import Question, QuestionChoice, Test
data = {}
qs = Question.objects.all()
qs = list(qs)
for q in qs:
 options = q.choices.all()
 data[q] = list(options)
