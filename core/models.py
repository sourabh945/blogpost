from django.db import models

from django.contrib.auth.models import AbstractBaseUser
from django.core.mail import send_mail

### settings imports 

from django.conf import settings

### local imports 

from .managers import AuthorManager

# Create your models here.


class Author(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='author email address',
        unique=True,
        max_length=126,
        error_messages={
            'unqiue':'Author with this email address already exists'
        }
    )

    username = models.CharField(
        verbose_name='username of the author',
        max_length=126,
        unique=True,
        primary_key=True,
        error_messages={
            'unique':'Author with this username already exists'
        }
    )

    full_name = models.CharField(
        verbose_name='name of user',
        max_length=126,
        null=True,
        blank=True
    )

    verified_user = models.BooleanField(
        verbose_name='email verified',
        default=False,
    )
    
    objects = AuthorManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def email_user(self,subject,message,from_email=None,**kwargs):
        send_mail(subject,message,from_email,[self.email],**kwargs)

    def verified_ok(self):
        self.verified_user = True
        self.save()

    def send_verification_email(self,verificationURL:str):
        message = f'Welcome there,\n I personally welcome you to start using our blog service\n\nFor verification please click on the link :{verificationURL}\n Thank you.\nWe love to have you.\nRegards:\nSourabh Sheokand\nMaintainer of the wesite.\n'
        subject = 'Verification for Portfolio website'
        try:
            self.email_user(subject,message,settings.EMAIL_HOST_USER,fail_silently=False)
            return True
        except: 
            return False
        

class Blog(models.Model):

    id = models.AutoField(
        primary_key=True,
        verbose_name='blog id',
    )

    title = models.TextField(
        verbose_name='title of the blog',
        blank=False,
        null=False,
        max_length=250
    )

    author = models.ForeignKey(
        to=Author,
        verbose_name='author of the blog',
        on_delete=models.CASCADE
    )

    date_of_publish = models.DateTimeField(
        verbose_name='date of publish',
        auto_now_add=True
    )

    blog_content = models.TextField(
        verbose_name='blog content',
        blank=False,
        null=False,
        max_length=25000
    )