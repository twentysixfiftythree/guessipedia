import json
import random

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from wikis.models import WikiPage

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
