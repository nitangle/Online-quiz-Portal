from django import forms


class RegistrationForm(forms.Form):
    Name = forms.CharField(max_length=50,
                           label='Name', widget=forms.TextInput(
            attrs={'type': 'text', 'id': 'icon_prefix', 'class': 'validate',
                   'name': 'name'}))

    Contact = forms.IntegerField(widget=forms.NumberInput(
        attrs={'type': 'tel', 'id': 'icon_telephone', 'class': 'validate',
               'name': 'contact'}), label='Contact No.'
    )
    Email = forms.EmailField(widget=forms.TextInput(
        attrs={'type': 'email', 'id': 'email', 'class': 'validate'}),
                             label="Email")
