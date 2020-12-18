from django.shortcuts import render
from django.http import HttpResponse
from .form import MusicForm, Names
from .models import Music

# Create your views here.


def index(request):
    return HttpResponse("Page MUSIC")


def addMusic(request):
    add = MusicForm()
    return render(request, 'music/addmusic.html', {'add': add})


def saveMusic(request):
    if request.method == "POST":
        q = MusicForm(request.POST)
        if q.is_valid():
            q.save()
            return HttpResponse("Add Music Success")
        else:
            return HttpResponse("Not Validated")
    else:
        return HttpResponse("Method Not Allowed")


def listMusic(request):
    listMusic = Music.objects.all()
    list = {
        "list": listMusic
    }
    return render(request, 'music/listmusic.html', list)

# def updateMusic(request, musicId):


def nameSinger(request):
    name = Names()
    context = {"name": name}
    return render(request, 'music/nameSinger.html', context)
