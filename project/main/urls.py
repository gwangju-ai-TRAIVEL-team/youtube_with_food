from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('list/', views.List, name='List'),
    path('video/<int:video_id>', views.video, name='video'),
]
