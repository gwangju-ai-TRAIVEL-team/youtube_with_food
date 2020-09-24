# coding: utf-8

import csv
read_list = []

f = open('./food_topic.csv', 'r', encoding='utf-8-sig')
reader = csv.DictReader(f)
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django
django.setup()

from main.models import food
if __name__=='__main__':
    for row in reader:
        food(food_name = row['food_name'], region = row['지역 / 제조사'], classification = row['식품상세분류'], topic = row['topic'], topic_rate = row['topic_rate']).save()
        print(row['food_name'] + 'is saved!')
