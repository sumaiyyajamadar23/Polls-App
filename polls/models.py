from django.utils import timezone
import datetime
from django.db import models
from django.contrib import admin


# Create your models here.
class Question(models.Model):
    q_text=models.CharField(max_length=255)
    pub_date=models.DateTimeField(default=timezone.now())
    def __str__(self):
        return self.q_text
    
    @admin.display(
            boolean=True,
            ordering="pub_date",
            description="Published Recently"
    )
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(1)
    
class Choice(models.Model):
    c_text=models.CharField(max_length=255)
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    vote=models.IntegerField(default=0) 
    def __str__(self):
        return self.c_text
    
