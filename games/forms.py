from django import forms

class userRegisteration(forms.Form):
    user_name = forms.CharField(
        max_length=20,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Usesrname',
                'id': 'user_name'
            }
        )
    )
    password = forms.CharField(
        max_length=20,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'type': 'password',
                'placeholder': 'Password',
                'id': 'user_password'
            }
        )
    )

class options(forms.Form):
    user_name = forms.CharField(
        max_length=20,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Usesrname',
                'id': 'user_name',
            }
        )
    )
    a = forms.BooleanField(
        required = False
    )
    b = forms.BooleanField(
        required = False
    )
    c = forms.BooleanField(
        required = False
    )
    d = forms.BooleanField(
        required = False
    )