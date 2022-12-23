from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


"""student table model"""
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length= 20)
    

"""create token by signals.
when new user create, token 
will automatically generate. 
"""
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance= True, created= False, **kwargs):

    if created:
        Token.objects.create(user= instance)