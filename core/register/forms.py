from django import forms
from .utils import forms_validators

class signup_form(forms.Form):

    email = forms.EmailField(
        max_length=126,
        label='Enter your email',
        validators=[forms_validators.validate_email],
        required=True
    )

    username = forms.CharField(
        max_length=126,
        label='Enter a username for you',
        validators=[forms_validators.validate_username],
        required=True,
    )

    name = forms.CharField(
        max_length=126,
        label='Enter your name',
        required=True,
    )

    password = forms.CharField(
        label='Enter a password for you',
        required=True,
        widget=forms.PasswordInput,
    )

    confirm_password = forms.CharField(
        label='Confirm your password',
        required=True,
        widget=forms.PasswordInput,
    )


class login_form(forms.Form):

    username_or_email = forms.CharField(
        max_length=126,
        label='Enter your email or username',
        validators=[forms_validators.validate_user],
        required=True,
    )

    password = forms.CharField(
        label='Enter your password',
        required=True,
        widget=forms.PasswordInput,
    )
    