from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


### local imports 

from .utils import validate_username


class AuthorManager(BaseUserManager):

    def create_user(self,username,email,name,passwords,**args):

        if not email or not username:
            raise ValidationError('Author name or email address is not present')
        
        if not validate_username(username):
            raise ValidationError('Author username is not valid')
        
        email = self.normalize_email(email=email)

        user = self.model(username=username,email=email,name=name,**args)
        user.set_password(passwords)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,name,email,passwords,**args):
        raise ValidationError('Super users are not allowed')