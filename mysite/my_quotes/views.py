import math

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Author, Quote
from .forms import AuthorForm, QuoteForm


def add_author(request):
    
    if request.method == "POST":
        form = AuthorForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect(to="my_quotes:index")
        
        render(request,
               "my_quotes/add_author.html",
               context={"form": form})
    
    return render(request,
                  "my_quotes/add_author.html",
                  context={"form": AuthorForm()})


def add_quote(request):
    
    if request.method == "POST":
        form = QuoteForm(request.POST)
        
        if form.is_valid():
            form.save()            
            return redirect(to="my_quotes:index")        
        
        return render(request, 
                        "my_quotes/add_edit_quote.html",
                        context={"form": form})  
    
    return render(request,
                  "my_quotes/add_edit_quote.html",
                  context={"form": QuoteForm()})
   
def index(request, page:int=1):
    
    count = math.ceil(Quote.objects.count() / 9)
    start = (page - 1) * 9
    end = start + 9
    quotes = Quote.objects.all()[start:end]        
    pages = [i for i in range(page, page+3)]
    
    context={
        "quotes": quotes,
        "count": count,
        "pages": pages,
        "next_page": pages[1],
        "previous_page": pages[0]-1
        }
    
    return render(request,
                  "my_quotes/index.html",
                  context=context)
    
  
def tag(request, tag):
    quotes = Quote.objects.filter(tags__iregex=tag)
    return render(request,
                  "my_quotes/index.html",
                  context={"quotes": quotes,
                           "tag": tag})


def get_author(request, author_name):
    author = Author.objects.filter(fullname=author_name).first()
    return render(request,
                  "my_quotes/author.html",
                  context={"author": author})
    



def edit_quote(request, quote_id):
    
    quote = Quote.objects.get(pk=quote_id)
    quote.tags = ",".join(quote.tags)
    
    if request.method == "POST":
        form = QuoteForm(request.POST, instance=quote)
        
        if form.is_valid():
            form.save()
            return redirect(to="my_quotes:index")
        
        return render(request,
                      "my_quotes/add_edit_quote.html",
                      context={"form": form,
                               "quote_id": quote_id})
        
    form = QuoteForm(instance=quote) 
     
    return render(request,
                  "my_quotes/add_edit_quote.html",
                  context={"form": form,
                           "quote_id": quote_id})


def delete_quote(request, quote_id):
    
    quote = Quote.objects.get(pk=quote_id)
    quote.delete()
    
    return redirect(to="my_quotes:index")

