from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=20)                                  # Stage1 of registration
    student_no = models.IntegerField()                                      # Stage2 of registration
    branch = models.CharField(max_length=5)                                 # Stage2 of registration
    contact = models.BigIntegerField()                                      # Stage1 of registration
    skills = models.CharField(max_length=10)                                # Stage3 of registration
    email = models.EmailField()                                             # Stage1 of registration
    hosteler = models.BooleanField()                                        # Stage2 of registration
    designer = models.CharField(label="Mention any software you worked on(photoshop etc)", max_length=10) # Stage3 of registration


class Categories(models.Model):
    category = models.CharField(max_length=10)


class Questions(models.Model):
    question_text = models.CharField(max_length=10)
    negative = models.BooleanField()
    marks = models.IntegerField()
    type = models.ForeignKey(Categories, on_delete=models.CASCADE)


class QuestionChoices(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice = models.CharField(max_length=20)


class CorrectChoices(models.Model):
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE, db_column='question_id')
    correct_choice = models.ForeignKey(QuestionChoices, on_delete=models.CASCADE)


class StudentAnswers(models.Model):
    answer = models.CharField(max_length=20)
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    student = models.ForeignKey(Students, on_delete=models.CASCADE)


class Test(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

'''
class Instructions(models.Model):
    instructions = models.CharField()

'''


