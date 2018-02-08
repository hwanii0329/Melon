from django.urls import path

from artist import views

urlpatterns = [
    path('', views.artist_list, name='artist-list'),
]