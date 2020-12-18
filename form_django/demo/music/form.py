from django import forms
from .models import Music


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ('nameSong', 'content', 'created_at')


class Names(forms.Form):
    names = forms.CharField(max_length=20)
    age = forms.IntegerField()
    addresses = forms.CharField(max_length=50)
