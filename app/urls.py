from django.urls import path
from .views import index,music_detail

urlpatterns = [
    path('', index, name="index"),
    path('detail/<int:id>/',music_detail, name="music_detail")
]