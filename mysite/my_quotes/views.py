from django.shortcuts import render
from django.http import HttpResponse

from .models import Author, Quote


# Create your views here.
def index(request):    
    quotes = Quote.objects.all()
    
    for quote in quotes:
        tags = quote.tags
        print(f"{tags=}")
        print(type(tags))
        break
        
    return render(request, 
                  "my_quotes/index.html", 
                  context={"quotes": quotes})
    

def get_quotes_by_tags(request, tag):
    
    quotes = Quote.objects.filter(tags__iregex=r'^[humor]^')
    print("+++++++++++++++")
    print(quotes)
    return render(request,
           "my_quotes/tag.html",
           context={"quotes": quotes})


def next_page(request, page_numb):
    quotes = ""
    return render(request,
                  "my_quotes/index.html",
                  context={"quote": quotes})
    

def get_author(request, author_name):
    author = Author.objects.filter(fullname=author_name).first()
    return render(request,
                  "my_quotes/author.html",
                  context={"author": author})
    


