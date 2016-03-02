from django import forms
from material import Layout, Row, Fieldset, Column, Span5

BRANCH_CHOICES = (('cse', 'CSE'),
                  ('it', 'IT'),
                  ('ec', 'EC'),
                  ('en', 'EN'),
                  ('me', 'ME'),
                  ('ce', 'CE'),
                  ('ei', 'EI'),
                  )
YES_OR_NO = (('y', 'yes'),
             ('n', 'no'))


class RegistrationForm(forms.Form):
    Name = forms.CharField(max_length=50,
                           label='Name', widget=forms.TextInput(
            attrs={'type': 'text', 'id': 'icon_prefix', 'class': 'validate',
                   'name': 'name'})
    )

    Contact = forms.IntegerField(widget=forms.NumberInput(
        attrs={'type': 'tel', 'id': 'icon_telephone', 'class': 'validate',
               'name': 'contact'}), label='Contact No.'
    )
    Email = forms.EmailField(widget=forms.TextInput(
        attrs={'type': 'email', 'id': 'email', 'class': 'validate'}),
        label="Email"
    )

    StudentNo = forms.IntegerField(widget=forms.NumberInput(
        attrs={'type': 'number', 'id': 'icon_prefix', 'class': 'validate',
               'name': 'student_no'}),
        label='Student No.'
    )

    Branch = forms.ChoiceField(widget=forms.Select(
        attrs={'type': 'text', 'id': 'branch', 'class': 'select-dropdown' , 'name':'Branch'}),
        label='Choose your branch name',
        choices=BRANCH_CHOICES, required=True
    )

    Hosteler = forms.ChoiceField(widget=forms.RadioSelect(
        attrs={'type': 'radio', 'id': 'test1', 'name': 'group1'}),
        label='Are you a Hosteler?',
        choices=YES_OR_NO, required=True
    )

    Skills = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'text', 'id': 'icon_prefix', 'class': 'validate',
               'name': 'skills'}),
        label='Mention your skills'
    )

    Designer = forms.CharField(widget=forms.Textarea(
        attrs={'type': 'textarea', 'id': 'icon_prefix', 'class': 'validate',
               'name': 'skills'}),
        label='Mention any designer softwares you have worked on'
    )

    layout = Layout(
        Row('Name', 'StudentNo'),
        Row('Email', 'Contact'),
        Row('Branch'),
        Row('Skills'),
        Row(Column('Hosteler'),
            Column('Designer')
            )
    )
