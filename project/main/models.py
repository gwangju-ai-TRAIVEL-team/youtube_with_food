from django.db import models

# Create your models here.

class youtube(models.Model) :
    video_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    publishedAt = models.CharField(max_length=100)
    channelId = models.CharField(max_length=50)
    categoryId = models.CharField(max_length=50)
    trending_date = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    view_count = models.CharField(max_length=50)
    likes = models.CharField(max_length=10)
    dislikes = models.CharField(max_length=10)
    comment_count = models.CharField(max_length=10)
    thumbnail_link = models.CharField(max_length=100)
    comments_disabled = models.CharField(max_length=50)
    ratings_disabled = models.CharField(max_length=100)
    description = models.CharField(max_length=200)


class youtube_recent(models.Model) :
    video_id = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    publishedAt = models.CharField(max_length=100)
    channelId = models.CharField(max_length=50)
    categoryId = models.CharField(max_length=50)
    trending_date = models.CharField(max_length=50)
    tags = models.CharField(max_length=50)
    view_count = models.CharField(max_length=50)
    likes = models.CharField(max_length=10)
    dislikes = models.CharField(max_length=10)
    comment_count = models.CharField(max_length=10)
    thumbnail_link = models.CharField(max_length=100)
    comments_disabled = models.CharField(max_length=50)
    ratings_disabled = models.CharField(max_length=100)
    description = models.CharField(max_length=200)

class food(models.Model) :
    food_name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    classification = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    topic_rate = models.CharField(max_length=50)
