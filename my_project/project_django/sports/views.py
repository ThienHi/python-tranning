from django.shortcuts import render
from django.http import HttpResponse
from .models import questionSports, choicesQuestion

# Create your views here.


def hello(request):
    name = "Thiện Kim"
    idol = ["Cristiano Ronaldo", "Thiện Hi", "CR7"]
    context = {"name": name, "idol": idol}
    return render(request, "sports/index.html", context)


def listQuestions(request):
    list = questionSports.objects.all()
    answer = choicesQuestion.objects.all()
    context = {"list": list, "answer": answer}
    return render(request, "sports/list_question.html", context)


def answer(request, question_id):
    q = questionSports.objects.get(pk=question_id)
    context = {"answer": q}
    return render(request, "sports/answer.html", context)


def vote(request, question_id):
    q = questionSports.objects.get(pk=question_id)
    try:
        data = request.POST["choice"]
        c = q.choicesquestion_set.get(pk=data)
    except:
        HttpResponse("Error exits data")
    c.vote = c.vote + 1
    c.save()
    return render(request, "sports/vote.html", {"vote": q})
