from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..wikis.models import WikiPage

# Create your views here.


@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'The api works!'})


@api_view(['POST'])
def get_page_data(request):
    return Response({'message': 'The api works!'})
