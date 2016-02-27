from django.contrib import admin

from .models import *



# Register your models here.

admin.site.register(QuestionChoice)
admin.site.register(Question)
admin.site.register(Test)
admin.site.register(Category)
admin.site.register(CorrectChoice)
admin.site.register(Student)
admin.site.register(StudentAnswer)