from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import PageSerializer, VideoSerializer, AudioSerializer, TextSerializer
from .models import Page, Video, Audio, Text

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all().order_by('title')
    serializer_class = PageSerializer

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().order_by('title')
    serializer_class = VideoSerializer

class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all().order_by('title')
    serializer_class = AudioSerializer

class TextViewSet(viewsets.ModelViewSet):
    queryset = Text.objects.all().order_by('title')
    serializer_class = TextSerializer
    


