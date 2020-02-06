from rest_framework import serializers
from django.http import HttpRequest
from .models import Page, Video, Audio, Text

class PageSerializer(serializers.ModelSerializer):
    details_endpoint = serializers.SerializerMethodField()
    

    class Meta:
        model = Page
        fields = 'id', 'title', 'counter', 'details_endpoint'

    def get_details_endpoint(self, obj):
        request = self.context.get('request')
        url = "{0}://{1}{2}".format(request.scheme, request.get_host(), request.path)
        return url + str(obj.id)

class PageDetailsSerializer(PageSerializer):
    videos = serializers.SerializerMethodField()
    audios = serializers.SerializerMethodField()
    texts  = serializers.SerializerMethodField()

    class Meta:
        model = Page
        fields = 'id', 'title', 'counter', 'videos', 'audios', 'texts'

    def get_videos(self, obj):
        videos = obj.myapi_video.order_by('title')
        video_serializer = VideoSerializer(videos, many=True)
        return video_serializer.data

    def get_audios(self, obj):
        audios = obj.myapi_audio.order_by('title')
        audio_serializer = AudioSerializer(audios, many=True)
        return audio_serializer.data

    def get_texts(self, obj):
        texts = obj.myapi_text.order_by('title')
        text_serializer = TextSerializer(texts, many=True)
        return text_serializer.data

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = '__all__'

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = '__all__'