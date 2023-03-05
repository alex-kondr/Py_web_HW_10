from django.db import models
from django_mysql.models import ListCharField

    
class User(models.Model):
    
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, default=None)
    phone = models.CharField(max_length=13, default=None)


class Author(models.Model):
    
    fullname = models.CharField(max_length=200)
    born_date = models.DateTimeField()
    born_location = models.CharField(max_length=200)
    description = models.TextField()
    

class Quote(models.Model):
    
    tags = ListCharField(base_field=models.CharField(max_length=50), max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True, null=True)
    
    
