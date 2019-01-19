from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse, HttpRequest
from .models import Question
from django.core.serializers import serialize

def index(request):
    polls = Question.objects.all()[:20]
    data = {"results": list(polls.values("question_text", "pub_date"))}
    return JsonResponse(data)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.
