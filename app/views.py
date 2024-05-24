from django.shortcuts import render
from .models import Music

def index(request):
    objs = Music.objects.all()
    return render(request,"app/index.html",{'objs':objs})

def music_detail(request, id):
    obj = Music.objects.get(id=id)
    return render(request,"app/music_detail.html",{'obj': obj})