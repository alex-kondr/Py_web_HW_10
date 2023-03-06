from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, TextInput, Textarea

from .models import Quote, Author


class QuoteForm(ModelForm):
    
    quote = CharField(widget=Textarea(attrs={"class": "form-control"}))
    tags = CharField(max_length=500, widget=TextInput(attrs={"class": "form-control"}))
    author = Author
    user = User
        
    class Meta:
        model = Quote
        fields = ["quote", "tags", "author", "user"]