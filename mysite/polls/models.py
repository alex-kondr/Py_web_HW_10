from django.db import models
import dateutil


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    
class Author(models.Model):
    
    fullname = models.CharField(max_length=200)
    born_date = models.DateTimeField(default=dateutil.parser)
    born_location = models.CharField()
    description = models.CharField()
    

class Quote(models.Model):
    
    tags = models.()
    author = ReferenceField(Author)
    quote = models.CharField()