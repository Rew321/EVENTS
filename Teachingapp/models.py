import datetime
from django.db import models
import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime
from django.utils.crypto import get_random_string
# Create your models here.
class User(models.Model):
    user = models.TextField(default=None)
    def __str__(self):
        return self.user
# Table Events
class Event(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, editable=False)
    title = models.CharField(max_length=200, blank=False, null=False)
    Venue = models.CharField(max_length=100)
    image= models.ImageField(upload_to="images/")
    notes = models.TextField(max_length=1000)
    starting_time = models.DateTimeField(default=datetime.now)
    end_time = models.DateTimeField(default=timezone.now)
    Origin = models.CharField(max_length=100, default='WEB')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    snumber = models.IntegerField(primary_key=True, editable=False)
    #tags = models.ManyToManyField("Tag", related_name = "tags", blank=True)
    # views = models.ManyToManyField("User", related_name = "views", blank=True)
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
    def total_views(self):
        return self.views.count()
    
    def snumber(self):
        self.snumber = get_random_string(length=8, allowed_chars='1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        return self.snumber

class Tag(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title    
    
        