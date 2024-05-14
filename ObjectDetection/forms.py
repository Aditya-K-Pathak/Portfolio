from django import forms

class ObjectForm(forms.Form):
    username = forms.CharField(
        max_length = 16,
        min_length = 4,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'username',
                'placeholder': 'Enter Your Name'
            }
        )
    )
    email = forms.CharField(
        max_length = 40,
        min_length = 4,
        label = '',
        widget = forms.EmailInput(
            attrs = {
                'id': 'email',
                'placeholder': 'Email'
            }
        )
    )
    objects = forms.CharField(
        max_length = 1000,
        min_length = 4,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'username',
                'placeholder': 'Enter Comma(,) separated object name'
            }
        )
    )