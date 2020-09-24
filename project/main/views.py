from django.shortcuts import render, redirect
from .models import youtube_recent, food
import pandas as pd
import random
import joblib
import gensim

# Create your views here.
ldamodel = joblib.load('ldamodel.pkl')
dictionary = joblib.load('dictionary.pkl')
# topictable dataframe 생성 함수
def make_topictable_per_doc(ldamodel, corpus):
    topic_table = pd.DataFrame()

    # 몇 번째 문서인지를 의미하는 문서 번호와 해당 문서의 토픽 비중을 한 줄씩 꺼내온다.
    for i, topic_list in enumerate(ldamodel[corpus]):
        doc = topic_list[0] if ldamodel.per_word_topics else topic_list
        doc = sorted(doc, key=lambda x: (x[1]), reverse=True)
        # 각 문서에 대해서 비중이 높은 토픽순으로 토픽을 정렬한다.
        # EX) 정렬 전 0번 문서 : (2번 토픽, 48.5%), (8번 토픽, 25%), (10번 토픽, 5%), (12번 토픽, 21.5%), 
        # Ex) 정렬 후 0번 문서 : (2번 토픽, 48.5%), (8번 토픽, 25%), (12번 토픽, 21.5%), (10번 토픽, 5%)
        # 48 > 25 > 21 > 5 순으로 정렬이 된 것.

        # 모든 문서에 대해서 각각 아래를 수행
        for j, (topic_num, prop_topic) in enumerate(doc): #  몇 번 토픽인지와 비중을 나눠서 저장한다.
            if j == 0:  # 정렬을 한 상태이므로 가장 앞에 있는 것이 가장 비중이 높은 토픽
                topic_table = topic_table.append(pd.Series([int(topic_num), round(prop_topic,4)]), ignore_index=True)
                # 가장 비중이 높은 토픽과, 가장 비중이 높은 토픽의 비중을 저장한다.
            else:
                break
    return(topic_table)

def List(request) :
    context = {}

    if request.method == "GET" :
        food = request.GET.getlist('food')
        while ("" in food) :
            food.remove("")
            print("success")

        context["food"] = food

        value = food
        print(value)
        X = " ".join(value)
        documents_input = []
        keyword_input = X.split()
        print(keyword_input)
        

        documents_input.append(keyword_input)
        corpus_input = [dictionary.doc2bow(text) for text in documents_input]
        topictable_input = make_topictable_per_doc(ldamodel, corpus_input)
        topictable_input.columns = ['topic', 'topic_rate']
        # 입력 키워드에 대한 가장 비중이 높은 토픽과, 가장 비중이 높은 토픽의 비중과, 전체 토픽의 비중 출력
        
        topic_result = topictable_input['topic'][0]
        print(topic_result)
        result = youtube_recent.objects.filter(categoryId=topic_result)[:5]
        print(f"1:{result}")

        context['video'] = result
        print(context['video'])
    

    return render(request, 'main/list.html', context)

def video(request, video_id) :
    video = youtube_recent.objects.filter(id=video_id)

    context = {
        'video' : video
    }

    return render(request, 'main/video.html', context)