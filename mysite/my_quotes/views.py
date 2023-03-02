from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    
    return render(request, 
                  "my_quotes/index.html", 
                  context={"title": "My quotes site"})


