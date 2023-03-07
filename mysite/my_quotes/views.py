from django.shortcuts import render, redirect
from django.core.paginator import Paginator

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
    
    quotes = Quote.objects.all()
    
    top_tags = {}
    
    for quote in quotes:
        for tag in quote.tags:
            if top_tags.get(tag):
                top_tags[tag] += 1
            else:
                top_tags.update({tag: 1})
    
    print(top_tags)
    paginator = Paginator(quotes, per_page=9)
    page_object = paginator.get_page(page)
    
    
    context={        
        "page_object": page_object
        }
    
    return render(request,
                  "my_quotes/index.html",
                  context=context)
    
  
def tag(request, tag:str):
    quotes = Quote.objects.filter(tags__iregex=tag)
    return render(request,
                  "my_quotes/index.html",
                  context={"quotes": quotes,
                           "tag": tag})


def get_author(request, author_name:str):
    author = Author.objects.filter(fullname=author_name).first()
    return render(request,
                  "my_quotes/author.html",
                  context={"author": author})
    



def edit_quote(request, quote_id:int):
    
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


def delete_quote(request, quote_id:int, page:int=1):
    
    quote = Quote.objects.get(pk=quote_id)
    quote.delete()
    
    return index(request, page)