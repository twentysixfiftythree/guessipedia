import json
import random

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from wikis.models import Score, WikiPage

# Create your views here.


def remove_obvious_links(title, links):

    url_title = title.replace(' ', '_')

    return [link for link in links if url_title not in link]


def string_to_json(title, string):

    array = string.split(',')

    array = remove_obvious_links(title, array)

    dict = {i: array[i].replace('_', ' ') for i in range(0, len(array) - 1)}
    return json.dumps(dict)


@api_view(['GET'])
def get_page_data(request):

    wikis = WikiPage.objects.all()
    wiki = random.choice(wikis)

    all_titles = [wiki.title for wiki in wikis]

    print(wiki.title)
    titles_list = []
    for title in all_titles:
        titles_list.append({"value": title, "label": title})

    return Response(
        {
            'title': wiki.title,
            'link': wiki.link,
            'surrounding_links': wiki.surrounding_links,
            'surrounding_titles': string_to_json(wiki.title, wiki.surrounding_titles),
            'categories': string_to_json(wiki.title, wiki.categories),
            'all_titles': json.dumps(all_titles),
        }
    )


@api_view(['GET'])
def get_all_wikis(request):

    wikis = WikiPage.objects.all()

    return Response(
        {
            'wikis': [
                {
                    'title': wiki.title,
                    'link': wiki.link,
                    'surrounding_links': wiki.surrounding_links,
                    'surrounding_titles': string_to_json(
                        wiki.title, wiki.surrounding_titles
                    ),
                    'categories': string_to_json(wiki.title, wiki.categories),
                }
                for wiki in wikis
            ]
        }
    )


@api_view(['POST'])
def add_score(request):
    print(request.body)
    data = json.loads(request.body)
    score = data.get('score')

    s = Score(score=score)
    s.save()
    return Response({'status': 'success'})


@api_view(['GET'])
def send_stats(request):
    scores = Score.objects.all()

    scores_dict = {'first': 0, 'second': 0, 'third': 0, 'fourth': 0, 'fifth': 0}

    for score in scores:
        if score.score < 20:
            scores_dict['first'] += 1
        elif score.score < 40:
            scores_dict['second'] += 1
        elif score.score < 60:
            scores_dict['third'] += 1
        elif score.score < 80:
            scores_dict['fourth'] += 1
        else:
            scores_dict['fifth'] += 1

    print(scores_dict)

    return Response({'scores': scores_dict})
