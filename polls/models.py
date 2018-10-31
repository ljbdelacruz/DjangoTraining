from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date_published')
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    votes = models.IntegerField(0)
    def __str__(self):
        return self.description
    

