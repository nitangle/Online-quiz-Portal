from django.contrib import admin

from .models import *




class QuestionInLine(admin.TabularInline):
    model = Question
    extra = 5


class CategoryAdmin(admin.ModelAdmin):
    list_editable = ['name']
    search_fields = ['name']
    list_display = ('id', 'name')
    inlines = [QuestionInLine]

    class Meta:
        model = Category

class CorrectChoiceInLine(admin.TabularInline):
    model = CorrectChoice
    extra = 1


class QuestionChoiceInLine(admin.TabularInline):
    model = QuestionChoice
    extra = 5


class QuestionAdmin(admin.ModelAdmin):
    list_editable = ['text', 'marks']
    list_display = ('id', 'text', 'marks')
    search_fields = ['text']
    inlines = [QuestionChoiceInLine,CorrectChoiceInLine]

    class Meta:
        model = Question



class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','name','branch')
    search_fields = ['name']
    ordering = ('id',)
    class Meta:
        model = Student


# Register your models here.
admin.site.register(QuestionChoice)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Test)
admin.site.register(Category, CategoryAdmin)
admin.site.register(CorrectChoice)
admin.site.register(Student,StudentAdmin)
admin.site.register(StudentAnswer)
