from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=20)  # Stage1 of registration
    student_no = models.IntegerField()  # Stage2 of registration
    branch = models.CharField(max_length=5)  # Stage2 of registration
    contact = models.BigIntegerField()  # Stage1 of registration
    skills = models.CharField(max_length=225)  # Stage3 of registration
    email = models.EmailField()  # Stage1 of registration
    hosteler = models.BooleanField()  # Stage2 of registration
    designer = models.CharField(
        "Mention any software you worked on(photoshop etc)",
        max_length=10)  # Stage3 of registration

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=50, default=None, null=True)
    questions = models.ManyToManyField('Question', related_name='tests')
    time = models.TimeField(null=True)

    # question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class Instruction(models.Model):
#     instructions = models.CharField(max_length=100)
#     test = models.ForeignKey(Test, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.instructions


class Category(models.Model):
    name = models.CharField(max_length=225, default='Category')

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return str(self.name)


class Question(models.Model):
    text = models.CharField(max_length=225)
    negative = models.BooleanField()
    marks = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='question')

    def __str__(self):
        return self.text


class QuestionChoice(models.Model):
    choice = models.CharField(max_length=50)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')

    def __str__(self):
        return str(self.choice)


class CorrectChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,
                                 db_column='question_id')
    correct_choice = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("question", "correct_choice"),)

    def __str__(self):
        return self.correct_choice


class StudentAnswer(models.Model):
    answer = models.Field(max_length=225)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    student = models.ForeignKey(Student, on_delete=models.CASCADE)


    def __str__(self):
        return self.answer
