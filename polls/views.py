from django.http import JsonResponse
from django.http import HttpResponse
from .models import Question
from .models import QuestionForm
from django.views.decorators.csrf import csrf_exempt

def index(request):
    polls = Question.objects.all()[:20]
    data = {"results": list(polls.values("question_text", "pub_date"))}
    return JsonResponse(data)

@csrf_exempt
def SaveNew(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'saved'})
        else:
            return JsonResponse({'message': 'failed'})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
# Create your views here.
