from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

url = 'https://bloggame.net/uploads/worigin/2020/03/28/Hinhnendautruongchanlydepnhat15e7eccb8dbb4f_5abfbc798434fbe082a09236905b14df.jpg'


def image(response):
    return HttpResponse('< img src={%url%}/>')
