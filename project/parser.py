# coding: utf-8

import csv
read_list = []

f = open('./KR_youtube_trending_data.csv', 'r', encoding='utf-8-sig')
reader = csv.DictReader(f)
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()

from main.models import youtube
if __name__=='__main__':
    for row in reader:
        youtube(video_id = row['video_id'], title = row['title'], publishedAt = row['publishedAt'], channelId = row['channelId'], categoryId = row['categoryId'], trending_date = row['trending_date'], tags = row['tags'], view_count = row['view_count'], likes = row['likes'], dislikes = row['dislikes'], comment_count = row['comment_count'], thumbnail_link = row['thumbnail_link'], comments_disabled = row['comments_disabled'], ratings_disabled = row['ratings_disabled'], description = row['description']).save()
        print(row['title'] + 'is saved!')
