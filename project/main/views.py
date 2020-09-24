from django.shortcuts import render, redirect
from .models import youtube
import random
# Create your views here.

def List(request) :
    video = youtube.objects.all()
    randomvideo = random.sample(list(video), 7)

    context = {
        'video': randomvideo
    }

    if request.method == "GET" :
        food = request.GET.getlist('food')
        while ("" in food) :
            food.remove("")
            print("success")

        context["food"] = food
        
    

    return render(request, 'main/list.html', context)

def video(request, video_id) :
    video = youtube.objects.filter(id=video_id)

    context = {
        'video' : video
    }

    return render(request, 'main/video.html', context)