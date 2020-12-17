from django.db import models

# Create your models here.


class questionSports(models.Model):
    questions = models.CharField(max_length=250)
    time_public = models.DateTimeField()


class choicesQuestion(models.Model):
    questions = models.ForeignKey(questionSports, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)
