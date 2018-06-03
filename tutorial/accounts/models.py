from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.utils import timezone
from datetime import datetime
from django.db import models
#from simple_history.models import HistoricalRecords
from django.conf import settings
from django.contrib.auth import get_user_model
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django_currentuser.db.models import CurrentUserField
import colorama
from colorama import Fore





# Create your models here.
class UserProfileManager(models.Manager):
    def get_queryset(self):
        if __name__ == '__main__':
            return super(UserProfileManager,self).get_queryset().filter(city='chennai')

class UserProfile(models.Model):
    user=models.OneToOneField(User,unique=True)
    description=models.CharField(max_length=100,default='',blank=True)
    city=models.CharField(max_length=100,default='',blank=True)
    website=models.URLField(default='',blank=True)
    phoneNo=models.IntegerField(default=0,blank=True)
    image=models.ImageField(upload_to='profile_image',blank=True,null=True)

    #Karur= UserProfileManager()

    def __str__(self):
        return '%s' %self.user.username

def create_profile(sender,**kwargs):
    if kwargs['created']:
        user_profile=UserProfile.objects.create(user=kwargs['instance'])
    post_save.connect(create_profile,sender=User)


#########################################################3
#class Enter_task(models.Model):
 #   task_id=models.FloatField()
 #   task_name=models.FloatField()
###########################################################
PRIORITY_CHOICES = (('HIGH', 'High'),
                    ('MEDIUM', 'Medium'),
                    ('LOW', 'Low'))
STATUS_CHOICES =  (('IN PROGRESS', 'In Progress'),
                    ('COMPLETED', 'Completed'),
                    ('HOLD', 'Hold'))

class Blogs(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True,default=get_current_authenticated_user())
    #User = get_user_model()
    title=models.CharField(max_length=255,default='',blank=False)
    #title = models.ForeignKey(max_length=255, default='', blank=False)
    task_id = models.CharField(max_length=255,default='',blank=False)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='HIGH')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='IN PROGRESS')
    resource_name = models.CharField(max_length=255, blank=False,default='')
    effort_estimated =models.IntegerField(default=0)
    actual_start_date=models.DateField(default=datetime.now(), blank=False)
    deadline = models.DateField(default=datetime.now(), blank=False)
    actual_effort = models.IntegerField(default=None,null=True, blank=True)
    actual_date_completion = models.DateField(default='',null=True,blank=True)
    resource_score = models.IntegerField(blank=True, default=0)
    reason= models.TextField(default='Significant achievement of your resource.')
    #history=HistoricalRecords()

    def __str__(self):
        return '%s' %self.title + " "+" "+ self.status + " "+"Entered By" +" "+ '%s' % self.user
       #return '%s' % self.user
