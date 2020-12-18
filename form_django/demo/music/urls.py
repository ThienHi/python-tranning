from django.urls import path
from . import views

app_name = 'music'
urlpatterns = [
    path('', views.index, name='home'),
    path('add/', views.addMusic, name='addMusic'),
    path('save/', views.saveMusic, name='saveMusic'),
    path('list/', views.listMusic, name='listMusic'),
    path('name/', views.nameSinger, name='nameSinger'),
]
