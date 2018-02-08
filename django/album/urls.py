from django.urls import path

from album import views

urlpatterns = [
    path('', views.album_list, name='album-list')
]
