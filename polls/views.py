import json
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Question
from .models import QuestionForm
from django.views.decorators.csrf import csrf_exempt

def index(request, format=None):
    polls = Question.objects.all()[:20]
    data = {"results": list(polls.values("question_text", "pub_date"))}
    return JsonResponse(data)

@csrf_exempt
def SaveNew(request, format=None):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'saved'})
        else:
            return JsonResponse({'message': 'failed'})


@csrf_exempt
def results(request):
    if 'application/json' in request.META['CONTENT_TYPE']:
        data = json.loads(request.body)
        question = data.get('question_text', None)
        pub_time = data.get('pub_date', None)

        q = Question(question_text=question, pub_date=pub_time)
        q.save()
        return JsonResponse({'message': 'saved'})
    else:
        return JsonResponse({'message': 'failed'})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.
