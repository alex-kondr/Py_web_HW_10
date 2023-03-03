from django.shortcuts import render
from django.http import HttpResponse

from .models import Author, Quote


# Create your views here.
def index(request):
    
    quotes = Quote.objects.all()
    
    return render(request, 
                  "my_quotes/index.html", 
                  context={"quotes": quotes})
    

def get_author(request, author_name):
    author = Author.objects.filter(fullname=author_name).first()
    return render(request,
                  "my_quotes/author.html",
                  context={"author": author})
    


