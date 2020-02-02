from rest_framework import serializers

from .models import Page, Video, Audio, Text

class PageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Page
        fields = ('title', 'counter')

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'counter', 'video_url', 'subs_url')

class AudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Audio
        fields = ('title', 'counter', 'bitrate')

class TextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Audio
        fields = ('title', 'counter', 'content')