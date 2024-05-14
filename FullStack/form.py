from django import forms

# Form for IP address input
class Ip(forms.Form):
    ip_address = forms.CharField(
        max_length=16,  # Maximum length of the input field
        label="",       # No label for the input field
    )

# Form for newsletter subscription
class NewsLetter(forms.Form):
    email = forms.EmailField(
        label='',   # No label for the input field
        max_length=40,  # Maximum length of the email field
        required=False, # Email field is not required
        widget=forms.EmailInput(   # Customizing email input field widget
            attrs={                # Adding placeholder text for the input field
                'placeholder': 'anyone@anymail.com'
            }
        )
    )

class ContactForm(forms.Form):
    Name = forms.CharField(
        label = '',
        max_length = 15,
        min_length = 3,
        widget = forms.TextInput(
            attrs = {
                'type':'text',
                'placeholder': 'John Doe',
                'id': 'name',
            }
        )
    )
    Email = forms.EmailField(
        label = '',
        max_length = 40,
        min_length = 11, 
        widget = forms.EmailInput(
            attrs = {
                'placeholder': 'johndoe@mail.com',
                'id': 'email'
            }
        )
    )
    Comment = forms.CharField(
        label = '',
        max_length = 300,
        widget = forms.Textarea(
            attrs = {
                'placeholder': 'Type your message here...',
                'id': 'message'
            }
        )
    )

class Verification(forms.Form):
    Email = forms.EmailField(
        label = '',
        max_length = 40,
        min_length = 11, 
        widget = forms.EmailInput(
            attrs = {
                'placeholder': 'johndoe@mail.com',
                'id': 'email'
            }
        )
    )
    pin = forms.CharField(
        label = '',
        widget = forms.TextInput(
            attrs = {
                'placeholder': '000000',
            }
        )
    )