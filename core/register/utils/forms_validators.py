from django.core.exceptions import ValidationError
from django.db.models import Q


from ...models import Author as User


def validate_email(email:str) -> bool:

    try:
        user = User.objects.get(email=email)
    except:
        return True
    if user:
        raise ValidationError('Email is already exist')


def validate_username(username:str) -> bool:

    try:
        user = User.objects.get(username=username)
    except:
        return True
    if user:
        raise ValidationError('Username is already exist')
    

def validate_user(email_or_username:str) -> bool:
    try:
        _ = User.objects.get(Q(username=email_or_username) | Q(email=email_or_username))
        return True
    except:
        raise ValidationError('User does not exist')