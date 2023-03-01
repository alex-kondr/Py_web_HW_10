from django.shortcuts import render
from django.http import HttpResponse

# from .models import Question
# from mongo_postgres_db import connect_by_mongo
# from .mongo_db.models_mongo import Author, Quote


# Create your views here.
def index(request):
    # latest_questions = Question.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.question_text for q in latest_questions])
    return HttpResponse()#output)


# def connect_mongo(reguest):
#     author = Author.objects(fullname="Jane Austen").first()
#     return HttpResponse(author.description)