from django.shortcuts import render
from django.http import HttpResponse
from . import views

# Create your views here.
def index(request, question_id):
    return HttpResponse("You're looking at the index page")

def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")

def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}")

def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")