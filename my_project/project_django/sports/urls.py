from django.urls import path
from . import views

app_name = 'sport'
urlpatterns = [
    path("<int:question_id>/", views.vote, name="vote"),
    path("answer/<int:question_id>", views.answer, name="answer"),
    path("list/", views.listQuestions, name="listQuestions"),
    path("", views.hello, name="Hello")
]
