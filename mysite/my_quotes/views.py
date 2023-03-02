from django.shortcuts import render
from django.http import HttpResponse

from .models import Author, Quote


# Create your views here.
def index(request):
    
    quotes = Quote.objects.all()
    
    return render(request, 
                  "my_quotes/index.html", 
                  context={"quotes": quotes})


