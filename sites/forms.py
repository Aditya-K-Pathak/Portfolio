from django import forms

class userform(forms.Form):
    username = forms.CharField(
        max_length = 16,
        min_length = 4,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'username',
                'placeholder': 'Username'
            }
        )
    )
    password = forms.CharField(
        max_length = 64,
        min_length = 8,
        label = '',
        widget = forms.PasswordInput(
            attrs = {
                'id': 'password',
                'type': 'password',
                'placeholder': 'Password'
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
    url = forms.CharField(
        max_length = 10,
        min_length = 4,
        label = '',
        widget = forms.TextInput(
            attrs = {
                'id': 'url',
                'placeholder': 'Your End Point URL'
            }
        )
    )
    html = forms.CharField(
        label = '',
        widget = forms.Textarea(
            attrs = {
                'id': 'html',
                'placeholder': 'Enter Your Code',
                'rows': 5,
                'cols': 50,
            }
        )
    )
    