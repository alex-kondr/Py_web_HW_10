import math

from django.shortcuts import render
from django.http import HttpResponse

from .models import Author, Quote


# Create your views here.
# def index(request):    
#     quotes = Quote.objects.all()
    
#     return render(request, 
#                   "my_quotes/index.html", 
#                   context={"quotes": quotes,
#                            "pages": [1, 2, 3],
#                            "count": 10})
    

def tag(request, tag):
    
    quotes = Quote.objects.filter(tags__iregex=tag)
    return render(request,
           "my_quotes/tag.html",
           context={"quotes": quotes,})


def index(request, numb_page=1):
    
    count = math.ceil(Quote.objects.count() / 10)
    start = (numb_page - 1) * 10
    end = start + 10
    quotes = Quote.objects.all()[start:end]        
    pages = [i for i in range(numb_page, numb_page+3)]
    
    return render(request,
                  "my_quotes/index.html",
                  context={"quotes": quotes,
                           "count": count,
                           "pages": pages,
                           "next_page": pages[1],
                           "previous_page": pages[0]-1})
    

def get_author(request, author_name):
    author = Author.objects.filter(fullname=author_name).first()
    return render(request,
                  "my_quotes/author.html",
                  context={"author": author})
    

def login(request):
    pass


def register(request):
    pass
    


