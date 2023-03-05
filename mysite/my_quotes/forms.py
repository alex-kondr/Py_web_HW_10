from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, TextInput, Textarea, ChoiceField

from .models import Quote, Author


class QuoteForm(ModelForm):
    
    quote = Textarea()
    tags = CharField(max_length=500, widget=TextInput())
    author = Author
    user = User
        
    class Meta:
        model = Quote
        fields = ["quote", "tags", "author", "user"]
        # exclude = ["user"]